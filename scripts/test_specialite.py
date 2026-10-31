"""Vérifier la structure et la numérotation du dossier thématique de trigonométrie."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "sources/specialite/trigonometrie"
NIVEAU = "specialite-trigonometrie"


class TrigonometrieSpecialiteTest(unittest.TestCase):
    def test_catalogue_et_quatre_maitres(self):
        niveaux = json.loads((ROOT / "niveaux.json").read_text(encoding="utf-8"))
        self.assertIn(NIVEAU, niveaux)
        self.assertEqual(niveaux[NIVEAU]["source"], "sources/specialite/trigonometrie")
        suffixe = niveaux[NIVEAU]["suffixe"]
        for nom in ("cours", "exercices", "corriges", "guide"):
            document = MODULE / f"{nom}_{suffixe}.tex"
            self.assertTrue(document.is_file(), document)
            contenu = document.read_text(encoding="utf-8")
            self.assertIn(r"\usepackage{mathscommun}", contenu)
            self.assertIn(r"\begin{document}", contenu)
            self.assertIn(r"\end{document}", contenu)

    def test_chapitres_autonomes_et_ordonnes(self):
        chapitres = sorted((MODULE / "chapitres").glob("[0-9][0-9]_*.tex"))
        self.assertEqual(len(chapitres), 19)
        maitre = (MODULE / "cours_spe_trigo.tex").read_text(encoding="utf-8")
        for index, chemin in enumerate(chapitres, start=1):
            texte = chemin.read_text(encoding="utf-8")
            self.assertIn(r"\documentclass[../cours_spe_trigo.tex]{subfiles}", texte)
            self.assertIn(rf"\setcounter{{chapter}}{{{index-1}}}", texte)
            self.assertIn(r"\chapter{", texte)
            self.assertEqual(maitre.count(r"\subfile{chapitres/" + chemin.name + "}"), 1)

    def test_40_exercices_40_corriges_correspondants(self):
        def numeros(repertoire, commande):
            contenu = "\n".join(p.read_text(encoding="utf-8")
                               for p in sorted((MODULE / repertoire).glob("*.tex")))
            return [int(x) for x in re.findall(r"\\" + commande + r"\{(\d+)", contenu)]
        self.assertEqual(numeros("exercices", "exercice"), list(range(1, 41)))
        self.assertEqual(numeros("corriges", "corrige"), list(range(1, 41)))

    def test_fondements_et_preuves_presentes(self):
        sources = "\n".join(p.read_text(encoding="utf-8")
                            for p in sorted((MODULE / "chapitres").glob("*.tex")))
        self.assertIn(r"\begin{demonstration}", sources)
        for notion in (r"\pi=\frac{C}{D}", "homothétie", "radians", "rotations", r"\sin", r"\cos"):
            self.assertIn(notion, sources)
        guide = (MODULE / "guide_spe_trigo.tex").read_text(encoding="utf-8")
        self.assertIn("Fondement admis", guide)
        self.assertIn("Table de couverture", guide)
        self.assertIn("diagnostic", guide)


if __name__ == "__main__":
    unittest.main()
