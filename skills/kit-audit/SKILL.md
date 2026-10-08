---
name: kit-audit
description: "Fait un audit d'un projet ou d'une question : rassemble le contexte, cherche en ligne ce qui se fait ailleurs, prend du recul et écrit un état des lieux daté dans dev/audits/. Pour une question de fond, avant une décision importante ou une diffusion."
disable-model-invocation: true
argument-hint: "[sujet et direction]"
---

Sujet et direction de l'audit : $ARGUMENTS

Prendre le temps d'une prise de recul, avec un regard neuf. Rassembler le contexte du projet sur le sujet, puis chercher en ligne ce qui se fait ailleurs : standards proches, pratiques reconnues, solutions élégantes, littérature, et l'état actuel des sources que le projet suit déjà. Confronter la pratique réelle, ce que disent les standards et ce que fait le projet ; quand le projet s'écarte de tout ce qui existe, se demander s'il comble un manque ou s'il fait fausse route. La profondeur suit l'ampleur du sujet.

Écrire l'état des lieux dans `dev/audits/AAAA-MM-JJ_sujet.md` : les constats, chacun avec sa source ; ce qui tient bien ; les décisions à prendre, avec les options et celle qu'on recommande ; ce qu'on attaquerait en premier. L'audit ne corrige rien. Dire ensuite en quelques lignes ce qu'il montre qu'on ne voyait plus.
