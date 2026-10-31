#!/usr/bin/env python3
"""Inspecter les PDF et rendre des planches de contrôle avec Poppler.

Les aperçus sont temporaires (build/). --destination permet une publication
ponctuelle sur la branche de PR pour une revue distante, jamais sur main.
"""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from compiler import NIVEAUX

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--niveau", choices=sorted(NIVEAUX), default="seconde")
    parser.add_argument("--destination", type=Path)
    args = parser.parse_args()
    destination = args.destination or ROOT / "build" / "apercus" / args.niveau
    destination.mkdir(parents=True, exist_ok=True)
    rapport = {}
    mots = {
        "cours_tle": ["Un cube pour voir", "Projeter sur une droite", "Lire les graphiques",
                      "Pourquoi les dérivées exigent", "Barycentres", "Le tableau se lit",
                      "Aire entre courbes", "polygone régulier", "Le lemme des poignées de main",
                      "Construire rigoureusement", "Graphe pondéré"],
        "guide_tle": ["Table de couverture", "Registre des admissions", "Réponses et contrôles"],
        "exercices_tle": ["Problèmes de synthèse", "Trois états et convergence"],
        "corriges_tle": ["Surbooking", "RSA", "Trois états et convergence"],
        "cours_2de": ["Distance entre deux points", "lecture graphique", "fonction inverse",
                     "Boîte à moustaches", "Classes de même amplitude",
                     "Un arbre pondéré", "Un tableau réel", "Concours des trois hauteurs"],
        "guide_2de": ["Table de couverture", "Réponses et contrôles"],
        "corriges_2de": ["Un jardin et son coût", "Un diagnostic fictif"],
        "exercices_2de": ["Classes et histogramme"],
        "cours_1re": ["La formule en coordonnées", "Lire et construire des oscillations",
                     "Construire une intégrale", "Pourquoi on peut passer à la limite",
                     "La méthode du milieu", "Euler : de l'erreur locale",
                     "La fonction exponentielle", "Une mesure signée"],
        "guide_1re": ["Table de couverture", "Histogramme, bâtons", "Arbre pondéré",
                     "Réponses et contrôles", "Dépendances et admissions"],
        "corriges_1re": ["Contrôle et prédiction", "Projection et cercle",
                        "Approcher une racine", "Variance totale"],
        "exercices_1re": ["Huit problèmes de synthèse"],
    }
    mots.update({
        "cours_spe_trigo": ["Pourquoi le quotient", "Pourquoi les radians", "formules d'addition", "Pourquoi les dérivées"],
        "guide_spe_trigo": ["Table de couverture", "Fondement admis"],
        "exercices_spe_trigo": ["Exercices supplémentaires"],
        "corriges_spe_trigo": ["Corrigés des exercices de démonstration"],
    })
    for pdf in sorted((ROOT / "build" / "pdf" / args.niveau).glob("*.pdf")):
        doc = fitz.open(pdf)
        alertes = []
        observations = []
        selections = {0}
        for numero, page in enumerate(doc):
            texte = page.get_text()
            if "??" in texte:
                alertes.append(f"Page {numero+1} : référence à vérifier")
            if "\ufffd" in texte:
                # Une table ToUnicode de police mathématique peut être incomplète.
                # L'extraction ne suffit pas à conclure à un défaut visuel :
                # conserver le contexte et rendre cette page pour inspection.
                extraits = [texte[max(0, i-35):i+36] for i, c in enumerate(texte)
                            if c == "\ufffd"]
                observations.append({"page": numero+1, "extraction_unicode": extraits})
                selections.add(numero)
            for x0, y0, x1, y1, mot, *_ in page.get_text("words"):
                if x0 < -1 or y0 < -1 or x1 > page.rect.width+1 or y1 > page.rect.height+1:
                    alertes.append(f"Page {numero+1} : texte hors page ({mot!r})")
            for mot in mots.get(pdf.stem, []):
                if mot.casefold() in texte.casefold() and numero > 3:
                    selections.add(numero)
        rapport[pdf.name] = {"pages": len(doc), "alertes": alertes, "observations": observations}
        with tempfile.TemporaryDirectory() as temporaire:
            prefixe = Path(temporaire) / "page"
            subprocess.run(["pdftoppm", "-r", "35", "-png", str(pdf), str(prefixe)],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
            pages = sorted(Path(temporaire).glob("page-*.png"))
            for debut in range(0, len(pages), 8):
                images = [Image.open(f).convert("RGB") for f in pages[debut:debut+8]]
                largeur, hauteur = images[0].size
                planche = Image.new("RGB", (2*largeur, 4*(hauteur+22)), "#dddddd")
                dessin = ImageDraw.Draw(planche)
                for i, image in enumerate(images):
                    x, y = (i % 2)*largeur, (i // 2)*(hauteur+22)
                    dessin.text((x+6, y+4), f"{pdf.stem} - page {debut+i+1}", fill="black")
                    planche.paste(image, (x, y+22))
                planche.save(destination / f"{pdf.stem}-planche-{debut//8+1:02}.png")
            for numero in sorted(selections):
                sortie = destination / f"{pdf.stem}-page-{numero+1:03}"
                subprocess.run(["pdftoppm", "-f", str(numero+1), "-l", str(numero+1),
                                "-r", "100", "-singlefile", "-png", str(pdf), str(sortie)],
                               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
        doc.close()
    if len(rapport) != 4:
        raise SystemExit(f"Les quatre PDF de {args.niveau} sont requis")
    (destination / "rapport.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(rapport, ensure_ascii=False, indent=2))
    if any(v["alertes"] for v in rapport.values()):
        raise SystemExit("Rendu à vérifier : voir les alertes")


if __name__ == "__main__":
    main()
