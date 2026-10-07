# Feuille de route

Ce qui reste à faire. Ce qui est livré part dans `CHANGELOG.md`.

## Prochaines étapes

1. `rules/posture.md`, la manière de travailler : le contexte de la recherche publique (lisible, reproductible, maintenable par peu de personnes pendant des années) et ce qu'il implique. Faire ce qui est demandé sans ajouter, s'aligner sur l'existant, préférer le plus simple, écrire sobrement.
2. `rules/project.md`, l'organisation d'un projet : une information à un seul endroit ; les fichiers de la racine et la question à laquelle chacun répond ; un `CLAUDE.md` court, sans état du projet, sans préférence personnelle ni pratique générale ; la langue ; vérifier avant d'affirmer ; où vont les sources (une section du README, puis `docs/references.md` quand elle grossit).
   Constats tirés de projets existants, à traiter : `CLAUDE.md` de plus de 400 lignes ; pratiques générales recopiées d'un dépôt à l'autre ; préférences personnelles dans des fichiers partagés ; un même rôle sous trois noms (`ROADMAP.md`, `dev/points_ouverts.md`, `docs/dev/CHANTIERS.md`) ; règles de langue contradictoires ; emphase (majuscules, gras) ; état du projet écrit dans le `CLAUDE.md`.
3. Publier la version 1.0.0.

## Plus tard

- Règles optionnelles, que chacun installe ou non, par exemple un détecteur de secrets avant commit. Deux voies, chacune avec un défaut : l'imposer (il contrôlerait Claude) ou le proposer (un outil tiers à installer).
- Skills (`~/.claude/skills/`) pour les prompts de session : reprise, clôture, audit d'un projet.
- Mémoire automatique de Claude Code : la couper (réglage du poste) ou la relire régulièrement (pratique).
- AGENTS.md, le format commun à plusieurs agents de code.
