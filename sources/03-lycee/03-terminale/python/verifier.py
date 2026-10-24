#!/usr/bin/env python3
"""Contrôles numériques, cas limites et cohérence des quatre documents."""
import json
import math
from pathlib import Path
import re
import unittest
from fractions import Fraction as F
from random import Random
import algorithmes as a


class Verification(unittest.TestCase):
    def test_pascal(self):
        for n, ligne in enumerate(a.pascal(15)):
            self.assertEqual(ligne, [math.comb(n, k) for k in range(n+1)])
            self.assertEqual(sum(ligne), 2**n)
        self.assertEqual(a.pascal(0), [[1]])

    def test_permutations(self):
        resultat = a.permutations(range(5))
        self.assertEqual(len({tuple(p) for p in resultat}), math.factorial(5))
        self.assertTrue(all(sorted(p) == list(range(5)) for p in resultat))
        self.assertEqual(a.permutations([]), [[]])

    def test_combinaisons(self):
        for k in (0, 2, 3, 6, 7):
            r = a.combinaisons(range(6), k)
            self.assertEqual(len(r), math.comb(6, k) if k <= 6 else 0)
            self.assertEqual(len(r), len({tuple(x) for x in r}))
            self.assertTrue(all(x == sorted(set(x)) for x in r))

    def test_permutation_aleatoire(self):
        valeurs = list(range(30))
        r = a.permutation_aleatoire(valeurs, Random(4))
        self.assertEqual(sorted(r), valeurs)
        self.assertEqual(r, a.permutation_aleatoire(valeurs, Random(4)))
        self.assertEqual(valeurs, list(range(30)))

    def test_seuil(self):
        n, u = a.premier_seuil(F(1), lambda x: x*F(4, 5), lambda x: x < F(1, 10))
        self.assertEqual(n, 11)
        self.assertLess(u, F(1, 10))
        self.assertGreaterEqual(u/F(4, 5), F(1, 10))
        self.assertEqual(a.premier_seuil(2, lambda x: x, lambda x: x == 2), (0, 2))
        with self.assertRaises(RuntimeError):
            a.premier_seuil(0, lambda x: x, lambda x: x > 1, 4)

    def test_dichotomie(self):
        g, d = a.dichotomie(lambda x: x*x-2, 1, 2, 1e-9)
        self.assertLessEqual(g*g, 2)
        self.assertGreaterEqual(d*d, 2)
        self.assertLessEqual(d-g, 2e-9)
        self.assertEqual(a.dichotomie(lambda x: x, 0, 1), (0, 0))
        with self.assertRaises(ValueError):
            a.dichotomie(lambda x: x*x+1, -1, 1)

    def test_newton(self):
        x = a.newton(lambda x: x*x-2, lambda x: 2*x, 2)
        self.assertAlmostEqual(x, math.sqrt(2), places=9)
        with self.assertRaises(RuntimeError):
            a.newton(lambda x: x**3-2*x+2, lambda x: 3*x*x-2, 0, max_etapes=10)
        with self.assertRaises(ValueError):
            a.newton(lambda x: x*x+1, lambda x: 2*x, 0)

    def test_secante(self):
        self.assertAlmostEqual(a.secante(lambda x: x*x-2, 1, 2), math.sqrt(2), places=9)
        with self.assertRaises(ValueError):
            a.secante(lambda x: 1, 0, 1)

    def test_heron_exact(self):
        u = a.heron(F(2), F(2), 3)[-1]
        self.assertEqual(u, F(577, 408))
        self.assertEqual(u-2/u, F(1, 235416))
        self.assertGreaterEqual(u*u, 2)
        self.assertLessEqual((2/u)**2, 2)

    def test_euler(self):
        grossier = a.euler(lambda t, y: y, 0, 1, 0.1, 10)[-1][1]
        fin = a.euler(lambda t, y: y, 0, 1, 0.01, 100)[-1][1]
        self.assertLess(abs(fin-math.e), abs(grossier-math.e))
        self.assertEqual(a.euler(lambda t, y: -4*y, 0, 1, 1, 3)[-1], (3, -27))

    def test_quadratures(self):
        for methode in ('gauche', 'droite', 'milieu', 'trapezes'):
            self.assertAlmostEqual(a.quadrature(lambda x: 3, 1, 4, 10, methode), 9)
        f = lambda x: x*x
        milieu = a.quadrature(f, 0, 1, 20)
        trapezes = a.quadrature(f, 0, 1, 20, 'trapezes')
        self.assertLess(milieu, 1/3)
        self.assertGreater(trapezes, 1/3)
        self.assertAlmostEqual(a.quadrature(lambda x: 2*x+1, 0, 2, 8, 'trapezes'), 6)
        g = a.quadrature(lambda x: 1/x, 1, 2, 100, 'gauche')
        d = a.quadrature(lambda x: 1/x, 1, 2, 100, 'droite')
        self.assertLessEqual(d, math.log(2))
        self.assertGreaterEqual(g, math.log(2))
        self.assertAlmostEqual(g-d, 1/200)

    def test_logarithmes(self):
        for x in (0.5, 2, 10):
            self.assertLess(abs(a.briggs(x)-math.log(x)), 1e-4)
        g, d = a.brouncker(50)
        self.assertLess(float(g), math.log(2))
        self.assertGreater(float(d), math.log(2))
        self.assertEqual(d-g, F(1, 101))

    def test_binomiale(self):
        for n, p in ((0, 0.3), (10, 0), (10, 1), (20, 0.3), (1000, 0.99)):
            loi = a.binomiale(n, p)
            self.assertAlmostEqual(sum(loi), 1)
            self.assertAlmostEqual(sum(k*v for k, v in enumerate(loi)), n*p, places=8)
            self.assertAlmostEqual(sum((k-n*p)**2*v for k, v in enumerate(loi)), n*p*(1-p), places=8)
            self.assertTrue(all(v >= 0 for v in loi))
        for k, valeur in enumerate(a.binomiale(5, 1/3)):
            exacte = math.comb(5, k)*F(1, 3)**k*F(2, 3)**(5-k)
            self.assertAlmostEqual(valeur, float(exacte))

    def test_quantiles(self):
        self.assertEqual(a.quantile_binomial(10, 0.5, 0.95), 8)
        self.assertEqual(a.quantile_binomial(10, 1, 1), 10)
        self.assertEqual(a.quantile_binomial(10, 0, 1), 0)
        self.assertEqual(a.quantile_binomial(10, 0.5, 0), 0)

    def test_surbooking_exact(self):
        n = a.surbooking(100, 0.9, 0.05)
        self.assertEqual(n, 106)
        for inscrits, autorise in ((106, True), (107, False)):
            risque = sum((math.comb(inscrits, k)*F(9, 10)**k*F(1, 10)**(inscrits-k)
                          for k in range(101, inscrits+1)), F(0))
            self.assertEqual(risque <= F(1, 20), autorise)
            self.assertAlmostEqual(sum(a.binomiale(inscrits, 0.9)[101:]), float(risque))

    def test_simulations(self):
        histogramme = a.galton(8, 1000, graine=17)
        self.assertEqual(sum(histogramme), 1000)
        self.assertEqual(histogramme, a.galton(8, 1000, graine=17))
        self.assertEqual(a.galton(3, 7, 0), [7, 0, 0, 0])
        self.assertEqual(a.galton(3, 7, 1), [0, 0, 0, 7])
        r = a.moyennes_bernoulli(20, 50, 0.3, 7)
        self.assertEqual(r, a.moyennes_bernoulli(20, 50, 0.3, 7))
        self.assertTrue(all(0 <= x <= 1 for x in r))
        self.assertEqual(a.monte_carlo(lambda x: 3, 1, 4, 100), 9)
        self.assertEqual(a.pi_disque(1000, 5), a.pi_disque(1000, 5))

    def test_euclide(self):
        for x, y in ((252, 198), (35, 22), (-35, 22), (0, 9), (0, 0), (14, -21)):
            d, u, v = a.euclide_etendu(x, y)
            self.assertEqual(d, math.gcd(x, y))
            self.assertEqual(x*u+y*v, d)
        self.assertEqual(a.inverse_modulaire(7, 11), 8)
        with self.assertRaises(ValueError):
            a.inverse_modulaire(6, 9)

    def test_puissance_modulaire_et_rsa(self):
        for x, n, m in ((7, 2026, 10), (3, 100, 7), (2, 340, 341), (5, 0, 1), (-7, 25, 11)):
            self.assertEqual(a.puissance_modulaire(x, n, m), pow(x, n, m))
        for message in range(55):
            chiffre = a.puissance_modulaire(message, 3, 55)
            self.assertEqual(a.puissance_modulaire(chiffre, 27, 55), message)

    def test_premiers(self):
        self.assertEqual(a.crible(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
        self.assertEqual(a.crible(1), [])
        for n in range(1, 200):
            facteurs = a.factorisation(n)
            self.assertEqual(math.prod(p**e for p, e in facteurs), n)
            self.assertTrue(all(p in a.crible(p) for p, _ in facteurs))
        self.assertEqual(a.factorisation(360), [(2, 3), (3, 2), (5, 1)])

    def test_matrices(self):
        m = [[2, 1], [1, 2]]
        for n in (0, 1, 5, 12):
            self.assertEqual(a.puissance_matrice(m, n),
                             [[(3**n+1)//2, (3**n-1)//2], [(3**n-1)//2, (3**n+1)//2]])
        self.assertEqual(a.produit([[1, 2, 3]], [[1], [0], [-1]]), [[-2]])
        with self.assertRaises(ValueError):
            a.produit([[1, 2]], [[1, 2]])
        with self.assertRaises(ValueError):
            a.puissance_matrice([[1, 2]], 2)

    def test_graphes(self):
        m = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        self.assertEqual(a.puissance_matrice(m, 2), [[1, 0, 1], [0, 2, 0], [1, 0, 1]])

    def test_markov_exact(self):
        p = [[F(1, 2) if i == j else F(1, 4) for j in range(3)] for i in range(3)]
        for n in (0, 1, 5):
            attendu = [F(1, 3)+F(1, 4)**n*(int(j == 0)-F(1, 3)) for j in range(3)]
            self.assertEqual(a.markov([1, 0, 0], p, n), attendu)
        self.assertEqual(a.markov([1, 0], [[0, 1], [1, 0]], 11), [0, 1])
        with self.assertRaises(ValueError):
            a.markov([1, 0], [[0.8, 0.3], [0, 1]], 3)

    def test_entrees_invalides(self):
        for fonction, args in ((a.pascal, (-1,)), (a.pascal, (True,)),
                               (a.binomiale, (3, 1.1)), (a.briggs, (0,)),
                               (a.quadrature, (lambda x: x, 0, 1, 0)),
                               (a.euler, (lambda t, y: y, 0, 1, -1, 2)),
                               (a.dichotomie, (lambda x: x, -1, 1, 0)),
                               (a.factorisation, (0,)), (a.heron, (2, 0, 3))):
            with self.subTest(fonction=fonction.__name__), self.assertRaises(ValueError):
                fonction(*args)

    def test_coherence_documents(self):
        racine = Path(__file__).resolve().parents[1]
        chapitres = json.loads((racine/'chapitres.json').read_text())
        self.assertEqual(set(chapitres), {str(n) for n in range(1, 37)})
        for n, chapitre in chapitres.items():
            source = racine/'chapitres'/chapitre['fichier']
            self.assertTrue(source.is_file())
            for dossier in ('exercices', 'corriges'):
                texte = (racine/dossier/f'{int(n):02d}.tex').read_text()
                ids = re.findall(r'\\section\*\{Exercice (\d+\.\d+) --', texte)
                self.assertEqual(ids, [f'{n}.{i}' for i in range(1, 7)])
                maitre = (racine/f'{dossier}_tle.tex').read_text()
                self.assertIn(f'\\input{{{dossier}/{int(n):02d}.tex}}', maitre)
            self.assertIn(f'\\subfile{{chapitres/{chapitre["fichier"]}}}', (racine/'cours_tle.tex').read_text())
        for dossier in ('exercices', 'corriges'):
            texte = (racine/dossier/'syntheses.tex').read_text()
            self.assertEqual(re.findall(r'\\section\{S(\d+) --', texte), [str(i) for i in range(1, 9)])


if __name__ == '__main__':
    unittest.main(verbosity=2)
