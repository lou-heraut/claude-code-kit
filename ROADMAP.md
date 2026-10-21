# Feuille de route

Ce qui reste à faire. Ce qui est livré part dans `CHANGELOG.md`.

## À reprendre

1. `project.md` (section « Les sessions ») et `kit-end` : Claude propose trop souvent de vider le contexte, alors qu'une longue session qui marche bien vaut plus qu'une reprise. Le proposer quand le travail devient brouillon, qu'on se perd dans un désaccord, ou que les sujets accumulés diluent la précision ; la longueur seule ne suffit pas.
2. Observer à l'usage les changements de la 1.2.0 : avec les repères de `project.md`, Claude écrit-il encore des choix comme des règles, demande-t-il trop souvent ? Avec `off-limits`, parle-t-il encore de la règle hors des lectures ?

## Plus tard

- Règles optionnelles, que chacun installe ou non, par exemple un détecteur de secrets avant commit. Deux voies, chacune avec un défaut : l'imposer (il contrôlerait Claude) ou le proposer (un outil tiers à installer).
- AGENTS.md, le format commun à plusieurs agents de code.
- Copies d'éditeur des autres fichiers de secrets : `security.json` bloque celles d'un `.env` (`.env~`, `#.env*#`), pas celles de `.Renviron` ni de `~/.pgpass` ou `~/.netrc`. Les ajouter une à une, ou conseiller dans le README de ranger les sauvegardes de l'éditeur dans un dossier interdit à la lecture (fait sur un poste avec Emacs).
