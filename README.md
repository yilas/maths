# Mathématiques — de la troisième à la terminale

Une collection de cours en français, écrite en LaTeX : définitions, exemples
expliqués, démonstrations, exercices et corrigés. Le fichier
[`mathscommun.sty`](mathscommun.sty) définit la présentation de tous les documents.

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
- `troisieme/` : quatre documents maîtres et dossiers `chapitres/`, `exercices/`, `corriges/`.
- `modeles/modele_nouveau_cours.tex` : modèle de départ pour les prochains niveaux.
- `pdf/troisieme/` : les quatre PDF prêts à lire, suivis dans Git.
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
pour stabiliser sommaires et renvois, puis met à jour les PDF dans `pdf/troisieme/`.
Les débordements et les références non résolues font échouer la vérification.

Pour compiler uniquement un chapitre ou essayer le modèle :

```sh
python3 compiler.py --niveau troisieme --chapitre 14
python3 compiler.py --document modeles/modele_nouveau_cours.tex
```

Ces PDF ponctuels restent dans `build/`. La commande fonctionne aussi depuis un
autre répertoire si l'on donne le chemin du script. Pour utiliser directement
pdfLaTeX, il faut ajouter la racine du dépôt à `TEXINPUTS` et travailler dans le
dossier du document ; le script le fait automatiquement.

## Suite de la collection et contributions

La troisième est le premier niveau rédigé. La seconde, la première et la terminale
seront ajoutées dans des PR distinctes. Pour la première et la terminale, chaque
dossier devra préciser la voie, l'enseignement (commun ou spécialité), les options
éventuelles et l'année d'application du programme avant d'en annoncer la couverture.

Tout ajout ou correction passe par une branche et une **pull request**. Une PR
décrit le périmètre traité, les documents modifiés et les vérifications effectuées.
Après un changement du style commun, recompiler les quatre documents existants.
Les sources et leurs PDF doivent rester cohérents. Les consignes de rédaction et
de vérification sont dans [`AGENTS.md`](AGENTS.md).
