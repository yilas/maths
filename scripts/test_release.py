"""Contrôler le conditionnement sans dépendre d'une compilation LaTeX."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import zipfile
import preparer_release as publication


class PublicationTest(unittest.TestCase):
    def test_archive_complete_et_nettoyage(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            niveaux = {'sixieme': {'suffixe': '6e'}, 'l1': {'suffixe': 'l1'}}
            for niveau, config in niveaux.items():
                repertoire = racine / 'build/pdf' / niveau
                repertoire.mkdir(parents=True)
                for document in publication.DOCUMENTS:
                    (repertoire / f"{document}_{config['suffixe']}.pdf").write_bytes(b'%PDF-1.7\ntest')
            with patch.object(publication, 'ROOT', racine), patch.object(publication, 'NIVEAUX', niveaux):
                publication.preparer()
                (racine / 'build/release/obsolete.pdf').touch()
                publication.preparer()
            sortie = racine / 'build/release'
            self.assertEqual(len(list(sortie.glob('*.pdf'))), 8)
            with zipfile.ZipFile(sortie / 'maths-tous-les-niveaux.zip') as archive:
                self.assertEqual(set(archive.namelist()),
                                 {f'{n}/{d}.pdf' for n in niveaux for d in publication.DOCUMENTS})
                self.assertIsNone(archive.testzip())
                self.assertTrue(all(archive.read(p).startswith(b'%PDF-') for p in archive.namelist()))

    def test_document_manquant_refuse(self):
        with tempfile.TemporaryDirectory() as dossier:
            racine = Path(dossier)
            with patch.object(publication, 'ROOT', racine):
                with self.assertRaises(SystemExit):
                    publication.preparer()
            self.assertFalse((racine / 'build/release').exists())


if __name__ == '__main__':
    unittest.main()
