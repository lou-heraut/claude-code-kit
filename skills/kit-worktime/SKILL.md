---
name: kit-worktime
description: "Résume le temps passé avec Claude Code sur les derniers jours : une frise par jour et un tableau projet, activité, date, début, fin, durée, à reporter dans un emploi du temps."
disable-model-invocation: true
argument-hint: "[nombre de jours, 1 par défaut]"
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/worktime.py *)
---

Nombre de jours, aujourd'hui compris : $ARGUMENTS

Lancer `python3 ${CLAUDE_SKILL_DIR}/worktime.py <nombre de jours>`, avec 1 si rien n'est précisé. Le script lit seulement l'heure des messages, le dossier et le titre des sessions.

Recopier la frise telle quelle, dans un bloc de code. Puis donner un tableau Markdown par jour, sous une ligne qui nomme le jour, colonnes alignées : projet, activité, date, début, fin, durée. L'activité tient en deux ou trois mots, tirés des titres de sessions que le script liste ; un même travail garde le même nom d'une ligne à l'autre. Dire en une phrase quelles lignes viennent de sessions parallèles, dont les heures sont une répartition.
