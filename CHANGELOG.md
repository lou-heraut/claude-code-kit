# Journal des versions

Format [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), numérotation [SemVer](https://semver.org/lang/fr/).

## [Non publié]

### Ajouté

- `rules/security.md` : ne pas se connecter à d'autres machines, ne pas lire de secret, annoncer avant d'utiliser un accès au nom de l'utilisateur. Git n'est pas concerné.
- `settings/security.json` : interdit `ssh`, `scp`, `sftp`, `rsync` et la lecture des fichiers de secrets (`~/.ssh`, `.env` et ses variantes sauf `.env.example`, identifiants des outils, historiques shell) ; désactive les connecteurs claude.ai et le mode « tout accepter ».
- `rules/posture.md` : l'esprit du travail, en un paragraphe.
- `rules/project.md` : où vit l'information dans un projet, le passage de la feuille de route aux versions, les sessions, le `CLAUDE.md`, la langue.
- `rules/writing.md` : tableaux alignés, peu de tirets cadratins, pas de superlatif, faits sourcés, choix exposés en prose.
- Installation en quatre étapes, la même pour chaque règle, dans le README.
