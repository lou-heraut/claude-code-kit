# Feuille de route

Ce qui reste à faire. Ce qui est livré part dans `CHANGELOG.md`.

## Prochaines étapes

1. Vérifier sur macOS le motif accentué de `off-limits` (`*privé*`).

## Plus tard

- Règles optionnelles, que chacun installe ou non, par exemple un détecteur de secrets avant commit. Deux voies, chacune avec un défaut : l'imposer (il contrôlerait Claude) ou le proposer (un outil tiers à installer).
- Mémoire automatique de Claude Code : ce qui est utile au projet vit dans le dépôt. Reste à décider s'il faut la couper (réglage du poste) ou la relire régulièrement ; un essai l'a vue garder d'une session à l'autre une prudence excessive après une remarque de l'utilisateur.
- AGENTS.md, le format commun à plusieurs agents de code.
- Copies d'éditeur des autres fichiers de secrets : `security.json` bloque celles d'un `.env` (`.env~`, `#.env*#`), pas celles de `.Renviron` ni de `~/.pgpass` ou `~/.netrc`. Les ajouter une à une, ou conseiller dans le README de ranger les sauvegardes de l'éditeur dans un dossier interdit à la lecture (fait sur un poste avec Emacs).
