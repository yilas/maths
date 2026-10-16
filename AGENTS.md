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

- Construire une collection de la troisième à la terminale, exhaustive par
  rapport au programme et au parcours explicitement annoncés.
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

- Utiliser l'unique `mathscommun.sty` à la racine ; ne pas en dupliquer une copie
  par niveau. La présentation reste sobre et adaptée à l'impression.
- Maintenir des fichiers distincts pour le cours, les exercices, les corrigés et
  le guide ; conserver la correspondance de leur numérotation.
- Ajouter les nouveaux niveaux dans `NIVEAUX` de `compiler.py`.
- Compiler les documents modifiés avec `python3 compiler.py`. Après une modification
  du style ou du script commun, compiler tous les niveaux disponibles.
- Corriger les erreurs, références non résolues et débordements ; inspecter le
  rendu des pages modifiées, les figures, les tableaux et les sauts de page.
- Vérifier les calculs, la cohérence des énoncés et des corrigés, les unités et les
  conditions d'application des théorèmes.
- Actualiser les PDF dans `pdf/<niveau>/`. Ne pas versionner `build/`, les journaux
  et les fichiers auxiliaires de compilation.
