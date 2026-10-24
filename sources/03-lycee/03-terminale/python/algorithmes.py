"""Algorithmes de terminale, sans dépendance externe.

Les listes de permutations/combinaisons portent sur les positions : fournir des
valeurs distinctes pour obtenir des résultats distincts. Les méthodes numériques
ont un budget fini ; une exception signale un échec, jamais une preuve de convergence.
"""
from fractions import Fraction
from math import isfinite, isqrt, sqrt
from random import Random


def entier(n, minimum=0):
    if isinstance(n, bool) or not isinstance(n, int) or n < minimum:
        raise ValueError(f"entier >= {minimum} requis")


def positif(x):
    if not isfinite(x) or x <= 0:
        raise ValueError("réel fini strictement positif requis")


def pascal(n):
    """Lignes 0 à n incluses ; addition des deux parents, calcul entier exact."""
    entier(n)
    lignes = [[1]]
    for _ in range(n):
        p = lignes[-1]
        lignes.append([1] + [p[k-1] + p[k] for k in range(1, len(p))] + [1])
    return lignes


def permutations(valeurs):
    """Toutes les permutations ; coût au moins factoriel (taille de la sortie)."""
    valeurs = list(valeurs)
    if not valeurs:
        return [[]]
    return [[v] + reste for i, v in enumerate(valeurs)
            for reste in permutations(valeurs[:i] + valeurs[i+1:])]


def combinaisons(valeurs, k):
    """Sous-listes de k positions dans l'ordre initial ; notamment k=2 ou 3."""
    entier(k)
    valeurs = list(valeurs)
    if k == 0:
        return [[]]
    if k > len(valeurs):
        return []
    return [[valeurs[i]] + r for i in range(len(valeurs)-k+1)
            for r in combinaisons(valeurs[i+1:], k-1)]


def permutation_aleatoire(valeurs, rng):
    """Fisher–Yates ; rng est un random.Random fourni par l'appelant."""
    resultat = list(valeurs)
    for i in range(len(resultat)-1, 0, -1):
        j = rng.randrange(i+1)
        resultat[i], resultat[j] = resultat[j], resultat[i]
    return resultat


def premier_seuil(u0, suivant, condition, max_etapes=10000):
    """Premier (n,u_n) vérifiant condition, y compris n=0, sinon RuntimeError."""
    entier(max_etapes)
    u = u0
    for n in range(max_etapes+1):
        if condition(u):
            return n, u
        if n < max_etapes:
            u = suivant(u)
    raise RuntimeError("seuil non atteint dans le budget autorisé")


def dichotomie(f, a, b, epsilon=1e-8, max_etapes=1000):
    """(gauche,droite), largeur <= 2 epsilon ; f continue est une hypothèse.

    L'encadrement est mathématique en arithmétique exacte. En flottants, contrôler
    aussi l'évaluation de f ; une valeur arrondie à zéro n'est pas un certificat.
    """
    positif(epsilon)
    entier(max_etapes, 1)
    if not isfinite(a) or not isfinite(b) or a >= b:
        raise ValueError("bornes finies a < b requises")
    fa, fb = f(a), f(b)
    if not isfinite(fa) or not isfinite(fb):
        raise ValueError("valeurs finies requises")
    if fa == 0:
        return a, a
    if fb == 0:
        return b, b
    if (fa > 0) == (fb > 0):
        raise ValueError("signes opposés requis")
    for _ in range(max_etapes):
        if b-a <= 2*epsilon:
            return a, b
        m = a + (b-a)/2
        if m == a or m == b:
            raise RuntimeError("précision flottante épuisée")
        fm = f(m)
        if not isfinite(fm):
            raise ValueError("évaluation non finie")
        if fm == 0:
            return m, m
        if (fa > 0) == (fm > 0):
            a, fa = m, fm
        else:
            b = m
    raise RuntimeError("budget de dichotomie épuisé")


def newton(f, derivee, x0, epsilon=1e-10, max_etapes=100):
    """Arrêt sur résidu <= epsilon ; cela ne certifie PAS l'erreur sur x."""
    positif(epsilon)
    entier(max_etapes, 1)
    x = x0
    for _ in range(max_etapes):
        fx = f(x)
        if not isfinite(fx):
            raise ValueError("évaluation non finie")
        if abs(fx) <= epsilon:
            return x
        d = derivee(x)
        if not isfinite(d) or d == 0:
            raise ValueError("dérivée nulle ou non finie")
        x = x - fx/d
        if not isfinite(x):
            raise ValueError("itéré non fini")
    raise RuntimeError("Newton n'a pas satisfait le critère de résidu")


def secante(f, x0, x1, epsilon=1e-10, max_etapes=100):
    """Même réserve que Newton sur l'arrêt fondé sur le résidu."""
    positif(epsilon)
    entier(max_etapes, 1)
    a, b = x0, x1
    fa = f(a)
    for _ in range(max_etapes):
        fb = f(b)
        if not isfinite(fa) or not isfinite(fb):
            raise ValueError("évaluation non finie")
        if abs(fb) <= epsilon:
            return b
        if fb == fa:
            raise ValueError("pente de sécante nulle")
        a, b, fa = b, b-fb*(b-a)/(fb-fa), fb
        if not isfinite(b):
            raise ValueError("itéré non fini")
    raise RuntimeError("sécante : budget épuisé")


def heron(a, u0, etapes):
    """Renvoie tous les itérés ; Fraction permet un calcul rationnel exact."""
    positif(a)
    positif(u0)
    entier(etapes)
    valeurs = [u0]
    for _ in range(etapes):
        u = valeurs[-1]
        valeurs.append((u+a/u)/2)
    return valeurs


def euler(f, t0, y0, h, n):
    """n pas positifs pour y'=f(t,y), sortie [(temps,valeur), ...]."""
    positif(h)
    entier(n)
    t, y = t0, y0
    valeurs = [(t, y)]
    for k in range(n):
        y = y + h*f(t, y)
        t = t0+(k+1)*h
        if not isfinite(y) or not isfinite(t):
            raise ValueError("itéré non fini")
        valeurs.append((t, y))
    return valeurs


def quadrature(f, a, b, n, methode='milieu'):
    """Somme de rectangles gauche/droite, milieux ou trapèzes (a <= b)."""
    entier(n, 1)
    if not isfinite(a) or not isfinite(b) or a > b:
        raise ValueError("bornes finies ordonnées requises")
    if methode not in ('gauche', 'droite', 'milieu', 'trapezes'):
        raise ValueError("méthode inconnue")
    h = (b-a)/n
    if methode == 'trapezes':
        return h*((f(a)+f(b))/2 + sum(f(a+k*h) for k in range(1, n)))
    decalage = {'gauche': 0, 'droite': 1, 'milieu': 0.5}[methode]
    return h*sum(f(a+(k+decalage)*h) for k in range(n))


def briggs(x, racines=15):
    """2**k (x**(1/2**k)-1) ; trop de racines perdent des chiffres."""
    positif(x)
    entier(racines)
    r = x
    for _ in range(racines):
        r = sqrt(r)
    return 2**racines*(r-1)


def brouncker(n):
    """Encadrement EXACT de ln(2) par sommes alternées S_2n et S_(2n+1)."""
    entier(n, 1)
    bas = sum((Fraction(1, (2*j-1)*2*j) for j in range(1, n+1)), Fraction(0))
    return bas, bas+Fraction(1, 2*n+1)


def probabilite(p):
    if not isfinite(p) or not 0 <= p <= 1:
        raise ValueError("probabilité dans [0,1] requise")


def binomiale(n, p):
    """Loi complète en flottants, calculée autour d'un mode puis normalisée.

    Évite de commencer par (1-p)**n, qui peut sous-déborder. Les très petites
    probabilités restent limitées par la précision des flottants.
    """
    entier(n)
    probabilite(p)
    loi = [0.0]*(n+1)
    if p == 0 or p == 1:
        loi[0 if p == 0 else n] = 1.0
        return loi
    m = min(n, int((n+1)*p))
    loi[m] = 1.0
    for k in range(m, 0, -1):
        loi[k-1] = loi[k]*k/(n-k+1)*(1-p)/p
    for k in range(m, n):
        loi[k+1] = loi[k]*(n-k)/(k+1)*p/(1-p)
    total = sum(loi)
    return [x/total for x in loi]


def quantile_binomial(n, p, niveau):
    """Plus petit k dans [0,n] avec P(X<=k)>=niveau ; convention k=0 si niveau=0."""
    probabilite(niveau)
    loi = binomiale(n, p)
    cumul = 0
    for k, masse in enumerate(loi):
        cumul += masse
        if cumul >= niveau:
            return k
    return n  # cumul peut être arrondi légèrement sous 1


def surbooking(places, p, risque, max_inscrits=10000):
    """Plus grand n autorisé par le risque P(B(n,p)>places), recherche bornée."""
    entier(places)
    entier(max_inscrits, places+1)
    probabilite(p)
    probabilite(risque)
    if p == 0 or risque == 1:
        raise ValueError("pas de maximum fini dans ce cas")
    for n in range(places+1, max_inscrits+1):
        if sum(binomiale(n, p)[places+1:]) > risque:
            return n-1
    raise RuntimeError("budget insuffisant pour trouver la frontière")


def galton(etages, billes, p=0.5, graine=0):
    """Histogramme simulé de sommes de Bernoulli indépendantes."""
    entier(etages)
    entier(billes)
    probabilite(p)
    rng = Random(graine)
    effectifs = [0]*(etages+1)
    for _ in range(billes):
        effectifs[sum(rng.random() < p for _ in range(etages))] += 1
    return effectifs


def moyennes_bernoulli(n, repetitions, p, graine=0):
    entier(n, 1)
    entier(repetitions)
    probabilite(p)
    rng = Random(graine)
    return [sum(rng.random() < p for _ in range(n))/n for _ in range(repetitions)]


def monte_carlo(f, a, b, n, graine=0):
    """Estimateur d'intégrale ; ne fournit pas de borne déterministe d'erreur."""
    entier(n, 1)
    if not isfinite(a) or not isfinite(b) or a > b:
        raise ValueError("bornes finies ordonnées requises")
    rng = Random(graine)
    return (b-a)*sum(f(rng.uniform(a, b)) for _ in range(n))/n


def pi_disque(n, graine=0):
    entier(n, 1)
    rng = Random(graine)
    succes = sum(rng.random()**2+rng.random()**2 <= 1 for _ in range(n))
    return 4*succes/n


def euclide_etendu(a, b):
    """(d,u,v), d>=0, a*u+b*v=d=pgcd(a,b), y compris entrées signées."""
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (a, b)):
        raise ValueError("entiers requis")
    r0, r1, u0, u1, v0, v1 = abs(a), abs(b), 1, 0, 0, 1
    while r1:
        q = r0//r1
        r0, r1 = r1, r0-q*r1
        u0, u1 = u1, u0-q*u1
        v0, v1 = v1, v0-q*v1
    return r0, u0 if a >= 0 else -u0, v0 if b >= 0 else -v0


def inverse_modulaire(a, module):
    entier(module, 2)
    d, u, _ = euclide_etendu(a, module)
    if d != 1:
        raise ValueError("inverse inexistant : pgcd différent de 1")
    return u % module


def puissance_modulaire(a, n, module):
    entier(n)
    entier(module, 1)
    if isinstance(a, bool) or not isinstance(a, int):
        raise ValueError("base entière requise")
    resultat, base = 1 % module, a % module
    while n:
        if n % 2:
            resultat = resultat*base % module
        base = base*base % module
        n //= 2
    return resultat


def crible(n):
    """Nombres premiers <= n ; élimination à partir de p**2."""
    entier(n)
    marque = [True]*(n+1)
    for p in range(2, isqrt(n)+1):
        if marque[p]:
            for k in range(p*p, n+1, p):
                marque[k] = False
    return [p for p in range(2, n+1) if marque[p]]


def factorisation(n):
    """Liste (premier,exposant), n>=1 ; cas 1 : liste vide."""
    entier(n, 1)
    resultat, p = [], 2
    while p*p <= n:
        exposant = 0
        while n % p == 0:
            n //= p
            exposant += 1
        if exposant:
            resultat.append((p, exposant))
        p += 1
    if n > 1:
        resultat.append((n, 1))
    return resultat


def dimensions(a):
    if not a or not a[0] or any(len(ligne) != len(a[0]) for ligne in a):
        raise ValueError("matrice rectangulaire non vide requise")
    return len(a), len(a[0])


def produit(a, b):
    m, k = dimensions(a)
    kb, n = dimensions(b)
    if k != kb:
        raise ValueError("dimensions incompatibles")
    return [[sum(a[i][r]*b[r][j] for r in range(k)) for j in range(n)] for i in range(m)]


def puissance_matrice(a, n):
    entier(n)
    m, k = dimensions(a)
    if m != k:
        raise ValueError("matrice carrée requise")
    resultat = [[int(i == j) for j in range(m)] for i in range(m)]
    base = [ligne[:] for ligne in a]
    while n:
        if n % 2:
            resultat = produit(resultat, base)
        base = produit(base, base)
        n //= 2
    return resultat


def markov(mu, p, n):
    """Distribution ligne mu P**n ; contrôle des probabilités à 1e-12 près."""
    m, k = dimensions(p)
    if m != k or len(mu) != m:
        raise ValueError("dimensions incompatibles")
    for ligne in [mu]+p:
        for x in ligne:
            probabilite(x)
        if abs(sum(ligne)-1) > 1e-12:
            raise ValueError("chaque distribution doit sommer à 1")
    return produit([mu], puissance_matrice(p, n))[0]
