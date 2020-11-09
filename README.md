# exif_and_versionning_image
Supprimer les exifs d'une image et en créer plusieurs version

Lorsque vous téléchargez une image sur un site, un code est ajouté à l'image, qu'on appelle un "exif" et qui renseigne plusieurs informations sur l'image, notamment le propriètaire. Je vous renvoie vers un article de [PhotoRend](https://phototrend.fr/2011/04/mp-87-technique-photo-exifs/) pour la définition claire des exifs.

## Objectif

Ce code vous permettra de supprimer les exifs des images mais également d'en créer 3 versions supplémentaires inconnus de Google.
Cela vous permettra de créer des images qui n'existent pas encore et de vous approprié l'autorité sur les images que vous allez créer.
Cela vous protégera également juridiquement car vous créer des versions d'image différentes de la version de base.

## Exemple

J'utilise ici [Instaloader](https://instaloader.github.io/) pour récupérer une base d'image pour réaliser mes tests.

#### Installation

```
pip install instaloader 
```

#### Utilisation

```
instaloader nom_du_compte_à_télécharger
```