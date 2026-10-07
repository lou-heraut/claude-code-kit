# claude-code-kit

Règles courtes pour Claude Code, installées par copie dans `~/.claude/` (voir le README). Ce fichier dit comment on les écrit et ce qu'il ne faut pas casser.

## Écrire une règle

Une règle est chargée dans le contexte de Claude à chaque session : chaque phrase oriente ce qu'il fait, y compris hors de son sujet. On l'écrit pour Claude seul ; le pourquoi destiné aux humains va dans le README.

- Une phrase porte un risque ou un besoin précis, l'action concrète, et ce qu'il faut faire à la place. Une raison courte quand elle aide à appliquer la règle.
- Dire quoi faire plutôt que quoi ne pas faire, quand c'est possible.
- Pas de catégorie à surveiller ni de sujet annexe : nommer un thème le rend présent partout.
- Pas de déclencheur d'alerte vague (« signaler », « au moindre soupçon ») : seulement des cas précis.
- Pas d'emphase : ni majuscules, ni gras d'insistance. Les modèles actuels sur-réagissent au langage appuyé (Anthropic, *Prompting best practices*).
- Dire ce qui n'est pas concerné quand une règle pourrait déborder sur l'usage normal. Ne rien écrire sur ce que Claude fait déjà bien.
- Court : pour chaque ligne, se demander si l'enlever ferait faire une erreur ; sinon la couper.
- Côté humain, tout se fait une fois, à l'installation : pas de routine, pas de liste de vérifications.
- Chaque règle s'installe seule, sans dépendre d'une autre.

## Ce qu'il ne faut pas casser

- `rules/security.md` ne vise que trois risques : agir sur une autre machine, lire un secret, utiliser un accès au nom de l'utilisateur sans le dire. Git n'est pas concerné. Ne pas y ajouter de consigne sur les données personnelles, l'infrastructure ou la manière d'écrire dans un dépôt : essayé, cela rendait Claude excessivement prudent.
- Le classifieur du mode auto reste le garde principal. Les réglages ajoutent des interdictions, désactivent les connecteurs claude.ai et le mode « tout accepter », et ne touchent pas à `autoMode` (`autoMode.environment` enverrait des noms de serveurs au fournisseur).
- Un secret est utilisé par les programmes, jamais lu par Claude : les interdictions `Read` ne s'appliquent pas aux sous-processus (git, ssh, script dotenv).
- Règles `.env` : `Read(//**/.env)` et `Read(//**/.env.[a-df-z]*)` partout, puis `Read(.env*)` suivi de `Read(!.env.example)` dans le projet. Une exception `!` ne vaut que pour les règles relatives placées avant elle ; la négation entre crochets (`[!e]`) n'est pas reconnue, un intervalle l'est.
- Installation par copie dans `~/.claude/rules/` : un plugin ne peut porter ni règle chargée à chaque session ni interdiction. Pas de script d'installation.

## Ce dépôt

- Il reproduit `~/.claude/` : `rules/` y est copié, `settings/` y est fusionné.
- Racine : `README.md` (s'en servir, pourquoi, sources), `CHANGELOG.md` (ce qui est livré), `ROADMAP.md` (ce qui reste, rien d'autre), ce fichier, `LICENSE`.
- Français pour ce qui se lit (règles, README, commits), anglais pour les noms de fichiers et de dossiers.
- Dépôt public : rien de personnel, aucun nom de serveur ni chemin interne.
- Un fait sur Claude Code vient de la documentation officielle, liée dans le README ; noter la version de Claude Code (`claude --version`) quand on le revérifie.
- Écrire « INRAE » sans article. Pas de tiret cadratin.
- Ce qui change pour l'utilisateur va dans `CHANGELOG.md`, sous « Non publié ».
