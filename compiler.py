#!/usr/bin/env python3
"""Compiler et vérifier la collection avec le style LaTeX commun."""

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
NIVEAUX = json.loads((ROOT / "niveaux.json").read_text(encoding="utf-8"))
DOCUMENTS = ("cours", "exercices", "corriges", "guide")
PROBLEMES = re.compile(
    r"Overfull \\[hv]box|undefined|Rerun to get cross-references right|"
    r"Label\(s\) may have changed|multiply defined",
    re.IGNORECASE,
)


def compiler(source, destination):
    """Trois passages, puis contrôle du journal du dernier passage."""
    destination.mkdir(parents=True, exist_ok=True)
    environnement = os.environ.copy()
    # Le séparateur final préserve le chemin de recherche standard de TeX.
    environnement["TEXINPUTS"] = (
        str(ROOT / "commun") + os.pathsep + environnement.get("TEXINPUTS", "") + os.pathsep
    )
    for passage in range(1, 4):
        resultat = subprocess.run(
            [
                "pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                "-file-line-error", "-no-shell-escape",
                f"-output-directory={destination}", source.name,
            ],
            cwd=source.parent, env=environnement,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, errors="replace",
        )
        if resultat.returncode:
            print("\n".join(resultat.stdout.splitlines()[-40:]), file=sys.stderr)
            raise SystemExit(f"Échec : {source.name}, passage {passage}.")
    journal = (destination / source.with_suffix(".log").name).read_text(
        encoding="utf-8", errors="replace"
    )
    problemes = [ligne for ligne in journal.splitlines() if PROBLEMES.search(ligne)]
    if problemes:
        print("\n".join(problemes), file=sys.stderr)
        raise SystemExit(f"Vérification nécessaire : {source.name}.")
    pdf = destination / source.with_suffix(".pdf").name
    if not pdf.is_file():
        raise SystemExit(f"PDF absent : {pdf}.")
    print(f"OK : {source.relative_to(ROOT)}", flush=True)
    return pdf


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--niveau", choices=sorted(NIVEAUX), help="Niveau à compiler.")
    parser.add_argument("--chapitre", type=int, help="Numéro du chapitre seul.")
    parser.add_argument("--document", type=Path, help="Fichier .tex relatif au dépôt.")
    args = parser.parse_args()
    if args.document is not None and (args.niveau is not None or args.chapitre is not None):
        parser.error("--document ne se combine pas avec --niveau ou --chapitre.")
    if not shutil.which("pdflatex"):
        raise SystemExit("pdfLaTeX introuvable : installer TeX Live ou MiKTeX.")

    if args.document is not None:
        source = (ROOT / args.document).resolve()
        if ROOT not in source.parents or source.suffix != ".tex" or not source.is_file():
            parser.error("--document doit désigner un fichier .tex existant du dépôt.")
        relatif = source.relative_to(ROOT)
        pdf = compiler(source, ROOT / "build" / "documents" / relatif.parent / source.stem)
        print(f"PDF : {pdf.relative_to(ROOT)}")
        return

    if args.chapitre is not None:
        niveau = args.niveau or "troisieme"
        if args.chapitre < 1:
            parser.error("--chapitre doit être positif.")
        choix = sorted((ROOT / NIVEAUX[niveau]["source"] / "chapitres").glob(f"{args.chapitre:02d}_*.tex"))
        if len(choix) != 1:
            parser.error(f"Chapitre {args.chapitre} introuvable ou ambigu pour {niveau}.")
        pdf = compiler(choix[0], ROOT / "build" / niveau / "chapitres")
        print(f"PDF : {pdf.relative_to(ROOT)}")
        return

    # Ne remplacer les PDF publiés qu'une fois toutes les compilations réussies.
    publications = []
    for niveau in ([args.niveau] if args.niveau else NIVEAUX):
        for document in DOCUMENTS:
            source = ROOT / NIVEAUX[niveau]["source"] / f"{document}_{NIVEAUX[niveau]['suffixe']}.tex"
            pdf = compiler(source, ROOT / "build" / niveau)
            publications.append((pdf, ROOT / "build" / "pdf" / niveau / pdf.name))
    for source, destination in publications:
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        print(f"PDF : {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
