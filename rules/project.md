# Projet

L'organisation d'un projet et de son suivi. Le `CLAUDE.md` du projet prime quand il dit autre chose. Ces conventions guident ce qu'on ajoute ; elles ne justifient pas de réorganiser un projet existant sans demande.

## Où vit l'information

Une information vit à un seul endroit ; les autres fichiers y renvoient au lieu de la recopier. Chaque fichier répond à une question, et n'est créé que lorsqu'il a quelque chose à porter.

```
README.md                        à quoi ça sert, comment s'en servir
ROADMAP.md                       ce qui reste à faire
CHANGELOG.md                     ce qui a été fait, version par version
CLAUDE.md                        comment on travaille ici, ce qu'il ne faut pas casser
CITATION.cff, codemeta.json      qui a fait quoi, comment citer
docs/                            la documentation publiée, s'il y en a une
dev/decisions.md                 ce qui a été décidé, quand et pourquoi
dev/references.md                les sources lues, avec les passages utiles
dev/plans/AAAA-MM-JJ_sujet.md    le fichier de travail d'un point devenu trop lourd
dev/audits/AAAA-MM-JJ_sujet.md   un état des lieux daté, et ce qu'il appelle
```

La racine porte ce qu'on trouve dans tout dépôt ; `docs/` s'adresse aux utilisateurs, `dev/` à qui développe le projet.

Deux fichiers naissent d'une section qui grossit : les sources commencent en fin de README, les décisions dans le `CLAUDE.md`. Une décision s'écrit avec sa date et sa raison, et se corrige ou se remplace quand elle change ; git garde l'historique.

Ce qui est utile au projet (décision, constat, ce qui reste) s'écrit dans ses fichiers, pas dans la mémoire automatique de Claude.

## Plans et audits

`ROADMAP.md` est le plan du projet. Quand un de ses points se révèle bien plus lourd une fois qu'on y est, Claude ouvre un fichier de travail dans `dev/plans/`, pour suivre les sous-étapes sans perdre l'avancée ; `ROADMAP.md` y renvoie tant qu'il est en cours. Ce fichier porte son état en tête (en cours, terminé le …) et reste en place une fois terminé.

Le nom des plans et des audits commence par la date, pour qu'un simple listing les range dans l'ordre. Un audit ne change plus une fois écrit : ses décisions partent dans `dev/decisions.md`, ses tâches dans `ROADMAP.md`.

## Les versions

Ce qui est fait sort de `ROADMAP.md` et entre dans `CHANGELOG.md`, sous « Non publié » (format Keep a Changelog). Quand cette section forme un ensemble utilisable, on publie une version : elle prend un numéro (SemVer) et une date, et le commit reçoit le tag `vX.Y.Z`. Le numéro de version vit à un seul endroit, d'où les autres fichiers le reprennent.

Tenir ce cycle revient à Claude, parce que c'est ce qu'on néglige le plus : le proposer de lui-même, sans attendre qu'on le demande. Sortir de `ROADMAP.md` ce qui est fait, tenir « Non publié » à jour, dire quand il est temps de publier une version.

## Les sessions

Quand le sujet change franchement, ou que la conversation devient longue, proposer de reprendre dans une session vide (`/clear`), après avoir écrit dans les fichiers du projet ce qu'il faut pour repartir.

## Le CLAUDE.md

Court et économe : chaque ligne apporte ce que Claude ne peut pas déduire du code. Ni l'état du projet (`ROADMAP.md`, `CHANGELOG.md`), ni les préférences personnelles (`~/.claude/CLAUDE.md`, `CLAUDE.local.md`), ni les pratiques générales (`~/.claude/rules/`).

## Langue

Ce qui se tape est en anglais : identifiants, noms de fichiers et de dossiers, options, cibles. Ce qui se lit est dans la langue de ses lecteurs : documentation, messages, commits.
