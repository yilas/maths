"""Algorithmes de première, bibliothèque standard uniquement.

Les bornes mathématiques sont démontrées en arithmétique exacte. Les valeurs
flottantes ne sont pas des certifications par arrondi dirigé.
"""
import math
import random
import unicodedata


def entier(n, minimum=0):
    if type(n) is not int or n < minimum:
        raise ValueError(f"entier supérieur ou égal à {minimum} attendu")


def reel_fini(x):
    if not isinstance(x, (int, float)) or isinstance(x, bool) or not math.isfinite(x):
        raise ValueError("réel fini attendu")


def factorielle(n):
    entier(n)
    produit = 1
    for k in range(1, n + 1):
        produit *= k
    return produit


def fibonacci(n):
    """Liste F_0,...,F_n, calculée en entiers exacts."""
    entier(n)
    a, b = 0, 1
    termes = []
    for _ in range(n + 1):
        termes.append(a)
        a, b = b, a + b
    return termes


def termes_affines(a, b, u0, n):
    """u_0,...,u_n pour u_(k+1)=a*u_k+b."""
    entier(n)
    for x in (a, b, u0):
        reel_fini(x)
    termes = [u0]
    for _ in range(n):
        termes.append(a * termes[-1] + b)
    return termes


def sommes_cumulees(termes):
    total = 0
    sommes = []
    for valeur in termes:
        total += valeur
        sommes.append(total)
    return sommes


def premier_seuil(f, u0, seuil, max_etapes=10000):
    """Premier n avec u_n >= seuil ; erreur si la borne ne permet pas de conclure."""
    entier(max_etapes)
    reel_fini(u0)
    reel_fini(seuil)
    u = u0
    for n in range(max_etapes + 1):
        if u >= seuil:
            return n, u
        if n < max_etapes:
            u = f(u)
            reel_fini(u)
    raise RuntimeError("borne atteinte : aucune conclusion au-delà")


def syracuse(u0, max_etapes=10000):
    """(trajectoire, arrivee_a_1), sans supposer la conjecture."""
    entier(u0, 1)
    entier(max_etapes)
    termes = [u0]
    for _ in range(max_etapes):
        u = termes[-1]
        if u == 1:
            break
        termes.append(u // 2 if u % 2 == 0 else 3 * u + 1)
    return termes, termes[-1] == 1


def taux_accroissement(f, a, pas):
    reel_fini(a)
    valeurs = []
    for h in pas:
        reel_fini(h)
        if h == 0:
            raise ValueError("un taux exige un pas non nul")
        valeurs.append((f(a + h) - f(a)) / h)
    return valeurs


def euler(f, t0, y0, fin, n):
    """Listes des n+1 temps et valeurs pour y'=f(t,y), pas constant positif."""
    entier(n, 1)
    for x in (t0, y0, fin):
        reel_fini(x)
    if fin <= t0:
        raise ValueError("la fin doit suivre le temps initial")
    h = (fin - t0) / n
    temps, valeurs = [t0], [y0]
    for k in range(n):
        valeurs.append(valeurs[-1] + h * f(t0 + k * h, valeurs[-1]))
        temps.append(t0 + (k + 1) * h)
    return temps, valeurs


def newton_racine(a, tolerance=1e-10, max_etapes=100):
    """Approche sqrt(a) ; la tolérance porte sur la largeur des bornes a/u et u.

    Les flottants peuvent arrondir les bornes. Une stagnation avant la précision
    demandée est signalée. Aucune certification par arrondi dirigé n'est revendiquée.
    """
    reel_fini(a)
    reel_fini(tolerance)
    entier(max_etapes, 1)
    if a <= 0 or tolerance <= 0:
        raise ValueError("a et tolérance strictement positifs attendus")
    u = max(1.0, a)
    termes = [u]
    for _ in range(max_etapes):
        bas, haut = sorted((a / u, u))
        if haut - bas <= tolerance:
            return bas, haut, termes
        suivant = (u + a / u) / 2
        if suivant == u:
            raise ArithmeticError("stagnation flottante avant la tolérance")
        u = suivant
        termes.append(u)
    raise RuntimeError("Newton : nombre maximal d'étapes atteint")


def archimede(doublements):
    """(nombre de côtés, borne inférieure, borne supérieure) à chaque étape."""
    entier(doublements)
    n, s = 6, 1.0
    lignes = []
    for k in range(doublements + 1):
        bas = n * s / 2
        haut = bas / math.sqrt(1 - s * s / 4)
        lignes.append((n, bas, haut))
        if k < doublements:
            s = s / math.sqrt(2 + math.sqrt(4 - s * s))
            n *= 2
    return lignes


def verifier_loi(valeurs, probabilites):
    if len(valeurs) == 0 or len(valeurs) != len(probabilites):
        raise ValueError("deux listes non vides de même longueur attendues")
    for x in valeurs:
        reel_fini(x)
    # Le noyau pédagogique travaille avec des listes, sans dictionnaire.
    if any(x in valeurs[:i] for i, x in enumerate(valeurs)):
        raise ValueError("les valeurs de la loi doivent être distinctes")
    for p in probabilites:
        reel_fini(p)
        if p < 0:
            raise ValueError("probabilité négative")
    if not math.isclose(math.fsum(probabilites), 1, rel_tol=0, abs_tol=1e-12):
        raise ValueError("les probabilités doivent sommer à 1")


def moments(valeurs, probabilites):
    """Moyenne, variance centrée et écart type d'une loi finie."""
    verifier_loi(valeurs, probabilites)
    mu = math.fsum(x * p for x, p in zip(valeurs, probabilites))
    variance = math.fsum(p * (x - mu) ** 2 for x, p in zip(valeurs, probabilites))
    return mu, variance, math.sqrt(variance)


def tirer(valeurs, probabilites, rng):
    """Tirage par cumuls ; rng est un random.Random explicite."""
    verifier_loi(valeurs, probabilites)
    u, cumul = rng.random(), 0.0
    dernier_possible = valeurs[0]
    for x, p in zip(valeurs, probabilites):
        if p > 0:
            dernier_possible = x
        cumul += p
        if u < cumul:
            return x
    # La somme flottante peut être légèrement inférieure à 1.
    return dernier_possible


def experience_moyennes(valeurs, probabilites, n, repetitions, graine=2026):
    """Les N moyennes et la proportion dans mu +/- 2 sigma/sqrt(n)."""
    entier(n, 1)
    entier(repetitions, 1)
    mu, _, sigma = moments(valeurs, probabilites)
    rng = random.Random(graine)
    moyennes = []
    for _ in range(repetitions):
        echantillon = [tirer(valeurs, probabilites, rng) for _ in range(n)]
        moyennes.append(math.fsum(echantillon) / n)
    proportion = (1.0 if sigma == 0 else
                  sum(abs(m - mu) <= 2 * sigma / math.sqrt(n) for m in moyennes)
                  / repetitions)
    return moyennes, proportion


def monte_carlo(n, graine=2026):
    """Aire sous x^2 sur [0,1] et pi, estimés avec les mêmes points."""
    entier(n, 1)
    rng = random.Random(graine)
    sous_parabole = dans_disque = 0
    for _ in range(n):
        u, v = rng.random(), rng.random()
        sous_parabole += v <= u * u
        dans_disque += u * u + v * v <= 1
    return sous_parabole / n, 4 * dans_disque / n


def marche_aleatoire(n, p=0.5, graine=2026):
    entier(n)
    reel_fini(p)
    if not 0 <= p <= 1:
        raise ValueError("p doit appartenir à [0,1]")
    rng = random.Random(graine)
    positions = [0]
    for _ in range(n):
        positions.append(positions[-1] + (1 if rng.random() < p else -1))
    return positions


def frequences_lettres(texte):
    """26 fréquences, accents retirés, œ->oe et æ->ae ; autres signes ignorés."""
    texte = texte.lower().replace("œ", "oe").replace("æ", "ae")
    texte = unicodedata.normalize("NFKD", texte)
    comptes = [0] * 26
    for caractere in texte:
        if "a" <= caractere <= "z":
            comptes[ord(caractere) - ord("a")] += 1
    total = sum(comptes)
    if total == 0:
        raise ValueError("aucune lettre retenue")
    return [c / total for c in comptes]


def demonstration():
    print("Fibonacci :", fibonacci(10))
    print("Seuil 140 :", premier_seuil(lambda u: 0.8 * u + 30, 50, 140))
    bas, haut, _ = newton_racine(2)
    print("Newton sqrt(2), bornes flottantes :", bas, haut)
    for n in (10, 100, 1000):
        _, y = euler(lambda t, y: y, 0, 1, 1, n)
        print("Euler n =", n, "valeur =", y[-1], "erreur =", math.e - y[-1])
    print("Archimède :", archimede(8)[-1])
    _, proportion = experience_moyennes([0, 1], [0.7, 0.3], 100, 2000)
    print("Bernoulli p=.3, n=100, N=2000, graine=2026 :", proportion)
    print("Monte-Carlo n=100000, graine=2026 :", monte_carlo(100000))
    textes = [
        "Les nombres et les figures nous aident à comprendre le monde.",
        "Numbers and shapes help us understand the world.",
    ]
    for texte in textes:
        frequences = frequences_lettres(texte)
        print("Phrase pédagogique :", texte)
        print("Fréquence de e :", frequences[ord("e") - ord("a")])


if __name__ == "__main__":
    demonstration()
