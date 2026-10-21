#!/usr/bin/env python3
"""Temps d'interaction avec Claude Code : une frise par jour et un tableau de plages.

Lit dans ~/.claude/projects/*/*.jsonl l'horodatage, le dossier et le titre des
sessions, jamais le contenu des messages. Les dossiers dont le nom contient
private ou privé sont ignorés. Un message de l'utilisateur ou de Claude compte
comme activité : Claude qui travaille seul, c'est du travail. Le format de ces
fichiers est interne à Claude Code et peut changer d'une version à l'autre.

- Frise : une case par demi-heure, vide quand plus de --pause minutes (15)
  passent sans message.
- Tableau : une plage court tant qu'aucun silence ne dépasse --gap minutes (60).
  Les plages où des sessions de plusieurs projets tournent en même temps sont
  réunies, sur la journée, en un paquet par projet, au prorata de l'activité de
  chacun, et ces paquets se suivent dans le temps de ces plages : les durées
  s'additionnent sans compter deux fois le même temps. Une plage qui passe
  minuit reste sur son jour de départ (fin notée 25:10).

Usage : python3 worktime.py [NOMBRE_DE_JOURS] [--gap 60] [--pause 15]
        1 (par défaut) : aujourd'hui ; 2 : hier et aujourd'hui ; etc.
"""

import argparse
import collections
import datetime as dt
import glob
import json
import os

STEP = dt.timedelta(minutes=5)
QUARTER = dt.timedelta(minutes=15)
DAYS = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
DAYS_FULL = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
MONTHS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
          "août", "septembre", "octobre", "novembre", "décembre"]


def floor5(t):
    return t.replace(minute=t.minute - t.minute % 5, second=0, microsecond=0)


def ceil5(t):
    f = floor5(t)
    return f if f == t else f + STEP


def project_name(cwd, cache={}):
    """Nom du dépôt git qui contient cwd, sinon le dernier dossier."""
    if cwd not in cache:
        d = cwd
        while d not in ("/", "") and not os.path.exists(os.path.join(d, ".git")):
            d = os.path.dirname(d)
        root = d if d not in ("/", "") else cwd
        cache[cwd] = "~" if root == os.path.expanduser("~") else os.path.basename(root)
    return cache[cwd]


def load_events(root, start, end):
    """(heure locale, projet, session) pour chaque message, et les titres."""
    events, titles = [], {}
    for path in glob.glob(os.path.join(root, "*", "*.jsonl")):
        if any(w in path.casefold() for w in ("private", "privé")):
            continue
        if os.path.getmtime(path) < start.timestamp():
            continue
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                if '"ai-title"' in line[:400]:
                    e = json.loads(line)
                    titles[e.get("sessionId")] = e.get("aiTitle")
                    continue
                if '"timestamp"' not in line or not ('"user"' in line or '"assistant"' in line):
                    continue
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("type") not in ("user", "assistant") or e.get("isSidechain"):
                    continue
                cwd = e.get("cwd") or ""
                # Les sessions lancées par un script (claude -p) depuis /tmp
                # tournent pendant une session de travail qui les couvre déjà.
                if cwd.startswith("/tmp") or str(e.get("entrypoint", "")).startswith("sdk"):
                    continue
                t = dt.datetime.fromisoformat(e["timestamp"].replace("Z", "+00:00")).astimezone()
                if start <= t < end:
                    events.append((t, project_name(cwd), e.get("sessionId")))
    return events, titles


def union(intervals):
    out = []
    for a, b in sorted(intervals):
        if out and a <= out[-1][1]:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def blocks(times, gap):
    """Plages arrondies à 5 min : un silence de plus de gap en ouvre une nouvelle."""
    out = []
    for t in sorted(times):
        if out and t - out[-1][1] <= gap:
            out[-1][1] = t
        else:
            out.append([t, t])
    return union([[floor5(a), ceil5(b + STEP)] for a, b in out])


def covers(intervals, t, length=STEP):
    return any(a < t + length and b > t for a, b in intervals)


def clock(t, day0):
    """Heure comptée depuis le minuit du jour de départ : 25:10 après minuit."""
    m = int((t - day0).total_seconds() // 60)
    return f"{m // 60:02d}:{m % 60:02d}"


def chart(days, fine, tz):
    """Une ligne par projet et par jour, une case par demi-heure de 0 h à 24 h.

    █ toute la demi-heure, ▌ le premier quart d'heure, ▐ le second.
    """
    lines = []
    for day in days:
        d0 = dt.datetime.combine(day, dt.time(), tz)
        projects = sorted((p for p in fine if covers(fine[p], d0, dt.timedelta(days=1))),
                          key=lambda p: next(a for a, b in fine[p] if b > d0))
        for i, proj in enumerate(projects):
            cells = ""
            for c in range(48):
                t = d0 + c * 2 * QUARTER
                first, second = covers(fine[proj], t, QUARTER), covers(fine[proj], t + QUARTER, QUARTER)
                cells += {(1, 1): "█", (1, 0): "▌", (0, 1): "▐"}.get((first, second), "·" if c % 2 == 0 else " ")
            label = f"{DAYS[day.weekday()]} {day.day:02d}" if i == 0 else ""
            lines.append((label, proj, cells))
    width = max([len(p) for _, p, _ in lines] + [0])
    ruler = "".join(f"{h}h".ljust(6) for h in range(0, 24, 3))
    out = [f"  {'':6}  {'':{width}}  {ruler}".rstrip()]
    for label, proj, cells in lines:
        if label and len(out) > 1:
            out.append("")
        out.append(f"  {label:6}  {proj:{width}}  {cells}".rstrip())
    return out


def day_rows(day, clusters, coarse, fine, events, titles, tz):
    """Les lignes du tableau pour un jour : (début, fin, projet, minutes, titres, partagée)."""
    day0 = dt.datetime.combine(day, dt.time(), tz)

    def names(proj, spans):
        sids = {s for t, p, s in events if p == proj and any(a <= t < b for a, b in spans)}
        return sorted({titles.get(s) or "(sans titre)" for s in sids})

    rows, parallel = [], []
    for c0, c1 in clusters:
        members = [p for p in coarse if any(a < c1 and b > c0 for a, b in coarse[p])]
        if len(members) == 1:
            m = int((c1 - c0).total_seconds() // 60)
            rows.append((c0, c1, members[0], m, names(members[0], [(c0, c1)]), False))
        else:
            parallel.append((c0, c1, members))
    if not parallel:
        return rows, day0

    # Chaque tranche de 5 min va aux projets qui y échangent des messages,
    # à défaut à ceux dont la plage la couvre.
    share, first = collections.Counter(), {}
    for c0, c1, members in parallel:
        for p in members:
            start = min(a for a, b in coarse[p] if a < c1 and b > c0)
            first[p] = min(first.get(p, start), start)
        t = c0
        while t < c1:
            here = [p for p in members if covers(coarse[p], t)]
            talking = [p for p in here if covers(fine[p], t)] or here
            for p in talking:
                share[p] += 5 / len(talking)
            t += STEP
    span = sum(int((c1 - c0).total_seconds() // 60) for c0, c1, _ in parallel)
    minutes = {p: int(share[p] // 5) * 5 for p in share}
    for p in sorted(share, key=lambda p: share[p] - minutes[p], reverse=True)[: (span - sum(minutes.values())) // 5]:
        minutes[p] += 5

    # Un paquet par projet, à la suite, dans le temps des plages parallèles.
    periods = [(c0, c1) for c0, c1, _ in parallel]
    i, t = 0, periods[0][0]
    for p in sorted(minutes, key=lambda p: first[p]):
        left = minutes[p]
        while left > 0:
            room = int((periods[i][1] - t).total_seconds() // 60)
            if room == 0:
                i, t = i + 1, periods[i + 1][0]
                continue
            take = min(left, room)
            u = t + dt.timedelta(minutes=take)
            rows.append((t, u, p, take, names(p, periods), True))
            left, t = left - take, u
    return sorted(rows), day0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("ndays", nargs="?", type=int, default=1, help="nombre de jours, aujourd'hui compris")
    p.add_argument("--gap", type=int, default=60, help="silence en minutes qui ferme une plage")
    p.add_argument("--pause", type=int, default=15, help="silence en minutes montré comme une pause")
    p.add_argument("--root", default=os.path.expanduser("~/.claude/projects"))
    a = p.parse_args()

    tz = dt.datetime.now().astimezone().tzinfo
    today = dt.date.today()
    days = [today - dt.timedelta(days=k) for k in range(max(a.ndays, 1) - 1, -1, -1)]
    start = dt.datetime.combine(days[0], dt.time(), tz)
    end = dt.datetime.combine(days[-1] + dt.timedelta(days=2), dt.time(), tz)
    events, titles = load_events(a.root, start, end)

    times = collections.defaultdict(list)
    for t, proj, _ in events:
        times[proj].append(t)
    fine = {proj: blocks(ts, dt.timedelta(minutes=a.pause)) for proj, ts in times.items()}
    coarse = {proj: blocks(ts, dt.timedelta(minutes=a.gap)) for proj, ts in times.items()}
    clusters = union([b for bs in coarse.values() for b in bs])

    print()
    print("\n".join(chart(days, fine, tz)))
    print(f"\n  une case = 30 min ; █ actif, ▌ ▐ un quart d'heure sur deux ; vide = plus de {a.pause} min sans message")

    notes = []
    for day in days:
        rows, day0 = day_rows(day, [c for c in clusters if c[0].date() == day], coarse, fine, events, titles, tz)
        if not rows:
            continue
        table = [("projet", "date", "début", "fin", "durée", "")]
        for t0, t1, proj, m, names, shared in rows:
            table.append((proj, f"{day:%d/%m/%Y}", clock(t0, day0), clock(t1, day0),
                          f"{m // 60}:{m % 60:02d}", "partagée" if shared else ""))
            notes.append(f"{day:%d/%m} {clock(t0, day0)} {proj} : {' ; '.join(names)}")
        widths = [max(len(r[i]) for r in table) for i in range(6)]
        print(f"\n  {DAYS_FULL[day.weekday()]} {day.day} {MONTHS[day.month - 1]} {day.year}\n")
        for r in table:
            print(("  " + "  ".join(f"{c:<{w}}" for c, w in zip(r, widths))).rstrip())
    print(f"\n  Une plage se ferme après {a.gap} min sans message. « partagée » : sessions de plusieurs projets en")
    print("  même temps, réunies en un paquet par projet au prorata de l'activité ; leurs heures sont une répartition.")
    print("\n  Titres des sessions, pour nommer l'activité :")
    print("\n".join(f"  {n}" for n in notes))


if __name__ == "__main__":
    main()
