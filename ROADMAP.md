# Feuille de route

Ce qui reste à faire. Ce qui est livré part dans `CHANGELOG.md`.

## À reprendre

1. `off-limits` : dans une conversation sur des données personnelles, Claude a prévenu de lui-même qu'un fichier nommé `private` deviendrait illisible, alors que personne n'en proposait ; ailleurs, il retire des listings les noms qui contiennent `priv`, alors que la règle ne vise que le contenu. Mesurer par un essai sur une question proche avant de toucher au texte.
2. Mémoire automatique de Claude Code : la couper (réglage du poste) ou la relire régulièrement. Elle porte d'une session à l'autre un cadre tiré d'un recadrage : une prudence excessive après une remarque de l'utilisateur (8 octobre 2026), puis trois notes de conduite écrites en une session (19 octobre : tenir un critère de risque proportionné, être franc plutôt que lisse, tirer d'une correction une direction générale plutôt que le cas). Leur fond rejoint parfois le kit : voir s'il a sa place dans une règle.
3. Observer à l'usage les repères de `project.md` : Claude écrit-il encore des choix comme des règles, demande-t-il trop souvent ?

## Plus tard

- Règles optionnelles, que chacun installe ou non, par exemple un détecteur de secrets avant commit. Deux voies, chacune avec un défaut : l'imposer (il contrôlerait Claude) ou le proposer (un outil tiers à installer).
- AGENTS.md, le format commun à plusieurs agents de code.
- Copies d'éditeur des autres fichiers de secrets : `security.json` bloque celles d'un `.env` (`.env~`, `#.env*#`), pas celles de `.Renviron` ni de `~/.pgpass` ou `~/.netrc`. Les ajouter une à une, ou conseiller dans le README de ranger les sauvegardes de l'éditeur dans un dossier interdit à la lecture (fait sur un poste avec Emacs).
