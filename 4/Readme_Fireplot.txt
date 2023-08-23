Dans ce Challenge, il est important d'installer les bibliothèques requises en exécutant ces commandes suivant dans un terminal :
	pip install matplotlib
	pip install geojson
	pip install argparse 
	pip install shapely
	pip install random
	
NB :
 - Le fichier "Brickaville.geojson" contient les Coordonnées d'un polygone autout de Brickaville
 - Le fichier "Madagascar.geojson" contient les Coordonnées du polygone de Madgascar
 - Le fichier "switzerland.geojson" est un fichier de test pour vérifier l'appartenance du polygone à celui de Madagascar
 - Le programme "Carte_polygone.py" génèrera une page nommé "carte_avec_polygon.html" contenant les polygone de Madagascar(en bleue) et celui de Brickaville (en rouge)
 
+ Suite à l'installation des dépendances, vous pouvez exécuter le script "Fireplot.py" comme suit :
	python Fireplot.py -p "Chemin/vers/le/fichier/Nom.geojson"
+ Le programme "Fireplot.py" génèrera un chart de la time séries du nombre de départ de feux par an dans la zone défini depuis 1993 à 2023(les données ont été généré de façon aléatoire entre 0 à 200).
 