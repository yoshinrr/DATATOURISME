IMPORTANT :
Vous devez d'abord télécharger les données sur le site https://diffuseur.datatourisme.gouv.fr/
Pour ce faire, il vous faudra ouvrir un compte, créer un flux et télécharger ce flux. 

L'utilisation de ce logiciel nécessite que les données que vous avez téléchargées soient en fichier JSON. 
Le dossier téléchargé se présente généralement en fichier zip qu'il vous faudra extraire. 
Un dossier du nom de "flux-suite de numéro", en résultera. Dans ce dossier se trouve différents sous dossiers dont le sous dossier "objects" qui
nous intéresse particulièrement car, y sont contenues les données à extraire.

Les données qui seront extraites seront :
le nom de l'entreprise, son numéro de téléphone, son email, sa catégorie, le lien vers l'image qui lui est associée, son adresse, son deépartement, sa description,
son site internet, son numéro de commune

A quoi sert ce logiciel ? 

Ce logiciel permet de d'extraire certaines données présentes dans le dossier "flux-suite de numéro" dans un fichier csv 
que vous pourrez lire sur excel (tutoriel pour lire un fichier csv sur excel https://fr.wikihow.com/ouvrir-un-fichier-CSV). 
Vous pourrez aussi convertir le fichier csv sur un site de conversion comme https://convertio.co/fr/csv-xls/.

Mode d'emploi

Dans chemin des fichiers, choisissez l'endroit où vous avez extrait le flux et chemin à l'intérieur du dossier "objects". 
Ce qui devrait être inscrit sur l'entrée chemin de fichier, si vous avez par exemple extrait le fichier zip sur le bureau sera : 
C:/Users/votrenom/OneDrive/Bureau/flux-9185-202101190156/objects
en ce qui concerne mon ordinateur. 

En dessous vous aurez à choisir l'endroit où vous souhaitez sauvegarder le fichier. Vous devrez par contre entrer le nom du fichier 
manuellement précédé d'un /. 
Ce qui devrait s'afficher dans chemin de sauvegarde du fichier csv sera C:/Users/votrenom/OndeDrive/Bureau vous voulez sauvegarder 
sur le bureau. Ajoutez manuellement /nomdufichier.csv pour choisir le nom du fichier. 
Ainsi, vous aurez ceci sur Chemin de sauvegarde du fichier csv si vous avez choisi extraction comme nom de fichier:
C:/Users/moi/OndeDrive/Bureau/extraction.csv

Pour extraire les données, appuyez sur extraire. Un popup vous avertira quand l'extraction sera terminée. 
Selon la taille du fichier, la puissance de votre ordinateur, le temps de traitement peut considérablement varier (jusqu'à 30 mn parfois).
Le bouton extraire restera enfoncé le temps de l'extraction. 
