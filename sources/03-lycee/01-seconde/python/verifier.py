"""Vérifications mathématiques des exemples exécutables (bibliothèque standard)."""
from fractions import Fraction
from math import sqrt
import unittest
from outils import (
    alignes, compter_filtre, determinant, dernier_multiple, dichotomie_racine2,
    encadrer_racine2, equation_droite, esch_autres, est_multiple, frequence,
    lire_cantons, longueur_polygonale, maximum_grille, moyenne_ecart_type,
    seuil_puissance, tableau_croise,
)


class Verifications(unittest.TestCase):
    def test_divisibilite_frontieres(self):
        for a in range(1, 20):
            for b in range(70):
                m = dernier_multiple(a, b)
                self.assertTrue(m <= b < m + a)
                self.assertTrue(est_multiple(m, a))
        self.assertTrue(est_multiple(-42, 6))
        with self.assertRaises(ValueError):
            est_multiple(3, 0)

    def test_seuil_strict_exact(self):
        self.assertEqual(seuil_puissance(Fraction(11, 10), 2), 8)
        self.assertEqual(seuil_puissance(Fraction(3, 2), Fraction(27, 8)), 4)
        self.assertEqual(seuil_puissance(2, 1), 1)
        with self.assertRaises(ValueError):
            seuil_puissance(1, 2)

    def test_encadrements_certifies(self):
        for n in range(5):
            bas, haut, d = encadrer_racine2(n)
            self.assertTrue(bas*bas <= 2*d*d < haut*haut)
            self.assertEqual(haut-bas, 1)
            self.assertEqual(d, 10**n)
        for n in [0, 1, 7, 10, 20]:
            a, b = dichotomie_racine2(n)
            self.assertTrue(a*a <= 2 <= b*b)
            self.assertEqual(b-a, Fraction(1, 2**n))

    def test_geometrie_et_cas_verticaux(self):
        self.assertTrue(alignes((1, -1), (3, 2), (5, 5)))
        self.assertFalse(alignes((0, 0), (1, 1), (2, 3)))
        self.assertEqual(determinant((0, 3), (0, -4)), 0)
        for A, B in [((4, 0), (4, 3)), ((1, 2), (3, 6)), ((0, 2), (3, 0))]:
            a, b, c = equation_droite(A, B)
            for x, y in [A, B]:
                self.assertEqual(a*x+b*y+c, 0)
            self.assertNotEqual((a, b), (0, 0))
        with self.assertRaises(ValueError):
            equation_droite((0, 0), (0, 0))

    def test_grille_ne_prouve_pas_maximum_continu(self):
        x, y = maximum_grille(lambda t: 1-(t-0.3)**2, 0, 1, 2)
        self.assertEqual(x, 0.5)
        self.assertAlmostEqual(y, 0.96)
        self.assertLess(y, 1)

    def test_longueur_polygonale(self):
        self.assertAlmostEqual(longueur_polygonale(lambda x: x*x, 0, 1, 1), sqrt(2))
        self.assertAlmostEqual(longueur_polygonale(lambda x: x*x, 0, 1, 2),
                               (sqrt(5)+sqrt(13))/4)
        valeurs = [longueur_polygonale(lambda x: x*x, 0, 1, n) for n in [1, 2, 4, 8]]
        self.assertEqual(valeurs, sorted(valeurs))
        # Pour une droite, toute subdivision donne la même longueur.
        self.assertAlmostEqual(longueur_polygonale(lambda x: 2*x+1, 0, 3, 7), 3*sqrt(5))

    def test_statistiques_et_changement_echelle(self):
        valeurs = [1, 2, 2, 4, 5, 8, 8, 10]
        m, s = moyenne_ecart_type(valeurs)
        self.assertEqual(m, 5)
        self.assertAlmostEqual(s, sqrt(39)/2)
        m2, s2 = moyenne_ecart_type([-3*x+2 for x in valeurs])
        self.assertEqual(m2, -13)
        self.assertAlmostEqual(s2, 3*s)
        self.assertEqual(moyenne_ecart_type([7, 7, 7]), (7, 0))
        with self.assertRaises(ValueError):
            moyenne_ecart_type([])

    def test_simulation_extremes_et_reproductibilite(self):
        self.assertEqual(frequence(0, 100, 42), 0)
        self.assertEqual(frequence(1, 100, 42), 1)
        self.assertEqual(frequence(0.5, 100, 42), frequence(0.5, 100, 42))
        self.assertTrue(0 <= frequence(0.3, 200, 8) <= 1)
        with self.assertRaises(ValueError):
            frequence(0.5, 0)

    def test_tableau_et_connecteurs(self):
        sites = ["A", "A", "B", "B"]
        casques = [True, False, True, True]
        individus = list(zip(sites, casques))
        t = tableau_croise(sites, casques)
        self.assertEqual(t, {("A", True): 1, ("A", False): 1, ("B", True): 2})
        self.assertEqual(compter_filtre(individus, lambda p: p[0] == "A" and p[1]), 1)
        self.assertEqual(compter_filtre(individus, lambda p: p[0] == "A" or p[1]), 4)
        self.assertEqual(compter_filtre(individus, lambda p: not p[1]), 1)
        with self.assertRaises(ValueError):
            tableau_croise(["A"], [])

    def test_donnees_reelles_et_marges(self):
        lignes = lire_cantons()
        self.assertEqual(len(lignes), 12)
        self.assertEqual(sum(f for _, f, _ in lignes), 339161)
        self.assertEqual(sum(h for _, _, h in lignes), 342812)
        self.assertEqual(esch_autres(lignes),
                         {"Esch-sur-Alzette": [97721, 97370],
                          "Autres cantons": [241440, 245442]})
        self.assertEqual(sum(f+h for _, f, h in lignes), 681973)


if __name__ == "__main__":
    unittest.main(verbosity=2)
