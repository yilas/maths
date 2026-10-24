# Première générale — spécialité mathématiques

Programme applicable à partir de la rentrée **2026–2027**, arrêté du 26 février
2026, BO n° 14 du 2 avril 2026, NOR MENE2602917A.
[Texte officiel et annexe](https://www.education.gouv.fr/bo/2026/Hebdo14/MENE2602917A).
Référence vérifiée le 23 octobre 2026.

Le périmètre concerne la spécialité de la voie générale, pas l'enseignement
commun hors spécialité ni les séries technologiques. L'objectif à long terme
est un niveau master, construit progressivement par la terminale et la licence.

**30 chapitres, 180 exercices corrigés, huit problèmes de synthèse corrigés,
80 automatismes avec réponses et 18 vérifications des algorithmes Python.**
Les quatre PDF sont dans [releases GitHub](https://github.com/yilas/maths/releases).

| Document | Source | PDF |
| --- | --- | --- |
| Cours et démonstrations | [cours_1re.tex](cours_1re.tex) | [Cours](https://github.com/yilas/maths/releases/latest/download/premiere-cours.pdf) |
| Exercices et problèmes | [exercices_1re.tex](exercices_1re.tex) | [Exercices](https://github.com/yilas/maths/releases/latest/download/premiere-exercices.pdf) |
| Corrigés expliqués | [corriges_1re.tex](corriges_1re.tex) | [Corrigés](https://github.com/yilas/maths/releases/latest/download/premiere-corriges.pdf) |
| Guide, couverture et révisions | [guide_1re.tex](guide_1re.tex) | [Guide](https://github.com/yilas/maths/releases/latest/download/premiere-guide.pdf) |

## Chapitres

Les chapitres 1–14 et 16–24 couvrent les thèmes officiels et contiennent des
approfondissements signalés. Le chapitre 15 et les chapitres 25–30 sont des
compléments hors programme, conçus pour être relus après la terminale.

| N° | Chapitre |
| --- | --- |
| 1 | [Raisonner, définir et démontrer](chapitres/01_raisonnement.tex) |
| 2 | [Calcul algébrique et polynômes](chapitres/02_polynomes.tex) |
| 3 | [Le second degré dans toutes ses formes](chapitres/03_second_degre.tex) |
| 4 | [Construire et représenter une suite](chapitres/04_suites.tex) |
| 5 | [Suites arithmétiques, géométriques et sommes](chapitres/05_suites_sommes.tex) |
| 6 | [Modèles discrets et suites affines](chapitres/06_modeles_discrets.tex) |
| 7 | [Variations et limites de suites](chapitres/07_limites_suites.tex) |
| 8 | [Nombre dérivé, tangente et approximation](chapitres/08_nombre_derive.tex) |
| 9 | [Calculer et justifier les dérivées](chapitres/09_calcul_differentiel.tex) |
| 10 | [Dérivées, variations et extrémums](chapitres/10_variations.tex) |
| 11 | [Optimiser, comparer et approcher](chapitres/11_optimisation.tex) |
| 12 | [La fonction exponentielle](chapitres/12_exponentielle.tex) |
| 13 | [Modèles continus et méthode d'Euler](chapitres/13_modeles_continus.tex) |
| 14 | [Radian et cercle trigonométrique](chapitres/14_cercle.tex) |
| 15 | [Identités et fonctions trigonométriques](chapitres/15_trigonometrie.tex) |
| 16 | [Produit scalaire et orthogonalité](chapitres/16_produit_scalaire.tex) |
| 17 | [Longueurs, angles et lieux géométriques](chapitres/17_geometrie.tex) |
| 18 | [Droites, projections et cercles](chapitres/18_droites_cercles.tex) |
| 19 | [Conditionnement, indépendance et Bayes](chapitres/19_conditionnement.tex) |
| 20 | [Épreuves répétées et dénombrement](chapitres/20_bernoulli.tex) |
| 21 | [Variables aléatoires et espérance](chapitres/21_variables_aleatoires.tex) |
| 22 | [Variance, covariance et erreur quadratique](chapitres/22_variance.tex) |
| 23 | [Échantillonnage et simulation](chapitres/23_echantillonnage.tex) |
| 24 | [Algorithmique, listes et calcul fiable](chapitres/24_python.tex) |
| 25 | [Complément : fonder les outils d'analyse](chapitres/25_fondements_analyse.tex) |
| 26 | [Complément : construire exponentielle et logarithme](chapitres/26_construire_exp.tex) |
| 27 | [Complément : espaces vectoriels et projections](chapitres/27_algebre_lineaire.tex) |
| 28 | [Complément : la géométrie des probabilités](chapitres/28_probabilites_geometrie.tex) |
| 29 | [Complément : convergence des algorithmes](chapitres/29_convergence_algorithmes.tex) |
| 30 | [Relier les outils et construire le parcours vers le master](chapitres/30_vers_master.tex) |

## Couverture et démonstrations

Le guide associe chaque groupe de contenus, capacités et algorithmes officiels
aux chapitres correspondants. Il répertorie séparément les démonstrations
identifiées dans le programme, les fondements admis et les dépendances.
Les automatismes entretiennent aussi les pourcentages, statistiques, graphiques
et probabilités conditionnelles acquis en seconde.

Le cours démontre notamment les formules des suites et du second degré, les règles
de dérivation, Fermat/Rolle/accroissements finis, les propriétés de l'exponentielle,
Al-Kashi, les lieux géométriques, la linéarité de l'espérance et König–Huygens.
Les compléments construisent l'exponentielle par séries, l'intégrale des fonctions
continues, le logarithme, les projections et les moindres carrés, l'espérance
conditionnelle finie, la concentration et la convergence des algorithmes.

La complétude des réels et les fondements algébriques et géométriques restent
explicitement admis. Une définition, une preuve, une illustration et une
simulation sont distinguées. Les programmes ne prétendent pas résoudre la
conjecture de Syracuse ni fournir des encadrements flottants par arrondi dirigé.

Chaque chapitre explique des réemplois concrets jusqu'au supérieur. Ces premiers
ponts ne constituent pas une équivalence avec une formation universitaire.

## Compilation et calcul

~~~sh
python3 compiler.py --niveau premiere
python3 compiler.py --niveau premiere --chapitre 16
python3 sources/03-lycee/02-premiere/python/verifier.py
python3 sources/03-lycee/02-premiere/python/outils.py
~~~

Le fichier de style est l'unique [mathscommun.sty](../../../commun/mathscommun.sty).
[Algorithmes et conventions numériques](python/README.md).
