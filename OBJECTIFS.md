# Objectifs et référentiel pédagogique de la collection

## 1. Rôle de ce document

Ce fichier est le cahier des charges de toute création, correction ou révision
pédagogique. Le lire avant de planifier un niveau, de rédiger un chapitre ou de
modifier un exercice. `AGENTS.md` précise les règles de contribution ; le README
explique l'organisation technique. En cas de contradiction pédagogique entre un
cours existant et ce référentiel, documenter l'écart et proposer sa correction.
Une évolution de ces objectifs doit être explicite dans la PR concernée.

L'ambition est de permettre à un lecteur francophone de construire, du primaire
au supérieur, les connaissances et l'autonomie correspondant progressivement à
un **niveau master de mathématiques**. La collection ne délivre aucun diplôme et
sa seule lecture ne garantit pas ce niveau : la résolution autonome de problèmes,
la rédaction de preuves et l'évaluation des acquis sont indispensables.

Un master possède une spécialisation : il n'existe pas un programme unique couvrant
toutes les mathématiques. Construire d'abord un socle solide, puis annoncer le ou
les parcours retenus, leurs prérequis et leurs limites. Ne pas confondre une
introduction intuitive à un sujet de master avec sa maîtrise.

## 2. Public, accessibilité et méthode de travail

Permettre à la fois l'apprentissage scolaire, la reprise d'études et le travail
autonome. Chaque volume indique le public, la filière, les connaissances requises
et un diagnostic initial corrigé. Proposer des renvois précis pour combler les
lacunes sans imposer la lecture de tous les volumes précédents.

Écrire en français clair, avec un vocabulaire précis expliqué à sa première
apparition. Ne pas utiliser « évident », « trivial » ou « on voit bien » pour
remplacer une étape essentielle. Décomposer les difficultés nouvelles et faire
varier les exemples. Préserver une présentation sobre, imprimable, lisible sans
couleur et avec des figures légendées, des unités et des échelles explicites.

Le lecteur doit pratiquer : alterner compréhension, entraînement, mémorisation,
restitution sans support et problèmes nouveaux. Prévoir des révisions espacées
et des exercices mêlant plusieurs chapitres. Les durées proposées sont indicatives.

## 3. Étapes du parcours et acquis attendus

Cette feuille de route donne une direction ; elle ne remplace pas la vérification
des programmes officiels ni le choix documenté d'un parcours universitaire.

| Étape | Fondations à construire | Manifestations observables de maîtrise |
| --- | --- | --- |
| Primaire : CP à CM2 | Numération, sens des opérations, calcul, premières fractions et décimaux, grandeurs, mesures, espace, figures et problèmes | Expliquer une procédure, choisir une opération, représenter une situation, contrôler un ordre de grandeur et une unité |
| Collège : sixième à troisième | Nombres, proportionnalité, calcul littéral, équations, géométrie, fonctions, statistiques, probabilités et algorithmes selon les programmes | Traduire un énoncé, justifier un calcul, enchaîner un raisonnement, construire et exploiter une figure, critiquer un résultat |
| Lycée : seconde à terminale | Algèbre, fonctions, suites, analyse, géométrie, probabilités et programmation selon la filière et les options annoncées | Manipuler les définitions, démontrer des résultats accessibles, modéliser, reconnaître les hypothèses d'une méthode et résoudre une synthèse |
| Licence : L1 à L3 | Logique et ensembles, algèbre linéaire et bilinéaire, analyse réelle et multivariable, structures algébriques, topologie, intégration, probabilités et méthodes numériques | Lire et rédiger des preuves abstraites, construire des contre-exemples, articuler plusieurs théorèmes, justifier convergence et approximations |
| Master : M1 et M2 | Approfondissements cohérents dans une ou plusieurs spécialités explicitement définies | Étudier des textes avancés, mobiliser des résultats avec leurs hypothèses, résoudre des problèmes substantiels et mener un projet mathématique documenté |

La licence devra préparer notamment les espaces vectoriels et applications
linéaires, les groupes et anneaux, les suites et séries, les espaces métriques,
la compacité et la complétude, le calcul différentiel, la mesure et l'intégration,
les équations différentielles et les probabilités. Leur répartition exacte par
année sera justifiée par les dépendances, et non présentée comme un programme
national universitaire uniforme.

Les orientations de master pourront comprendre analyse fonctionnelle et EDP,
algèbre et géométrie, probabilités et statistiques, optimisation et calcul
scientifique. Choisir les orientations avant de revendiquer leur couverture ;
prévoir des bibliographies, problèmes longs et projets, puis un travail de
synthèse autonome avec présentation écrite et discussion critique des résultats.

## 4. Exhaustivité, sources et limites annoncées

Pour chaque classe scolaire, vérifier les textes officiels applicables, la date
d'entrée en vigueur, la filière et les options. Conserver les liens et la date de
consultation dans le guide. Distinguer programme en vigueur et programme futur.
Pour le supérieur, définir un syllabus et citer les références institutionnelles
ou universitaires choisies ; expliquer les éventuels écarts entre parcours.

Maintenir une table de couverture avec au minimum :

| Exigence ou compétence | Source et statut | Prérequis | Chapitre | Exercices et corrigés | État de validation |
| --- | --- | --- | --- | --- | --- |
| Une ligne par notion, capacité, démonstration ou algorithme attendu | Programme obligatoire / rappel / approfondissement | Renvois précis | Section identifiable | Numéros stables | À rédiger / à vérifier / validé |

Inclure les exigences transversales : automatismes, raisonnement, représentation,
communication, calcul, modélisation et algorithmique. Ne pas limiter la couverture
aux titres de chapitres. Un sujet seulement mentionné n'est pas couvert : il faut
les explications et une possibilité de mettre la compétence en pratique.

Ne jamais annoncer « complet » tant que les exigences du périmètre annoncé ne
sont pas vérifiées. Énumérer explicitement les limites et les éléments différés.
Les compléments ne compensent pas une lacune dans le programme obligatoire.

## 5. Définitions, démonstrations et dépendances

Distinguer systématiquement : définition, axiome ou fondement admis, conjecture,
proposition démontrée, méthode pratique, approximation et complément hors programme.
Une définition fixe le sens d'un objet ; elle ne se démontre pas. En revanche,
l'existence de l'objet défini, son unicité ou l'équivalence de deux définitions
peuvent nécessiter une preuve.

Pour toute propriété ou formule importante :

1. Introduire le problème ou l'intuition qui la motive.
2. Énoncer précisément les hypothèses, le domaine de validité et la conclusion.
3. Donner une preuve accessible avec les prérequis disponibles ; citer les résultats utilisés.
4. Développer un exemple et, lorsque pertinent, un cas limite ou un contre-exemple
   montrant ce qui échoue si une hypothèse est retirée.
5. Expliquer les usages présents et les réemplois futurs.

Démontrer autant que possible les formules algébriques, résultats géométriques,
règles de calcul, théorèmes d'analyse et identités probabilistes. Justifier les
transformations d'équations et inéquations : réversibilité, division par une
quantité non nulle, signe, domaine, solutions extraites ou introduites.

En géométrie, distinguer observation et preuve ; préciser les propriétés admises,
les cas dégénérés et les conditions de construction. Un dessin convaincant, une
mesure ou cent simulations ne constituent pas une preuve générale.

Lorsqu'une démonstration dépasse le niveau : signaler l'admission au point d'usage,
expliquer pourquoi, indiquer les prérequis manquants et où elle sera reprise.
Maintenir dans le guide un registre des admissions : résultat, usages, justification
disponible, preuve future et statut. Ne pas annoncer une preuve future comme déjà
rédigée. Éviter les dépendances circulaires entre chapitres et entre volumes.

La rigueur doit être adaptée à l'âge : manipulation et explication verbale au
primaire, raisonnement progressivement structuré au collège, formalisation au
lycée et autonomie dans les preuves au supérieur. Ne pas surcharger un débutant
d'un formalisme inutile, ni masquer une hypothèse nécessaire.

## 6. Construction de chaque chapitre

Chaque chapitre doit permettre de répondre à : « Que vais-je apprendre ? De quoi
ai-je besoin ? Pourquoi cela fonctionne-t-il ? Quand cela sert-il ? Suis-je capable
de l'utiliser seul ? » Prévoir, avec une longueur adaptée :

- Objectifs observables et prérequis avec renvois et courte remise en mémoire.
- Situation motivante, vocabulaire, notations et définitions précises.
- Résultats et démonstrations, en distinguant le statut de chaque affirmation.
- Exemples résolus avec les décisions expliquées, pas uniquement les calculs.
- Méthodes et critères de choix, erreurs fréquentes, contre-exemples et contrôles.
- Synthèse des idées, formules avec hypothèses et questions d'autoévaluation.
- Exercices gradués, renvois aux corrigés et prolongements identifiés.
- Section « Utilité et suite du parcours » avec applications concrètes.

La progression n'est pas une accumulation de formules : faire relier différentes
représentations d'un même objet (énoncé, figure, tableau, graphe, formule, algorithme).
Définir les notations avant usage et conserver leur cohérence entre volumes.

## 7. Raisonnement et préparation au supérieur

Introduire progressivement les ensembles, les fonctions, les quantificateurs,
les implications et équivalences, les conditions nécessaires et suffisantes,
les raisonnements directs, par cas, par contraposée, par l'absurde et par récurrence.
Travailler la négation d'un énoncé et la différence entre exemple et contre-exemple.

Au supérieur, expliciter existence et unicité, bonne définition des applications,
structures et morphismes, changements de représentation et portée des théorèmes.
Apprendre à chercher une preuve : petits cas, conjecture, recherche de contre-exemple,
décomposition en lemmes, rédaction et relecture critique.

Ne pas anticiper un outil uniquement pour son prestige. Un complément doit avoir
un bénéfice pédagogique, des prérequis identifiés et un chemin de lecture qui
permette de poursuivre le programme obligatoire sans l'avoir étudié.

## 8. Utilité et liens entre les domaines

Pour les outils importants, donner au moins un usage actuel et, lorsqu'il existe,
un réemploi futur précis. Exemples de fils conducteurs à développer :

| Outil initial | Réemploi à construire progressivement |
| --- | --- |
| Fractions, proportions et unités | Taux, changement d'échelle, analyse dimensionnelle, probabilités |
| Calcul littéral et factorisation | Polynômes, résolution d'équations, structures algébriques |
| Vecteurs et produit scalaire | Algèbre linéaire, projections, moindres carrés, espaces de Hilbert |
| Suites et dérivation | Convergence, approximation locale, optimisation, équations différentielles |
| Aires et sommes | Intégration, mesure, espérance |
| Probabilités finies et statistiques | Variables aléatoires, estimation, convergence et inférence |
| Algorithmes et approximations | Analyse numérique, stabilité, complexité et calcul scientifique |

Expliquer le mécanisme du lien avec un exemple ; une liste de noms de domaines
ne suffit pas. Distinguer utilité mathématique interne et application concrète.
Pour une modélisation, annoncer hypothèses, unités, données et limites ; ne pas
transformer une illustration pédagogique en affirmation scientifique non sourcée.

## 9. Exercices, corrigés et évaluation des acquis

Prévoir plusieurs fonctions d'exercices : diagnostic, automatismes, application
directe, choix d'une méthode, démonstration, critique d'un raisonnement, synthèse,
recherche et modélisation. Graduer les difficultés sans se limiter à reproduire
les exemples. Réutiliser régulièrement des notions plus anciennes.

Chaque exercice possède une correction identifiable. Les problèmes ouverts ont
une discussion des pistes, des résultats attendus ou des critères d'évaluation,
même lorsqu'il n'existe pas une réponse unique. Vérifier les données, la faisabilité,
la numérotation et les renvois. Ne pas fixer un quota artificiel d'exercices : leur
ensemble doit couvrir les compétences et les difficultés réelles.

Les corrigés expliquent la stratégie, les étapes, les conditions d'application,
les unités et les contrôles. Proposer plusieurs méthodes lorsqu'elles éclairent
une différence de point de vue. Prévoir des indices séparés lorsque cela aide à
chercher sans dévoiler immédiatement toute la solution.

Distinguer « reconnaître avec aide », « appliquer seul », « justifier » et
« transférer à un problème nouveau ». Les bilans de fin de chapitre et de niveau
doivent permettre cette appréciation. Une note ou un seuil ne suffit pas à
attester un niveau : documenter les compétences acquises et celles à reprendre.

## 10. Informatique, données et calcul numérique

Les programmes doivent être exécutables, expliqués et reliés aux mathématiques.
Préciser entrées, sorties, hypothèses, terminaison et limites. Utiliser les
simulations pour explorer et conjecturer, jamais comme substitut implicite à une
preuve. Distinguer calcul exact, arrondi, erreur d'approximation et incertitude.

Introduire progressivement invariants, complexité, stabilité et convergence.
Contrôler les algorithmes par des cas connus et des cas limites ; fixer une graine
quand la reproductibilité d'une simulation est nécessaire. Sourcer les données
réelles, conserver leur provenance et distinguer données fictives et observations.
Éviter les dépendances techniques sans bénéfice pédagogique.

## 11. Les quatre documents de chaque niveau

- **Guide** : public, périmètre, sources datées, diagnostic, prérequis, progression,
  table de couverture, registre des admissions, conseils de travail et bilans.
- **Cours** : explications, définitions, démonstrations, exemples et prolongements.
- **Exercices** : entraînement progressif et problèmes de synthèse, sans dévoiler
  les réponses au milieu des énoncés.
- **Corrigés** : solutions expliquées, indications de méthode et contrôles.

Conserver des numérotations et renvois compatibles entre ces documents. Utiliser
l'unique style commun ; ne pas en créer de variante par classe. Les chapitres
restent modulaires. Publier les quatre PDF ensemble pour un même tag, afin que
le lecteur utilise des versions cohérentes.

## 11 bis. Spécialité thématique : dossiers transversaux

En complément des volumes scolaires et universitaires, la collection propose des dossiers
thématiques approfondis, construits depuis les fondements et les démonstrations jusqu'aux
prolongements explicitement définis. Ne pas confondre cette catégorie avec l'enseignement
de « spécialité mathématiques » de première ou de terminale.

Chaque sujet a quatre maîtres (guide, cours, exercices, corrigés), des chapitres modulaires,
des objectifs, un diagnostic initial corrigé, une table de couverture et un registre des
admissions. Les résultats prouvés, les fondements admis et les approfondissements restent
distingués ; les prérequis renvoient aux volumes scolaires existants.

Les dossiers sont dans `sources/specialite/<theme>/` et déclarés dans `niveaux.json` sous
un identifiant unique comme `specialite-trigonometrie`. Leur publication suit les mêmes
règles : sources LaTeX versionnées, PDF produits en CI et publiés seulement sur release.

## 12. Processus de création et de révision

Pour un nouveau niveau : établir le périmètre et les sources, construire la table
de couverture, ordonner les dépendances, rédiger les quatre documents, contrôler
les mathématiques et les exercices, puis vérifier compilation et rendu.

Pour un cours existant : conserver ses acquis utiles, relever les écarts au
référentiel et aux textes applicables, corriger d'abord les erreurs mathématiques
et prérequis manquants, puis la couverture, les preuves, les explications et les
exercices. Élargir ensuite les prolongements. Éviter une réécriture purement
cosmétique lorsqu'une difficulté de fond demeure.

La PR doit préciser le périmètre audité, les corrections, les éléments encore
admis ou différés et les vérifications effectuées. L'adoption de ce fichier ne
certifie pas rétroactivement chaque page existante : l'audit est progressif et
traçable. Toute erreur identifiée doit être corrigée dans les sources, puis
publiée sous un nouveau tag ; ne pas remplacer silencieusement une release.

## 13. Grille avant validation d'un chapitre ou d'une révision

- [ ] Le public, le programme et le statut des compléments sont explicites.
- [ ] Les exigences concernées sont reliées à la table de couverture.
- [ ] Les prérequis sont accessibles et les dépendances sans circularité.
- [ ] Les objectifs sont observables et évalués par des exercices adaptés.
- [ ] Les termes et notations sont définis avant leur usage.
- [ ] Les résultats ont des hypothèses et un domaine de validité précis.
- [ ] Les preuves accessibles sont rédigées et leurs étapes justifiées.
- [ ] Les admissions et approximations sont signalées et suivies dans le guide.
- [ ] Les exemples, erreurs fréquentes et contre-exemples éclairent les difficultés.
- [ ] L'utilité actuelle et les réemplois futurs sont expliqués concrètement.
- [ ] Les énoncés sont cohérents, résolubles et associés à des corrigés vérifiés.
- [ ] Les raisonnements, calculs, unités et cas limites ont été relus.
- [ ] Les programmes et données ont les contrôles et sources nécessaires.
- [ ] Les quatre documents restent cohérents dans leurs renvois et numérotations.
- [ ] La compilation réussit sans référence non résolue ni débordement.
- [ ] Les figures, tableaux, sauts de page et pages modifiées ont été inspectés.
- [ ] Toute lacune restante est nommée ; aucune complétude non vérifiée n'est annoncée.

Une case non applicable doit être justifiée. La grille accompagne le jugement
pédagogique et la relecture mathématique ; elle ne les remplace pas.
