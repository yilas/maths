# Consignes de travail

## Livraison

- Toute modification du contenu, du style ou des outils est proposée dans une
  branche et une pull request vers `main`.
- Ne pas fusionner une PR sans demande explicite de l'utilisateur.
- Conserver les ajouts par niveau ou par ensemble cohérent, avec un titre et une
  description en français précisant le périmètre et les vérifications.
- L'initialisation technique du dépôt vide est terminée ; les contributions
  suivantes passent toutes par PR.

## Objectif pédagogique

- Lire `OBJECTIFS.md` avant toute création ou révision pédagogique ; appliquer sa grille de contrôle.

- Construire une collection du primaire au master, exhaustive par
  rapport au programme et au parcours explicitement annoncés.
- L'objectif final est un niveau master de mathématiques, construit progressivement
  après la terminale par des volumes de licence puis de master.
  Renforcer progressivement la précision des définitions, la rédaction de preuves,
  les contre-exemples et l'autonomie ; signaler clairement les compléments hors programme.
- Expliquer dans chaque chapitre l'utilité présente des outils et leur réemploi
  ultérieur, avec des exemples précis et des dépendances explicites. Ne pas confondre
  une introduction à un objet avancé avec sa maîtrise au niveau universitaire.
- Vérifier les textes officiels applicables avant de rédiger un nouveau niveau.
  Recenser toutes les notions dans une table de couverture avec leurs chapitres.
- Écrire comme un professeur pédagogue : objectifs, prérequis, définitions
  précises, exemples résolus, méthodes, erreurs fréquentes et exercices corrigés.
- Démontrer autant que possible chaque propriété, formule et résultat géométrique.
  Donner les hypothèses et les étapes du raisonnement. Une figure ou une simulation
  n'est pas une preuve générale.
- Distinguer les définitions, les résultats démontrés, les fondements admis et les
  approfondissements. Expliquer les limites d'une justification au niveau étudié.
- Ne pas annoncer un niveau comme complet tant que sa table de couverture n'a pas
  été vérifiée. Ne pas présenter un modèle ou un plan comme un cours rédigé.

## Structure et vérification

- Utiliser l'unique `commun/mathscommun.sty` ; ne pas en dupliquer une copie
  par niveau. La présentation reste sobre et adaptée à l'impression.
- Maintenir des fichiers distincts pour le cours, les exercices, les corrigés et
  le guide ; conserver la correspondance de leur numérotation.
- Ajouter les nouveaux niveaux dans `niveaux.json` (chemin et suffixe des quatre maîtres).
- Compiler les documents modifiés avec `python3 compiler.py`. Après une modification
  du style ou du script commun, compiler tous les niveaux disponibles.
- Corriger les erreurs, références non résolues et débordements ; inspecter le
  rendu des pages modifiées, les figures, les tableaux et les sauts de page.
- Vérifier les calculs, la cohérence des énoncés et des corrigés, les unités et les
  conditions d'application des théorèmes.
- Ne jamais versionner les PDF : les générer dans `build/pdf/<niveau>/`, puis les publier
  par le workflow de release sur tag. Ne pas versionner `build/`, les journaux
  et les fichiers auxiliaires. Vérifier aussi le conditionnement de tous les niveaux.
