# claude-code-kit

Règles courtes pour Claude Code, installées par copie dans `~/.claude/` (voir le README). Ce fichier dit comment on les écrit et ce qu'il ne faut pas casser.

## Écrire une règle

Une règle est chargée dans le contexte de Claude à chaque session : chaque phrase oriente ce qu'il fait, y compris hors de son sujet. On l'écrit pour Claude seul ; le pourquoi destiné aux humains va dans le README.

Chaque règle a un seul rôle : `security` dit ce qu'on ne fait pas et ce qu'on annonce, `off-limits` ce que Claude ne lit pas, `posture` l'esprit du travail, `project` la vie d'un projet, `writing` ce qu'on écrit et dit. Avant d'ajouter une phrase, vérifier qu'elle va dans la bonne.

Il y a deux sortes de règles :

- **les limites** (`security.md`, `off-limits.md`, `project.md`, `writing.md`) : chaque phrase porte un risque ou un besoin précis, l'action concrète, et ce qu'il faut faire à la place. Une raison courte quand elle aide à l'appliquer. Dire quoi faire plutôt que quoi ne pas faire, quand c'est possible ;
- **la posture** (`posture.md`) : une direction, pas des actes. Elle donne l'esprit dans lequel réfléchir et proposer, avec les mots du mainteneur, choisis pour l'imaginaire qu'ils portent (keep it clean, keep it simple, bloat, pérennité). Elle ne bride ni la créativité ni les propositions qui changent tout, tant qu'elles vont dans ce sens.

Pour les deux :

- Pas de catégorie à surveiller ni de sujet annexe : nommer un thème le rend présent partout.
- Pas de déclencheur d'alerte vague (« signaler », « au moindre soupçon ») : seulement des cas précis.
- Pas d'emphase : ni majuscules, ni gras d'insistance. Les modèles actuels sur-réagissent au langage appuyé (Anthropic, *Prompting best practices*).
- Dire ce qui n'est pas concerné quand une règle pourrait déborder sur l'usage normal, y compris le travail où elle ne joue pas : chargée à chaque session, une règle se glisse sinon dans des conseils qui ne la regardent pas. Une préférence s'énonce comme un fait, pas comme une action, que Claude referait à chaque réponse. Ne rien écrire sur ce que Claude fait déjà bien.
- Court : pour chaque ligne, se demander si l'enlever ferait faire une erreur ; sinon la couper.
- Côté humain, tout se fait une fois, à l'installation : pas de routine, pas de liste de vérifications.
- Chaque règle s'installe seule, sans dépendre d'une autre.

Les skills suivent les mêmes principes. Ils ne se lancent que sur commande (`disable-model-invocation: true`), prennent un thème en argument, et donnent une direction avec les mots du mainteneur plutôt qu'une procédure : ce que disent déjà les règles (où vit l'information, la posture) n'y est pas répété. Une formule qui portait l'enjeu d'une session particulière n'a pas sa place dans un skill général. Les descriptions YAML se mettent entre guillemets.

## Ce qu'il ne faut pas casser

- `rules/security.md` ne vise que trois risques : agir sur une autre machine, lire un secret, utiliser un accès au nom de l'utilisateur sans le dire. Git n'est pas concerné. Ne pas y ajouter de consigne sur les données personnelles, l'infrastructure ou la manière d'écrire dans un dépôt : essayé, cela rendait Claude excessivement prudent.
- Le classifieur du mode auto reste le garde principal. Les réglages ajoutent des interdictions, désactivent les connecteurs claude.ai et le mode « tout accepter », et ne touchent pas à `autoMode` (`autoMode.environment` enverrait des noms de serveurs au fournisseur).
- Un secret est utilisé par les programmes, jamais lu par Claude : les interdictions `Read` ne s'appliquent pas aux sous-processus (git, ssh, script dotenv).
- Règles `.env` : `Read(//**/.env)`, `Read(//**/.env.[a-df-z]*)`, `Read(//**/.env-*)` (un fichier par instance, `.env-demo`) et les copies d'Emacs (`.env~`, `#.env*#`) partout, puis `Read(.env*)` suivi de `Read(!.env.example)` dans le projet. Une exception `!` ne vaut que pour les règles relatives placées avant elle ; la négation entre crochets (`[!e]`) n'est pas reconnue, un intervalle l'est.
- `rules/off-limits.md` vise un mot dans les noms (`private`, `privé`), pas une catégorie de données, et reste hors de `security.md`. Son propre nom ne contient pas ce mot, sinon ses fichiers deviendraient illisibles une fois installés. Ses interdictions sont ancrées au dossier personnel (`~/**/…`) : sur macOS, `/tmp` et `/var` mènent à `/private/…`. `*private*` suffit : un motif qui attrape un dossier bloque aussi son contenu. Motif large voulu, l'ambiguïté prime ; son revers (des fichiers de code illisibles) est dit dans le README. Le filet git ne prend que `private/` : un motif large y ignorerait sans bruit des fichiers de code. La phrase sur les variantes donne ses exemples et laisse lisibles les mots de la même famille : essayé sans, Claude ne lisait plus `privacy.md`, même nommé dans la demande. La dernière phrase cantonne la règle au moment de lire : essayé sans le 19 octobre 2026 (Claude Code 2.1.303), Claude mettait en garde contre le nom `private` dans trois sessions sur trois où personne n'en proposait, et retirait de ses listings les noms qui contiennent `priv`.
- La mémoire automatique est coupée par `settings/project.json`. Relue le 20 octobre 2026 (55 notes), elle recopiait l'état des projets, réapprenait les mêmes préférences d'un projet à l'autre et gardait de chaque recadrage une consigne invisible, parfois contraire aux règles. Ce qui sert va dans les fichiers du projet, dans `~/.claude/CLAUDE.md` ou dans `CLAUDE.local.md`.
- Installation par copie dans `~/.claude/rules/` : un plugin ne peut porter ni règle chargée à chaque session ni interdiction. Pas de script d'installation.
- `kit-start` sert la remise en contexte de Claude, et son retour se limite à l'état de la roadmap et à par quoi on reprend. Ne pas y remettre de prise de recul, de vérification de cohérence ou de point d'avancement : essayé, cela produisait au démarrage un audit de plusieurs pages, impossible à reprendre.
- `project.md` : « un seul endroit » vise ce qui évolue, et laisse une explication se redire ailleurs. Essayé le 20 octobre 2026 avec la formulation large : sur un projet factice, Claude proposait six fois sur six de retirer d'un README une définition déjà dans `docs/`, en citant la règle ; jamais avec la formulation actuelle, qui signale toujours une version recopiée et périmée.
- `project.md` : un fichier de travail dans `dev/plans/` se propose, Claude ne l'ouvre pas de lui-même. Essayé : il en ouvrait d'office, avant même de commencer le point, ou en fin de session pour un point seulement interrompu.
- `project.md` : les repères de `dev/decisions.md` servent d'abord au prochain Claude, qui les tient lui-même et les fait évoluer ; il demande seulement quand il doute. Essayé le 19 octobre 2026 : écrits comme le registre des choix de l'utilisateur, ou versés d'office depuis un audit, ils devenaient des règles figées.
- `posture.md` n'a de phrase ni sur la franchise ni sur le moment où Claude tranche. Proposées le 20 octobre 2026 depuis les notes de mémoire : la franchise, essayée sur trois cas (36 sessions, dont un retour délicat à une déposante), ne changeait rien, Claude étant déjà franc en session neuve ; trancher reste libre, au cas par cas ; « vérifier plutôt que supposer » redisait « chercher ».
- `kit-worktime` est un outil, avec son script (Python, bibliothèque standard), et non une direction : il ne lit des sessions que l'heure des messages, le dossier et le titre. Choisi à l'usage le 22 octobre 2026 : journée de minuit à minuit, plage fermée après une heure sans message (20 minutes coupaient des temps de réflexion), Claude qui travaille seul compte comme du travail, et les sessions parallèles d'une journée réunies en un paquet par projet au prorata, parce que des lignes qui alternent d'un projet à l'autre ne se reportent pas dans un tableur.
- Les skills portent le préfixe `kit-` : on les retrouve en tapant `/kit`, et aucun ne peut entrer en conflit avec une commande intégrée (`/resume`, `/review`…). Ils ne se déclenchent pas seuls, parce qu'une tournure de l'utilisateur suffirait à les lancer à tort.

## Ce dépôt

- Il reproduit `~/.claude/` : `rules/` et `skills/` y sont copiés, `settings/` y est fusionné.
- Racine : `README.md` (s'en servir, pourquoi, sources), `CHANGELOG.md` (ce qui est livré), `ROADMAP.md` (ce qui reste, rien d'autre), ce fichier, `LICENSE`.
- Français pour ce qui se lit (règles, README, commits), anglais pour les noms de fichiers et de dossiers.
- Dépôt public : rien de personnel, aucun nom de serveur ni chemin interne.
- En début de session, avant de toucher à une règle ou un skill, relire la documentation officielle et les conseils d'Anthropic liés dans le README, et l'index de la documentation (https://code.claude.com/docs/llms.txt) pour repérer les pages nouvelles : ils changent avec les versions de Claude Code et les modèles. En dire en quelques lignes ce qui est nouveau ou contredit le dépôt.
- Un fait sur Claude Code vient de la documentation officielle, liée dans le README ; noter la version de Claude Code (`claude --version`) quand on le revérifie.
- Vérifier un réglage dans une session séparée (`claude -p --settings <fichier>`) sur des fichiers factices : la session en cours ne relit plus un fichier de réglages dont le dossier a été supprimé puis recréé.
- Essayer une formulation de règle sans toucher à la copie installée : la poser dans un `CLAUDE.md` du dossier parent d'un projet factice (dans `.claude/rules/`, elle devient un fichier du projet, que Claude commente), écarter la copie installée par `claudeMdExcludes` dans le fichier passé à `--settings`, et passer la formulation actuelle par le même chemin comme témoin. Plusieurs sessions par version, en `--output-format stream-json --verbose`, pour voir ce que Claude ouvre et ce qu'il dit.
- Écrire « INRAE » sans article. Pas de tiret cadratin.
- Ce qui change pour l'utilisateur va dans `CHANGELOG.md`, sous « Non publié ».
