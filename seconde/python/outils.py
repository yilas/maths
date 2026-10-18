"""Algorithmes du cours de seconde ; Python 3, bibliothèque standard seule.

Les nombres entiers et Fraction permettent des décisions exactes. Les fonctions
numériques à base de float retournent des approximations, jamais des preuves.
Les structures de listes et le CSV sont des supports de lecture facultatifs.
"""
import csv
from fractions import Fraction
from math import fsum, hypot, isfinite, sqrt
from pathlib import Path
from random import Random

DONNEES = Path(__file__).resolve().parents[1] / "donnees" / "population_cantons_2025.csv"


def entier(n, minimum=None):
    if type(n) is not int or (minimum is not None and n < minimum):
        raise ValueError("Entier hors du domaine attendu")
    return n


def est_multiple(b, a):
    entier(a)
    entier(b)
    if a == 0:
        raise ValueError("Diviseur non nul")
    return b % a == 0


def dernier_multiple(a, b):
    entier(a, 1)
    entier(b, 0)
    return a * (b // a)


def seuil_puissance(q, seuil):
    """Premier n >= 0 tel que q**n > seuil, pour q rationnel > 1.

    Employer Fraction(11, 10) ou '1.1', pas un float déjà arrondi.
    """
    if isinstance(q, float) or isinstance(seuil, float):
        raise ValueError("Utiliser des entiers, des chaînes ou Fraction")
    q, seuil = Fraction(q), Fraction(seuil)
    if q <= 1 or seuil < 1:
        raise ValueError("q > 1 et seuil >= 1")
    n, valeur = 0, Fraction(1)
    while valeur <= seuil:
        valeur *= q
        n += 1
    return n


def encadrer_racine2(decimales):
    """Balayage entier : retourne k, k+1, d avec k/d <= sqrt(2) < (k+1)/d."""
    entier(decimales, 0)
    d = 10 ** decimales
    k = d
    while (k + 1) ** 2 <= 2 * d * d:
        k += 1
    return k, k + 1, d


def dichotomie_racine2(iterations):
    """Encadrement rationnel exact ; largeur 2**(-iterations)."""
    entier(iterations, 0)
    a, b = Fraction(1), Fraction(2)
    for _ in range(iterations):
        m = (a + b) / 2
        if m * m < 2:
            a = m
        else:
            b = m
    return a, b


def determinant(u, v):
    return u[0] * v[1] - u[1] * v[0]


def alignes(A, B, C):
    """Exact pour des coordonnées entières ou Fraction.

    Si A=B, le déterminant est nul ; cela ne définit pas une droite AB.
    """
    return determinant((B[0] - A[0], B[1] - A[1]),
                       (C[0] - A[0], C[1] - A[1])) == 0


def equation_droite(A, B):
    """Coefficients (a,b,c) de ax+by+c=0 ; A et B doivent être distincts."""
    if A == B:
        raise ValueError("Deux points distincts sont nécessaires")
    ux, uy = B[0] - A[0], B[1] - A[1]
    return -uy, ux, uy * A[0] - ux * A[1]


def maximum_grille(f, a, b, n):
    """Maximum sur n+1 points d'une grille ; aucune garantie entre les points."""
    entier(n, 1)
    if not (isfinite(a) and isfinite(b) and a < b):
        raise ValueError("Bornes finies et ordonnées")
    points = [(a + (b-a)*k/n, None) for k in range(n+1)]
    valeurs = [(x, f(x)) for x, _ in points]
    if not all(isfinite(y) for _, y in valeurs):
        raise ValueError("Images finies requises")
    return max(valeurs, key=lambda couple: couple[1])


def longueur_polygonale(f, a, b, n):
    """Somme des distances entre points consécutifs ; résultat flottant."""
    entier(n, 1)
    if not (isfinite(a) and isfinite(b) and a < b):
        raise ValueError("Bornes finies et ordonnées")
    x, y = a, f(a)
    if not isfinite(y):
        raise ValueError("Images finies requises")
    segments = []
    for k in range(1, n + 1):
        suivant = a + (b-a)*k/n
        image = f(suivant)
        if not isfinite(image):
            raise ValueError("Images finies requises")
        segments.append(hypot(suivant-x, image-y))
        x, y = suivant, image
    return fsum(segments)


def moyenne_ecart_type(valeurs):
    """Statistique descriptive, dénominateur N (et non N-1)."""
    valeurs = list(valeurs)
    if not valeurs or not all(isfinite(x) for x in valeurs):
        raise ValueError("Série non vide de nombres finis")
    n = len(valeurs)
    m = fsum(valeurs) / n
    v = fsum((x-m)**2 for x in valeurs) / n
    return m, sqrt(v)


def experience(p, generateur):
    if not isfinite(p) or not 0 <= p <= 1:
        raise ValueError("Probabilité comprise entre 0 et 1")
    return int(generateur.random() < p)


def frequence(p, n, graine=None):
    entier(n, 1)
    if not isfinite(p) or not 0 <= p <= 1:
        raise ValueError("Probabilité comprise entre 0 et 1")
    generateur = Random(graine)
    return sum(experience(p, generateur) for _ in range(n)) / n


def tableau_croise(premier, second):
    """Deux listes de modalités sur les mêmes individus, dans le même ordre."""
    if len(premier) != len(second):
        raise ValueError("Les deux listes doivent décrire les mêmes individus")
    tableau = {}
    for a, b in zip(premier, second):
        tableau[a, b] = tableau.get((a, b), 0) + 1
    return tableau


def compter_filtre(individus, predicat):
    """Le prédicat peut combiner and, or et not."""
    return sum(1 for individu in individus if predicat(individu))


def lire_cantons(chemin=DONNEES):
    """Le CSV contient des agrégats cantonaux, pas des individus."""
    with Path(chemin).open(encoding="utf-8", newline="") as fichier:
        lecteur = csv.DictReader(fichier)
        if lecteur.fieldnames != ["canton", "femmes", "hommes"]:
            raise ValueError("Colonnes inattendues")
        lignes, vus = [], set()
        for ligne in lecteur:
            canton = ligne["canton"]
            if not canton or canton in vus:
                raise ValueError("Canton absent ou répété")
            femmes, hommes = int(ligne["femmes"]), int(ligne["hommes"])
            if femmes < 0 or hommes < 0:
                raise ValueError("Effectif négatif")
            lignes.append((canton, femmes, hommes))
            vus.add(canton)
    if not lignes:
        raise ValueError("Fichier vide")
    return lignes


def esch_autres(lignes):
    tableau = {"Esch-sur-Alzette": [0, 0], "Autres cantons": [0, 0]}
    for canton, femmes, hommes in lignes:
        groupe = "Esch-sur-Alzette" if canton == "Esch-sur-Alzette" else "Autres cantons"
        tableau[groupe][0] += femmes
        tableau[groupe][1] += hommes
    return tableau


if __name__ == "__main__":
    print("Encadrement de sqrt(2) au millième :", encadrer_racine2(3))
    print("Premier n tel que (11/10)^n > 2 :", seuil_puissance(Fraction(11, 10), 2))
    print("Moyenne et écart-type :", moyenne_ecart_type([1, 2, 2, 4, 5, 8, 8, 10]))
    print("Tableau réel femmes / hommes :", esch_autres(lire_cantons()))
