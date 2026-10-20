# Journal des versions

Format [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), numérotation [SemVer](https://semver.org/lang/fr/).

## [Non publié]

### Modifié

- `rules/off-limits.md` : la règle ne joue qu'au moment de lire ; conseils, organisation et choix des noms se font comme si elle n'existait pas. Seules les recherches dans le contenu excluent ces fichiers, et les noms restent visibles. Sans ces précisions, Claude mettait en garde contre le nom `private` quand personne n'en proposait.

- `rules/project.md` : `dev/decisions.md` porte des repères que Claude tient lui-même pour le prochain Claude (ce qu'il déferait ou referait sinon, avec sa raison) et qu'il change quand ils ne tiennent plus ; il demande seulement quand il doute. Les choix nés d'un audit n'y partent plus d'office.

## [1.1.0] - 2026-10-17

### Ajouté

- `rules/off-limits.md`, avec `settings/off-limits.json` : ce dont le nom contient `private` ou `privé`, fichier ou dossier, Claude ne le lit pas ; pour une variante proche (`prive` sans accent, une faute de frappe), il demande. La lecture en est interdite sous le dossier personnel. Le filet git de l'installation ignore les dossiers `private/`.

### Modifié

- `settings/security.json` : bloque aussi les copies qu'Emacs laisse à côté d'un `.env` (`.env~`, `#.env#`). Pour une installation existante, ajouter `Read(//**/.env~)` et `Read(//**/#.env*#)` après `Read(//**/.env.[a-df-z]*)`.

## [1.0.0] - 2026-10-11

### Ajouté

- `rules/security.md` : ne pas se connecter à d'autres machines, ne pas lire de secret, annoncer avant d'utiliser un accès au nom de l'utilisateur. Git n'est pas concerné.
- `settings/security.json` : interdit `ssh`, `scp`, `sftp`, `rsync` et la lecture des fichiers de secrets (`~/.ssh`, `.env` et ses variantes sauf `.env.example`, identifiants des outils, historiques shell) ; désactive les connecteurs claude.ai et le mode « tout accepter ».
- `rules/posture.md` : l'esprit du travail, en un paragraphe.
- `rules/project.md` : où vit l'information dans un projet (la racine, `docs/` pour la documentation publiée, `dev/` pour le travail : les choix qui émergent, les sources, les fichiers de travail des points devenus trop lourds, les audits datés), le passage de `ROADMAP.md` aux versions, tenu par Claude, les sessions, le `CLAUDE.md`, la langue.
- `rules/writing.md` : tableaux alignés, peu de tirets cadratins, pas de superlatif, choses nommées en mots plutôt que par leurs identifiants, faits sourcés, choix exposés en prose (petits choix en liste, sujet à comprendre présenté seul).
- Skills `kit-start`, `kit-end`, `kit-clean` et `kit-audit`, lancés seulement à la demande : reprendre le contexte, mettre à plat une session, nettoyer un projet, faire un audit daté.
- Installation en quatre étapes, la même pour chaque règle et chaque skill, dans le README.

[Non publié]: https://github.com/lou-heraut/claude-code-kit/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/lou-heraut/claude-code-kit/releases/tag/v1.1.0
[1.0.0]: https://github.com/lou-heraut/claude-code-kit/releases/tag/v1.0.0
