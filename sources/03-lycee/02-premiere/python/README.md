# Algorithmes de première

Python 3, bibliothèque standard uniquement.

~~~sh
python3 sources/03-lycee/02-premiere/python/outils.py
python3 sources/03-lycee/02-premiere/python/verifier.py
~~~

| Algorithmes | Chapitres | Justification mathématique |
| --- | --- | --- |
| Termes et sommes, seuils, Fibonacci, factorielle, Syracuse borné | 4–7, 24 | Invariants, formules, borne d'itérations |
| Taux d'accroissement | 8–9, 24 | Limite et contrôle sur un polynôme |
| Newton pour une racine carrée | 11, 29 | Monotonie, encadrement, identité d'erreur |
| Euler, approximation de e | 13, 26, 29 | Récurrence, erreur locale puis globale |
| Archimède et π | 14, 24 | Polygones inscrits/circonscrits, demi-corde |
| Lois finies, moments, moyennes à deux écarts types | 21–23 | Linéarité, variance, Tchebychev |
| Monte-Carlo pour une aire parabolique et π | 23 | Fréquences d'indicatrices |
| Marches aléatoires, fréquence de lettres | 20, 24 | Comptage et normalisation |

Les 18 vérifications portent sur des cas exacts, des contrats d'entrée, des
identités indépendantes, des erreurs et des simulations reproductibles. Elles
contrôlent les programmes ; les preuves générales restent dans le cours.

Les exemples aléatoires utilisent une graine explicite. Ils ne prétendent pas
certifier la qualité du générateur ni une probabilité de 95 % pour toutes les lois.
Les flottants ordinaires ne font pas d'arrondi dirigé : les encadrements de Newton
et d'Archimède sont des bornes mathématiques en arithmétique exacte, dont les
valeurs numériques peuvent être arrondies. Un calcul certifié demanderait une
arithmétique adaptée.

Les deux phrases de comparaison de lettres sont des exemples pédagogiques
originaux, pas des corpus représentatifs des langues. Les accents sont retirés,
œ devient oe, æ devient ae, et les caractères hors de a à z sont ignorés.
Les données des autres exemples sont fictives ; aucun téléchargement n'est requis.
