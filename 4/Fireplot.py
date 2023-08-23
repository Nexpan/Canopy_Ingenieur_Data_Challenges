import argparse
import geojson
import matplotlib.pyplot as plt
#from geojson import Polygon 
from shapely.geometry import shape, Point
import random

#Générer des données 
def generate_mock_data(years):
    return {str(year): random.randint(0, 200) for year in years}

#Charger le fichier Geojson
def parse_geojson_file(file_path):
    with open(file_path, 'r') as file:
        data = geojson.load(file)
        return data['features'][0]['geometry']['coordinates']

#Création du visuel 
def plot_fire_timeseries(data):
    years = sorted(list(data.keys()))
    values = [data[year] for year in years]

    #Informations sur le visuel
    plt.figure(figsize=(10, 6))
    plt.plot(years, values, marker='o')
    plt.title('Incendies Timeserie')
    plt.xlabel('Années')
    plt.ylabel('Nombre(s) d\'incendie(s)')
    plt.grid(True)
    plt.show()
          

def main():
    # Charger le fichier GeoJSON de Madagascar
    with open('Madagascar.geojson', 'r') as geojson_file:
        madagascar_geojson = geojson.load(geojson_file)

    # Créer un objet de polygone à partir du GeoJSON de Madagascar
    madagascar_polygon = shape(madagascar_geojson['features'][0]['geometry'])

    #Création de l'argument -p
    parser = argparse.ArgumentParser(description='Generer une timeseries des incendies qui se sont produits')
    parser.add_argument('-p', '--polygon', required=True, help='Chemin vers le fichier GeoJSON')
    args = parser.parse_args()
    
    # Accédez à la valeur de l'argument "p" en utilisant args.parametre
    if args.polygon:
        valeur_de_p = args.polygon
        # Charger le fichier GeoJSON avec le polygone à vérifier
        with open(valeur_de_p, 'r') as geojson_file:
            fichier_polygone = geojson.load(geojson_file)
        # Créer un objet de polygone à partir du GeoJSON du polygone à vérifier
        polygone = shape(fichier_polygone['features'][0]['geometry'])
    else:
        print("Le fichier Goejson {valeur_de_p} spécifié est introuvable.")

    # Vérifier si le polygone est inclus dans Madagascar
    if madagascar_polygon.contains(polygone):
        print("Le polygone séléctionnée est inclus dans Madagascar.")
        # Générer des chiffres aléatoires pour chaque année entre 1993 et 2023
        years = list(range(1993, 2023))  
        mock_data = generate_mock_data(years)

        plot_fire_timeseries(mock_data)
    
    else:
        print("Le polygone séléctionné n'est pas inclus dans Madagascar.")
  
if __name__ == '__main__':
    main()

    