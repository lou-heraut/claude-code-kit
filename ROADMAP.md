# Feuille de route

Ce qui reste à faire. Ce qui est livré part dans `CHANGELOG.md`.

## Prochaines étapes

1. `rules/project.md`, l'organisation d'un projet : une information à un seul endroit ; les fichiers de la racine et la question à laquelle chacun répond ; un `CLAUDE.md` court, sans état du projet, sans préférence personnelle ni pratique générale ; la langue ; vérifier avant d'affirmer ; où vont les sources (une section du README, puis `docs/references.md` quand elle grossit).
   Constats tirés de projets existants, à traiter : `CLAUDE.md` de plus de 400 lignes ; pratiques générales recopiées d'un dépôt à l'autre ; préférences personnelles dans des fichiers partagés ; un même rôle sous trois noms (`ROADMAP.md`, `dev/points_ouverts.md`, `docs/dev/CHANTIERS.md`) ; règles de langue contradictoires ; emphase (majuscules, gras) ; état du projet écrit dans le `CLAUDE.md`.
2. Publier la version 1.0.0 (sécurité, posture, projet).
3. Les skills (`skills/`, copiés dans `~/.claude/skills/`), à écrire à partir des prompts de session qui ont fait leurs preuves. Le but commun : qu'un prochain Claude puisse reprendre proprement le travail.
   - reprise : lire la structure du projet et les fichiers qui disent où il en est, dans l'ordre, avant de toucher à quoi que ce soit ;
   - fin de session : verser dans les fichiers du projet ce que la session a appris (décisions, constats, ce qui reste), au lieu de le laisser dans la mémoire locale de Claude ;
   - nettoyage : remettre le projet d'aplomb (une information à un seul endroit, une roadmap qui rétrécit, chaque fichier à sa place) ;
   - audit : chercher en ligne et rassembler le contexte avant de conclure, puis écrire un `AUDIT.md` daté.
   Noms à choisir en évitant les commandes intégrées de Claude Code (`/resume`, `/context` existent déjà).

## Plus tard

- Règles optionnelles, que chacun installe ou non, par exemple un détecteur de secrets avant commit. Deux voies, chacune avec un défaut : l'imposer (il contrôlerait Claude) ou le proposer (un outil tiers à installer).
- Mémoire automatique de Claude Code : ce qui est utile au projet vit dans le dépôt. Reste à décider s'il faut la couper (réglage du poste) ou la relire régulièrement.
- AGENTS.md, le format commun à plusieurs agents de code.
