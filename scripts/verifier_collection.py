#!/usr/bin/env python3
"""Exécuter les contrôles de chaque niveau déclaré, puis inspecter ses PDF."""
from pathlib import Path
import subprocess
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from compiler import ROOT, NIVEAUX

for niveau, config in NIVEAUX.items():
    verification = ROOT / config['source'] / 'python' / 'verifier.py'
    if verification.exists():
        subprocess.run([sys.executable, str(verification)], check=True)
    subprocess.run([sys.executable, str(ROOT / 'scripts/verifier_rendu.py'),
                    '--niveau', niveau], check=True)
