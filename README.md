# Mathématiques — du collège vers le supérieur

Une collection de cours en français, écrite en LaTeX : définitions, exemples
expliqués, démonstrations, exercices et corrigés. Le fichier
[`mathscommun.sty`](mathscommun.sty) définit la présentation de tous les documents.

L'objectif à terme est un parcours vers des mathématiques universitaires :
calcul maîtrisé, définitions précises, preuves, contre-exemples et autonomie.
Les compléments avancés restent distingués du programme obligatoire.

## Seconde générale et technologique : rentrée 2026

Le dossier suit le **nouveau programme publié au BO du 2 avril 2026**, applicable
à partir de 2026–2027. Il couvre ses quatre domaines et ses trois parties
transversales, avec une table de correspondance détaillée dans le guide.
[Texte officiel et annexe](https://www.education.gouv.fr/bo/2026/Hebdo14/MENE2602914A).

Il comporte **24 chapitres, 144 exercices corrigés, six problèmes de synthèse
et 60 automatismes avec réponses**. Toutes les démonstrations exemplaires
identifiées dans le programme sont rédigées, avec de nombreuses preuves
supplémentaires. Les définitions, fondements admis et approfondissements sont
explicitement distingués.

| Document | PDF | Source LaTeX |
| --- | --- | --- |
| Cours et démonstrations | [Lire le cours](pdf/seconde/cours_2de.pdf) | [cours_2de.tex](seconde/cours_2de.tex) |
| Exercices et problèmes | [Lire les exercices](pdf/seconde/exercices_2de.pdf) | [exercices_2de.tex](seconde/exercices_2de.tex) |
| Corrigés expliqués | [Lire les corrigés](pdf/seconde/corriges_2de.pdf) | [corriges_2de.tex](seconde/corriges_2de.tex) |
| Guide, couverture et révisions | [Lire le guide](pdf/seconde/guide_2de.pdf) | [guide_2de.tex](seconde/guide_2de.tex) |

Les chapitres couvrent nombres et algèbre (1–6), géométrie (7–11),
fonctions (12–16), proportions et statistiques (17–20), probabilités (21–22),
Python (23) et approfondissements vers le supérieur (24).
Logique, programmation et automatismes se travaillent toute l'année ; cet ordre
de consultation n'impose pas une progression linéaire.

Le nouveau programme inclut notamment la valeur absolue, les tableaux croisés,
les séries regroupées en classes et les probabilités conditionnelles.
Le chapitre 24, les barycentres, certaines preuves de concours, la récurrence et
la preuve d'une loi faible des grands nombres sont des **compléments facultatifs**.

- [Algorithmes exécutables et vérifications](seconde/python/README.md).
- [Données cantonales réelles et provenance STATEC](seconde/donnees/README.md).
- Les vecteurs sont introduits depuis le début ; les démonstrations des acquis
  de collège restent accessibles dans le volume de troisième.

## Troisième : documents disponibles

Le dossier couvre le programme français de troisième applicable en **2026–2027**,
avec les prérequis utiles du cycle 4. Il comprend 20 chapitres, 80 exercices,
4 problèmes de synthèse corrigés et 40 automatismes avec réponses.

| Document | PDF | Source LaTeX |
| --- | --- | --- |
| Cours et démonstrations | [Lire le cours](pdf/troisieme/cours_3e.pdf) | [cours_3e.tex](troisieme/cours_3e.tex) |
| Exercices | [Lire les exercices](pdf/troisieme/exercices_3e.pdf) | [exercices_3e.tex](troisieme/exercices_3e.tex) |
| Corrigés expliqués | [Lire les corrigés](pdf/troisieme/corriges_3e.pdf) | [corriges_3e.tex](troisieme/corriges_3e.tex) |
| Guide, couverture et révisions | [Lire le guide](pdf/troisieme/guide_3e.pdf) | [guide_3e.tex](troisieme/guide_3e.tex) |

Commencer par le guide : il présente les sources officielles, la correspondance
entre notions et chapitres, une progression et les principes admis. Les notions
facultatives sont signalées. Une définition n'est pas une proposition à démontrer ;
les propriétés sont justifiées autant que possible au niveau considéré.

Le programme de troisième entrant en application en septembre 2028 devra faire
l'objet d'une vérification spécifique. Sa couverture n'est pas revendiquée ici.

## Organisation

- `mathscommun.sty` : style et environnements pédagogiques communs.
- `troisieme/` et `seconde/` : quatre maîtres par niveau, chapitres, exercices et corrigés.
- `modeles/modele_nouveau_cours.tex` : modèle de départ pour les prochains niveaux.
- `pdf/<niveau>/` : les PDF prêts à lire, suivis dans Git.
- `compiler.py` : compilation avec pdfLaTeX ; fichiers temporaires dans `build/`.

Les figures sont dessinées en TikZ/PGFPlots, sans images externes.

## Compiler

Installer Python 3 et une distribution TeX Live ou MiKTeX avec pdfLaTeX et les
extensions utilisées par le style (notamment `babel`, `lmodern`, `amsmath`,
`tcolorbox`, `tikz`, `pgfplots`, `subfiles` et `listings`). Une installation LaTeX
complète convient. Aucune bibliothèque Python supplémentaire n'est requise.

Depuis la racine du dépôt :

```sh
python3 compiler.py
```

Le script ajoute la racine du dépôt au chemin de recherche de LaTeX pour que tous
les niveaux utilisent **le même fichier de style**. Il effectue trois passages
pour stabiliser sommaires et renvois, puis met à jour les PDF dans `pdf/<niveau>/`.
Les débordements et les références non résolues font échouer la vérification.

Pour compiler uniquement un chapitre ou essayer le modèle :

```sh
python3 compiler.py --niveau seconde
python3 compiler.py --niveau seconde --chapitre 9
python3 seconde/python/verifier.py
python3 compiler.py --document modeles/modele_nouveau_cours.tex
```

Ces PDF ponctuels restent dans `build/`. La commande fonctionne aussi depuis un
autre répertoire si l'on donne le chemin du script. Pour utiliser directement
pdfLaTeX, il faut ajouter la racine du dépôt à `TEXINPUTS` et travailler dans le
dossier du document ; le script le fait automatiquement.

La vérification GitHub Actions compile tous les niveaux et un chapitre autonome,
puis exécute les contrôles Python et prépare des planches de rendu. Les PDF et
aperçus sont disponibles dans les artefacts de la vérification pendant 14 jours.
Le workflow final fonctionne en lecture seule sur le dépôt : les PDF suivis dans
Git restent à actualiser dans la PR avec leurs sources.

Pour refaire les planches localement, `scripts/verifier_rendu.py` utilise Poppler
(`pdftoppm`), PyMuPDF et Pillow ; ces outils sont facultatifs pour la compilation
LaTeX normale. Les aperçus restent dans `build/apercus/`. Les anomalies
d'extraction Unicode sont signalées avec leur contexte pour inspection visuelle :
elles ne signifient pas nécessairement qu'un glyphe est absent du PDF.

## Suite de la collection et contributions

La troisième et la seconde sont rédigées. La première et la terminale
seront ajoutées dans des PR distinctes, avec une orientation vers la spécialité
mathématiques et les compléments utiles au supérieur. Pour la première et la terminale, chaque
dossier devra préciser la voie, l'enseignement (commun ou spécialité), les options
éventuelles et l'année d'application du programme avant d'en annoncer la couverture.

Tout ajout ou correction passe par une branche et une **pull request**. Une PR
décrit le périmètre traité, les documents modifiés et les vérifications effectuées.
Après un changement du style ou du compilateur commun, recompiler tous les niveaux.
Les sources et leurs PDF doivent rester cohérents. Les consignes de rédaction et
de vérification sont dans [`AGENTS.md`](AGENTS.md).
