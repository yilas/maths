# Spécialité — Trigonométrie, des origines aux démonstrations

Ce dossier thématique approfondit un sujet transversal **de la seconde à la terminale**, avec une passerelle facultative vers le supérieur. « Spécialité » désigne ici une **collection de cours autonomes sur un thème** : elle ne remplace pas les volumes officiels de première/terminale spécialité et ne prétend pas couvrir à elle seule un programme scolaire.

## Documents

| Document | Maître LaTeX | PDF dans la release suivant le prochain tag |
| --- | --- | --- |
| Cours et démonstrations | [`cours_spe_trigo.tex`](cours_spe_trigo.tex) | `specialite-trigonometrie-cours.pdf` |
| Exercices | [`exercices_spe_trigo.tex`](exercices_spe_trigo.tex) | `specialite-trigonometrie-exercices.pdf` |
| Corrigés détaillés | [`corriges_spe_trigo.tex`](corriges_spe_trigo.tex) | `specialite-trigonometrie-corriges.pdf` |
| Guide, diagnostic, couverture, admissions | [`guide_spe_trigo.tex`](guide_spe_trigo.tex) | `specialite-trigonometrie-guide.pdf` |

Le cours est modulaire dans `chapitres/`, les 40 énoncés dans `exercices/` et leurs 40 corrigés correspondants dans `corriges/`. Les figures TikZ et PGFPlots sont incluses dans les sources ; le style reste **`commun/mathscommun.sty`**. Le fichier `commandes.tex` conserve uniquement des alias de couleurs pour les figures historiques.

## Plan de progression

1. Cercle, disque, similitudes, **définition de π**, circonférence et encadrements polygonaux ; fondements admis précisés.
2. Radians, longueur d'arc, secteur, définition du cercle trigonométrique et raccord avec la trigonométrie du collège.
3. Valeurs exactes, symétries et rotations ; démonstrations des formules d'addition et des identités.
4. Tangente, courbes, fonctions, équations et inéquations trigonométriques.
5. Triangles quelconques, vecteurs, produit scalaire, limites, dérivées et primitives.
6. Fonctions réciproques, oscillations et nombres complexes (prolongements signalés), méthodes et synthèse.

La table de couverture et le registre des admissions figurent dans le guide. Chaque exercice possède son corrigé portant le même numéro.

## Compilation locale ou Codespaces

À la racine du dépôt :

```bash
python3 compiler.py --niveau specialite-trigonometrie
# ou
make pdf NIVEAU=specialite-trigonometrie
```

Les quatre PDF sont construits dans `build/pdf/specialite-trigonometrie/`. Ils **ne sont pas suivis dans Git**. La pipeline les assemble dans les artefacts de Pull Request et les publie sur la release GitHub lorsque le commit est tagué.

## Ajouter un autre cours thématique

Créer par exemple `sources/specialite/derivation/`, organiser le cours en `chapitres/`, les énoncés en `exercices/`, les solutions en `corriges/` et maintenir les quatre maîtres `guide_*.tex`, `cours_*.tex`, `exercices_*.tex`, `corriges_*.tex`. Employer le style commun, ajouter l'entrée (`source` et `suffixe`) dans `niveaux.json`, relier les chapitres au guide et tester la compilation des quatre documents. Mettre à jour le catalogue du README principal et le référentiel `OBJECTIFS.md` si le périmètre évolue. Le script `scripts/test_specialite.py` fournit des contrôles de cohérence pour le présent module ; l'étendre pour les modules futurs.

Les notions présentes dans les parcours de première/terminale restent dans leurs volumes existants ; cette collection ajoute la profondeur de preuve et la transversalité, plutôt que de déplacer le programme scolaire.
