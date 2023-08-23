Le script Export_feuille_Excel_mode_paysage.py est le script qui imprime une feuille d'un classeur Excel au format PDF avec les arguments -f et -w.
 - Assurez-vous d'installer ces bibliothèques openpyxl et reportlab en executant la commande suivant dans un terminal : "pip install openpyxl, reportlab"
 - Exécuter le script en exécutant la commande suivant : python Export_feuille_Excel_mode_paysage.py -f "chemin/vers/votre/classeur.xlsx" -w "Nom de la feuille à imprimer"
 - Le résultat sera dans un fichier au même nom que la feuille en format PDF au même endroit que le fichier Excel d'origine.

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Le script Export_feuille_Excel.py est un script que je propose en guise d'alternative pour l'impression d'une feuille Excel en PDF. 
Pour pouvoir utiliser ce script, il faut : 
 - Installer la librairie pywin32 avec la commande suivante sur un terminal : pip install pywin32 , PyPDF2
 - Ouvrir le script et remplacer le champ "Nom de la feuille" par le nom de la feuille qu'e l'on veut imprimer
 - Lancer le script à partir d'un terminal avec : python Export_feuille_Excel.py
 - Saisir le chemin ou se trouve le fichier Excel
 - Le fichier final sortira sous le nom de "output.pdf" dans le répertoire contenant le script
 