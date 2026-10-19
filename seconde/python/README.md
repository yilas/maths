# Algorithmes de seconde

Depuis la racine :

```sh
python3 seconde/python/outils.py
python3 seconde/python/verifier.py
```

Python 3 et sa bibliothèque standard suffisent. Le second script lance dix
vérifications : cas limites, seuil strict, encadrements rationnels, droites
verticales, maximum sur une grille, longueur polygonale, statistiques,
simulation reproductible, filtres et marges de données réelles.

Les fonctions exactes utilisent les entiers ou `fractions.Fraction`.
Un balayage décimal demande un nombre de pas proportionnel à 10 puissance la
précision : choisir quelques décimales pour cet exercice, puis comparer à la
dichotomie. Les fonctions numériques à flottants rendent des approximations.

Les tests ne remplacent pas les preuves du cours. Ils contrôlent que les
programmes réalisent les calculs et respectent les cas limites annoncés.
Les listes, dictionnaires et fichiers CSV servent de supports de lecture ;
leur maîtrise générale n'est pas un attendu de seconde.
