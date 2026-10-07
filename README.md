# claude-code-kit

Des règles courtes pour Claude Code, à installer dans `~/.claude/`, pensées pour un travail de recherche publique : simple, sobre, durable. Chaque règle est un fichier indépendant, qu'on installe ou non.

| Règle | Ce qu'elle fait |
|---|---|
| `rules/security.md` et `settings/security.json` | pas de connexion à d'autres machines, pas de lecture de secret, annonce avant d'utiliser un accès en votre nom |

État au 7 octobre 2026, avec Claude Code 2.1.292.

## Installer

**1. Le compte, en premier.** Sur `claude.ai/settings/data-privacy-controls`, décocher l'option qui autorise l'utilisation de vos données pour l'entraînement des modèles (au 7 octobre 2026 : « Allow the use of your chats and coding sessions to train and improve Anthropic AI models »). Elle vaut aussi pour Claude Code. Vos conversations sont alors gardées 30 jours au lieu de 5 ans.

**2. La règle.** Ouvrir Claude Code dans ce dossier et coller :

```text
Installe la règle security de ce dépôt : copie rules/security.md dans
~/.claude/rules/, puis ajoute settings/security.json à mon
~/.claude/settings.json en gardant tout ce qui existe (les règles deny
à la fin de ma liste, dans le même ordre, sans doublon). Ne lis rien
d'autre dans ~/.claude. Montre-moi les changements et attends mon oui.
```

À la main, c'est la même chose : copier le fichier, puis reporter le contenu de `settings/security.json` dans `~/.claude/settings.json`.

**3. Un filet pour git**, valable dans tous vos dépôts : le fichier personnel `CLAUDE.local.md` et les fichiers de secrets ne seront jamais ajoutés par erreur.

```bash
mkdir -p ~/.config/git && printf '%s\n' 'CLAUDE.local.md' '.env' '.env.*' '!.env.example' >> ~/.config/git/ignore
```

Si `git config --global core.excludesFile` affiche un chemin, mettre plutôt ces lignes dans ce fichier-là.

**4. Redémarrer** Claude Code.

Pour mettre à jour : recopier la règle et ajouter les réglages nouveaux, que le `CHANGELOG.md` signale. Pour retirer : supprimer `~/.claude/rules/security.md` et les lignes ajoutées à `~/.claude/settings.json`.

## Dans vos projets

Deux conventions suffisent pour que la règle de sécurité fonctionne :

- les secrets vont dans un `.env` ignoré par git, avec un `.env.example` committé (noms des variables, valeurs factices). Vos programmes chargent le `.env`, Claude lit le `.env.example` ;
- quand Claude annonce un accès externe (un jeton pour une API, un stockage S3…), vous pouvez noter votre accord dans un `CLAUDE.local.md` à la racine du projet, pour ne pas le redonner à chaque session :

  ```markdown
  ## Accès convenus
  - Lecture de l'API <service> avec le jeton `API_TOKEN` du `.env`.
    Les écritures restent à annoncer.
  ```

## Pourquoi ces règles

Claude Code agit avec votre compte : il lit vos fichiers, lance des commandes, utilise vos clés SSH et vos accès réseau. Il n'est pas cloisonné au dossier du projet, et tout ce qu'il lit part chez le fournisseur.

Valider chaque action à la main ne protège pas : les utilisateurs acceptaient 93 % des demandes. Le mode auto, où un second modèle (le classifieur) relit les actions risquées, est devenu le mode par défaut. Il laisse passer environ une action excessive sur six, mais il reste plus attentif qu'une validation par réflexe. La règle de sécurité ne cherche pas à le remplacer : elle pose des limites nettes là où une erreur coûte cher, et laisse le reste au jugement de Claude.

- **Les autres machines.** Claude ne se connecte à aucune autre machine : il prépare les commandes, vous les lancez. Une erreur sur un serveur de production coûte trop cher pour être laissée au classifieur.
- **Les secrets.** Un secret est utilisé par le programme qui le charge (git, un script avec dotenv), jamais lu par Claude. Les interdictions de lecture ne s'appliquent qu'aux outils de Claude, pas aux programmes qu'il lance : c'est ce qui rend la règle praticable.
- **Les accès en votre nom.** Un jeton chargé par un script permet d'agir sur un service externe sans voir le secret. L'action part quand même en votre nom : Claude l'annonce et attend votre oui.
- **Les réglages** désactivent aussi les connecteurs claude.ai (accès large à des contenus privés, non testés ici) et le mode « tout accepter » (il retire le classifieur).

Ces interdictions filtrent la façon dont Claude écrit ses commandes : ce ne sont pas des murs, et une commande écrite autrement passe encore devant le classifieur. Pour un vrai mur, il faut la sandbox de Claude Code ou un conteneur.

Deux détails des réglages, vérifiés sur un poste : les variantes de `.env` sont bloquées partout par `.env.[a-df-z]*` (toute extension qui ne commence pas par « e »), ce qui laisse lisible `.env.example` ; l'exception `!.env.example` ne s'applique qu'aux règles relatives placées avant elle, d'où l'ordre de la liste.

## Ce qui reste à vous

- Les données qui entrent dans la conversation. Chez INRAE, un outil grand public n'est admis que pour des données de sensibilité « public » : pas de données personnelles ni de données de partenaires. Un manuscrit confié pour évaluation n'est pas à vous : Elsevier, Springer Nature et les NIH demandent de ne pas le soumettre à un outil d'IA.
- Le compte et son réglage d'entraînement.

## Sources

- Documentation de Claude Code : [permissions](https://code.claude.com/docs/en/permissions), [modes de permission](https://code.claude.com/docs/en/permission-modes), [mode auto](https://code.claude.com/docs/en/auto-mode-config), [CLAUDE.md et règles](https://code.claude.com/docs/en/memory), [réglages](https://code.claude.com/docs/en/settings), [connecteurs](https://code.claude.com/docs/en/mcp), [données](https://code.claude.com/docs/en/data-usage), [sandbox](https://code.claude.com/docs/en/sandboxing), [bonnes pratiques](https://code.claude.com/docs/en/best-practices).
- Anthropic : [How we built Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode) (taux d'acceptation, erreurs du classifieur) ; [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) (écriture des règles).
- INRAE : [guide du bon usage des IA génératives](https://science-ouverte.inrae.fr/sites/default/files/2026-06/GUIDE_IA_Page_a_p_2605.pdf) et [notice n° 2](https://science-ouverte.inrae.fr/sites/default/files/2026-06/FICHE%20IA_Notice2_2605.pdf) (mai 2026).
- Évaluation par les pairs : [Elsevier](https://www.elsevier.com/about/policies-and-standards/the-use-of-generative-ai-and-ai-assisted-technologies-in-the-review-process), [Springer Nature](https://www.springer.com/us/editorial-policies/artificial-intelligence--ai-/25428500), [NIH](https://grants.nih.gov/grants/guide/notice-files/NOT-OD-23-149.html).
- ANSSI et BSI : [AI Coding Assistants](https://cyber.gouv.fr/nous-connaitre/publications/publications-internationales/ai-coding-assistants/) (2024).

## Licence

GPL-3.0-or-later, voir `LICENSE`.

## Avertissement

Projet communautaire, non affilié à Anthropic. « Claude » et « Claude Code » sont des marques d'Anthropic. Ces règles ne remplacent ni la documentation officielle ni la politique de sécurité de votre établissement.
