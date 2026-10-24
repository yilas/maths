# Algorithmes de terminale

Python 3, bibliothèque standard uniquement. Depuis ce dossier :

```sh
python3 verifier.py
```

Les **24 contrôles** portent sur des propriétés et des frontières : identité de
Pascal, encadrements rationnels, convergence et échecs numériques, moments
binomiaux, quantiles discrets, risque exact à la frontière du surbooking, Bézout,
RSA pour tous les messages du petit exemple, puissances matricielles et Markov.
Ils vérifient aussi les 216 identifiants d'exercices et leurs corrections, les
36 inclusions du cours et les huit synthèses. Ils sont exécutés automatiquement
par les contrôles de collection et la CI.

## Fonctions et liens avec le cours

| Fonctions | Chapitres | Contrat et idée |
| --- | --- | --- |
| `pascal` | 4 | Lignes 0 à n ; addition des parents, O(n²) coefficients |
| `permutations`, `combinaisons` | 3–4 | Énumération par positions ; taille de sortie factorielle ou binomiale |
| `permutation_aleatoire` | 3–4 | Fisher–Yates ; générateur fourni, n échanges au plus |
| `premier_seuil` | 10–11, 24 | Premier rang satisfaisant le prédicat, budget fini |
| `dichotomie` | 13, 24 | Encadrement de largeur au plus 2 epsilon ; continuité à vérifier mathématiquement |
| `newton`, `secante` | 13, 24 | Arrêt sur résidu ; contrôle du dénominateur et budget, sans garantie générale de convergence |
| `heron` | 11, S1 | Itérés depuis un point positif ; accepte des `Fraction` |
| `euler` | 18, 24 | Pas positif, n étapes ; stabilité à étudier selon l'équation |
| `quadrature` | 20 | Gauche, droite, milieu ou trapèzes ; n sous-intervalles |
| `briggs`, `brouncker` | 16, 20 | Approximation flottante par racines ; encadrement rationnel exact par somme alternée |
| `binomiale`, `quantile_binomial` | 21–22 | Loi complète calculée autour d'un mode, cumul et quantile discret |
| `surbooking` | S4 | Recherche bornée de la dernière capacité autorisée ; modèle indépendant |
| `galton`, `moyennes_bernoulli` | 21–23 | Historiques simulés reproductibles avec graine |
| `monte_carlo`, `pi_disque` | 24 | Estimateurs aléatoires ; erreur probabiliste, pas déterministe |
| `euclide_etendu`, `inverse_modulaire` | 29–30 | PGCD et identité de Bézout, entrées entières signées |
| `puissance_modulaire` | 31, S6 | Carrés successifs, O(log n) multiplications modulaires |
| `crible`, `factorisation` | 31 | Primalité jusqu'à une borne, décomposition exacte par divisions |
| `produit`, `puissance_matrice`, `markov` | 32–35 | Tailles contrôlées ; distribution ligne, coefficients exacts possibles |

## Essayer et interpréter

Depuis ce dossier, dans un interpréteur Python :

```python
from fractions import Fraction
from math import log
from algorithmes import dichotomie, heron, brouncker, binomiale, surbooking

gauche, droite = dichotomie(lambda x: x*x - 2, 1, 2, epsilon=1e-8)
print((gauche + droite)/2, "borne théorique :", (droite-gauche)/2)
u = heron(Fraction(2), Fraction(2), 3)[-1]
print(2/u, u)  # encadrement rationnel exact de sqrt(2)
a, b = brouncker(100)
print(float(a), log(2), float(b))
print(sum(binomiale(10, 0.5)[2:9]))
print(surbooking(100, 0.9, 0.05))  # 106, modèle fictif S4
```

La preuve d'un invariant explique pourquoi un algorithme mathématique fonctionne.
Un test vérifie seulement certaines exécutions de son implémentation. Une graine
fixe rend une simulation reproductible, sans la rendre exacte.

Les flottants peuvent perdre des chiffres (Briggs), arrondir une petite masse
binomiale à zéro ou épuiser une dichotomie. Les fonctions lèvent une exception
pour les principaux cas invalides et les budgets épuisés ; elles ne détectent pas
toutes les erreurs possibles du modèle ou des fonctions transmises.
Un petit résidu de Newton ne garantit une petite erreur sur la racine qu'avec
un contrôle supplémentaire, par exemple une minoration de la dérivée.
Les encadrements dits exacts le sont pour les calculs en `Fraction` indiqués ;
une comparaison flottante ne remplace pas l'arithmétique d'intervalles certifiée.

Fisher–Yates choisit uniformément une position parmi les i+1 positions restantes :
chaque permutation a probabilité 1/n! dans le modèle d'un générateur idéal.
Les listes énumérées deviennent rapidement volumineuses ; les fonctions sont
pédagogiques et ne prétendent pas traiter de très grands objets.
