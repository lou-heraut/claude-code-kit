---
name: kit-clean
description: "Fait une passe de nettoyage sur un projet, pour remettre l'information à plat, sans doublon ni incohérence, et laisser un état stable."
disable-model-invocation: true
argument-hint: "[partie du projet]"
---

Partie à nettoyer, si elle est précisée : $ARGUMENTS

Prendre le temps d'une passe de nettoyage, sans casser ce qui marche : chercher les incohérences qui ont pu se glisser au fil des modifications, ce qui est périmé, recopié à plusieurs endroits ou rangé au mauvais endroit, ce qui ne sert plus. Le but est un projet cohérent et non ambigu, dont un prochain Claude reprend le contexte en lisant peu.

Ce qui est simple et non ambigu se corrige directement. Le reste s'expose : le constat, les options, celle qu'on recommande. Puis committer, et dire ce qui a été fait et ce qui attend une décision.
