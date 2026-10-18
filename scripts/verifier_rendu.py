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

import fitz
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, default=ROOT / "build" / "apercus")
    args = parser.parse_args()
    destination = args.destination
    destination.mkdir(parents=True, exist_ok=True)
    rapport = {}
    mots = {
        "cours_2de": ["Distance entre deux points", "lecture graphique", "fonction inverse",
                     "Boîte à moustaches", "Classes de même amplitude",
                     "Un arbre pondéré", "Un tableau réel", "Concours des trois hauteurs"],
        "guide_2de": ["Table de couverture", "Réponses et contrôles"],
        "corriges_2de": ["Un jardin et son coût", "Un diagnostic fictif"],
        "exercices_2de": ["Classes et histogramme"],
    }
    for pdf in sorted((ROOT / "pdf" / "seconde").glob("*.pdf")):
        doc = fitz.open(pdf)
        alertes = []
        selections = {0}
        for numero, page in enumerate(doc):
            texte = page.get_text()
            if "\ufffd" in texte or "??" in texte:
                alertes.append(f"Page {numero+1} : caractère ou référence à vérifier")
            for x0, y0, x1, y1, mot, *_ in page.get_text("words"):
                if x0 < -1 or y0 < -1 or x1 > page.rect.width+1 or y1 > page.rect.height+1:
                    alertes.append(f"Page {numero+1} : texte hors page ({mot!r})")
            for mot in mots.get(pdf.stem, []):
                if mot.casefold() in texte.casefold() and numero > 3:
                    selections.add(numero)
        rapport[pdf.name] = {"pages": len(doc), "alertes": alertes}
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
        raise SystemExit("Les quatre PDF de seconde sont requis")
    (destination / "rapport.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps(rapport, ensure_ascii=False, indent=2))
    if any(v["alertes"] for v in rapport.values()):
        raise SystemExit("Rendu à vérifier : voir les alertes")


if __name__ == "__main__":
    main()
