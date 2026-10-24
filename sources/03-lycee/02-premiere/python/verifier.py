"""Vérifications déterministes des algorithmes et de leurs contrats."""
import math
import random
import unittest
from outils import (
    archimede, euler, experience_moyennes, factorielle, fibonacci,
    frequences_lettres, marche_aleatoire, moments, monte_carlo,
    newton_racine, premier_seuil, sommes_cumulees, syracuse,
    taux_accroissement, termes_affines, tirer,
)


class Algorithmes(unittest.TestCase):
    def test_factorielle_et_cas_vides(self):
        self.assertEqual(factorielle(0), 1)
        self.assertEqual(factorielle(20), math.factorial(20))
        self.assertEqual(sommes_cumulees([]), [])
        self.assertEqual(sommes_cumulees([1, -2, 4]), [1, -1, 3])

    def test_entiers_invalides(self):
        for n in (-1, 2.5, True):
            with self.assertRaises(ValueError):
                factorielle(n)

    def test_fibonacci_et_somme(self):
        f = fibonacci(30)
        self.assertEqual(f[:7], [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(sum(fibonacci(28)), f[30] - 1)

    def test_affine_formule_fermee_et_seuil(self):
        for n, u in enumerate(termes_affines(0.8, 30, 50, 20)):
            self.assertAlmostEqual(u, 150 - 100 * 0.8 ** n)
        self.assertEqual(premier_seuil(lambda u: 0.8*u+30, 50, 140)[0], 11)
        self.assertEqual(premier_seuil(lambda u: u, 50, 50, 0), (0, 50))
        with self.assertRaises(RuntimeError):
            premier_seuil(lambda u: u/2, 1, 2, 10)

    def test_syracuse_borne_sans_affirmer_la_conjecture(self):
        self.assertEqual(syracuse(6), ([6, 3, 10, 5, 16, 8, 4, 2, 1], True))
        self.assertEqual(syracuse(6, 2), ([6, 3, 10], False))
        self.assertEqual(syracuse(1, 0), ([1], True))
        with self.assertRaises(ValueError):
            syracuse(0)

    def test_taux_exacts_dun_polynome(self):
        hs = [0.5, 0.25, -0.5]
        self.assertEqual(taux_accroissement(lambda x: x*x, 2, hs), [4+h for h in hs])
        with self.assertRaises(ValueError):
            taux_accroissement(lambda x: x, 0, [0])

    def test_euler_solution_affine_exacte(self):
        t, y = euler(lambda t, y: 3, 0, 2, 1, 8)
        self.assertEqual(y, [2+3*x for x in t])
        self.assertEqual(len(t), 9)
        self.assertEqual(t[-1], 1)

    def test_euler_ordre_et_borne_theorique(self):
        erreurs = []
        for n in (20, 40, 80):
            _, y = euler(lambda t, y: y, 0, 1, 1, n)
            erreur = math.e-y[-1]
            self.assertGreater(erreur, 0)
            self.assertLess(erreur, 0.5*math.e*(math.e-1)/n)
            erreurs.append(erreur)
        for a, b in zip(erreurs, erreurs[1:]):
            self.assertTrue(1.8 < a/b < 2.1)

    def test_euler_instabilite(self):
        _, y = euler(lambda t, y: -3*y, 0, 1, 4, 4)
        self.assertEqual(y, [1, -2, 4, -8, 16])
        with self.assertRaises(ValueError):
            euler(lambda t, y: y, 0, 1, 1, 0)

    def test_newton_largeur_et_racines(self):
        for a in (0.04, 2, 3, 100):
            bas, haut, termes = newton_racine(a, 1e-9)
            self.assertLessEqual(bas, math.sqrt(a)+1e-14)
            self.assertGreaterEqual(haut, math.sqrt(a)-1e-14)
            self.assertLessEqual(haut-bas, 1e-9)
            self.assertLessEqual(len(termes), 100)
        with self.assertRaises(ValueError):
            newton_racine(-1)
        with self.assertRaises(RuntimeError):
            newton_racine(2, 1e-15, 1)

    def test_archimede_geometrie(self):
        lignes = archimede(8)
        self.assertEqual(lignes[0][0], 6)
        self.assertAlmostEqual(lignes[0][1], 3)
        self.assertAlmostEqual(lignes[0][2], 2*math.sqrt(3))
        for i, (n, bas, haut) in enumerate(lignes):
            self.assertEqual(n, 6*2**i)
            self.assertLess(bas, math.pi)
            self.assertGreater(haut, math.pi)
            if i:
                self.assertGreater(bas, lignes[i-1][1])
                self.assertLess(haut, lignes[i-1][2])

    def test_moments_huygens_et_changement_unite(self):
        valeurs, probas = [0, 2, 5], [1/2, 1/3, 1/6]
        mu, variance, sigma = moments(valeurs, probas)
        self.assertAlmostEqual(mu, 1.5)
        self.assertAlmostEqual(variance, 3.25)
        self.assertAlmostEqual(sigma**2, variance)
        nouveau = moments([2*x-5 for x in valeurs], probas)
        self.assertAlmostEqual(nouveau[0], 2*mu-5)
        self.assertAlmostEqual(nouveau[1], 4*variance)

    def test_lois_invalides(self):
        for valeurs, probas in (([], []), ([1], [.8]), ([1, 2], [-1, 2]),
                                ([1, 1], [.5, .5]), ([math.inf], [1])):
            with self.assertRaises(ValueError):
                moments(valeurs, probas)

    def test_tirage_seuils_et_probabilites_nulles(self):
        class Generateur:
            def __init__(self, valeur):
                self.valeur = valeur
            def random(self):
                return self.valeur
        self.assertEqual(tirer([2, 3, 4], [0, .25, .75], Generateur(0)), 3)
        self.assertEqual(tirer([2, 3, 4], [0, .25, .75], Generateur(.25)), 4)
        self.assertEqual(tirer([2, 3, 4], [0, 1, 0], random.Random(4)), 3)

    def test_echantillons_degeneres_et_reproductibles(self):
        moyennes, p = experience_moyennes([2], [1], 10, 50)
        self.assertEqual(moyennes, [2]*50)
        self.assertEqual(p, 1)
        args = ([0, 1], [.7, .3], 100, 500, 2026)
        a = experience_moyennes(*args)
        self.assertEqual(a, experience_moyennes(*args))
        self.assertLess(abs(sum(a[0])/len(a[0])-.3), .03)
        self.assertTrue(.85 < a[1] <= 1)

    def test_monte_carlo_reproductibilite_et_echelle(self):
        a = monte_carlo(50000, 2026)
        self.assertEqual(a, monte_carlo(50000, 2026))
        self.assertLess(abs(a[0]-1/3), .02)
        self.assertLess(abs(a[1]-math.pi), .06)

    def test_marche_parite_et_extremes(self):
        for n, position in enumerate(marche_aleatoire(50)):
            self.assertEqual((position-n) % 2, 0)
            self.assertLessEqual(abs(position), n)
        self.assertEqual(marche_aleatoire(3, 1), [0, 1, 2, 3])
        self.assertEqual(marche_aleatoire(3, 0), [0, -1, -2, -3])

    def test_lettres_accents_et_conventions(self):
        f = frequences_lettres("été")
        self.assertAlmostEqual(f[4], 2/3)
        self.assertAlmostEqual(f[19], 1/3)
        self.assertAlmostEqual(sum(f), 1)
        self.assertEqual(frequences_lettres("œ"), frequences_lettres("oe"))
        with self.assertRaises(ValueError):
            frequences_lettres("123 !")


if __name__ == "__main__":
    unittest.main(verbosity=2)
