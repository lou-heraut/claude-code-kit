---
name: kit-worktime
description: "Résume le temps passé avec Claude Code sur les derniers jours : une frise par jour et un tableau projet, activité, date, début, fin, durée, à reporter dans un emploi du temps."
disable-model-invocation: true
argument-hint: "[nombre de jours, 1 par défaut]"
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/worktime.py *)
---

Nombre de jours, aujourd'hui compris : $ARGUMENTS

Lancer `python3 ${CLAUDE_SKILL_DIR}/worktime.py <nombre de jours>`, avec 1 si rien n'est précisé. Le script lit seulement l'heure des messages, le dossier et le titre des sessions.

Recopier la frise telle quelle, dans un bloc de code : elle montre ce qui s'est passé. Puis donner un tableau Markdown par jour, sous une ligne qui nomme le jour, colonnes alignées : projet, activité, date, début, fin, durée.

Le tableau part de celui du script, mais il cherche des groupes d'activité homogènes et de vraies plages de travail et de réflexion humaine : une pause pour Claude n'en est pas forcément une de l'autre côté. Il peut être malléable sur les horaires, réunir les morceaux d'un même travail, absorber les petits écarts et les fragments de quelques minutes, quitte à perdre un peu en précision, tant qu'il respecte en gros le temps d'activité effectif de la journée. L'activité tient en deux ou trois mots, tirés des titres de sessions que le script liste ; un même travail garde le même nom. Dire en une phrase ce qui a été réparti ou lissé.
