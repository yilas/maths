#!/usr/bin/env python3
"""Préparer les quatre PDF par niveau et une archive, sans publier sur GitHub."""
from pathlib import Path
import shutil
import sys
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from compiler import ROOT, NIVEAUX, DOCUMENTS


def preparer():
    fichiers = []
    for niveau, config in NIVEAUX.items():
        for document in DOCUMENTS:
            source = ROOT / 'build/pdf' / niveau / f"{document}_{config['suffixe']}.pdf"
            if not source.is_file() or not source.read_bytes().startswith(b'%PDF-'):
                raise SystemExit(f'PDF manquant ou invalide : {source}')
            fichiers.append((source, niveau, document))
    destination = ROOT / 'build/release'
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    with zipfile.ZipFile(destination / 'maths-tous-les-niveaux.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for source, niveau, document in fichiers:
            shutil.copy2(source, destination / f'{niveau}-{document}.pdf')
            archive.write(source, f'{niveau}/{document}.pdf')
    print(f'{len(fichiers)} PDF et une archive dans {destination}')


if __name__ == '__main__':
    preparer()
