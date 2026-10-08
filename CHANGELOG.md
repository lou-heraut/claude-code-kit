# Journal des versions

Format [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/), numérotation [SemVer](https://semver.org/lang/fr/).

## [Non publié]

### Ajouté

- `rules/security.md` : ne pas se connecter à d'autres machines, ne pas lire de secret, annoncer avant d'utiliser un accès au nom de l'utilisateur. Git n'est pas concerné.
- `settings/security.json` : interdit `ssh`, `scp`, `sftp`, `rsync` et la lecture des fichiers de secrets (`~/.ssh`, `.env` et ses variantes sauf `.env.example`, identifiants des outils, historiques shell) ; désactive les connecteurs claude.ai et le mode « tout accepter ».
- `rules/posture.md` : l'esprit du travail, en un paragraphe.
- `rules/project.md` : où vit l'information dans un projet (la racine, `docs/` pour la documentation publiée, `dev/` pour le travail : décisions, sources, plans et audits datés), le passage de `ROADMAP.md` aux versions, les sessions, le `CLAUDE.md`, la langue.
- `rules/writing.md` : tableaux alignés, peu de tirets cadratins, pas de superlatif, faits sourcés, choix exposés en prose.
- Skills `kit-start`, `kit-end`, `kit-clean` et `kit-audit`, lancés seulement à la demande : reprendre le contexte, mettre à plat une session, nettoyer un projet, faire un audit daté.
- Installation en quatre étapes, la même pour chaque règle et chaque skill, dans le README.
