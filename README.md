# LE MORPION
#### par Abraham GAULT

Voici un projet de __morpion__. Le jeu en lui-même a été réalisé pour un projet guidé en cours de __NSI__.
Le système de __score__ a été ajouté à l'occasion d'un autre projet en NSI impliquant un __algorithme de tri__ et des __opérations fichiers__.

## Le fichier main

Ce fichier contient les __4 fonctions__ permettant aux joueurs de *jouer*. 
Le plateau est notamment fait à partir d'une liste de liste contenant des points que les joueurs modifieront en X ou O.

## La classe Profil

La classe Profil est composée de trois méthodes. :  
* La première, selecProfil(), permet au joueur de selectionner son profil préexistant ou d'en créer un nouveau. La fonction retourne une liste afin d'enregistrer les modifications faite à liste dans la méthode et d'appliquer ces modifications à la liste table dans le fichier main. 

* La seconde, victoire(), est appelée lorsque le joueur a gagné. Nous ajoutons donc 1 à son nombre de victoires, son nombre de défaites reste inchangé, son ratio victoire/défaite sera mis à jour et si le joueur n'a jamais perdu son ratio sera égal à son nombre de victoire car on ne peut diviser par zéro. Nous ajoutons également 1 à sa série de victoires

* La dernière défaite

## La fonction stats

L'algorithme derrière la __fonction__ tri est un algorithme de __tri à bulle__ fait à partir de __pseudo-code__ trouvé dans le cours de NSI (le chapitre 9).
Le __choix de l'algorithme__ importe *peu* en raison de la faible taille des __données__.
