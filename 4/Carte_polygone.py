import folium
import geojson
import matplotlib.pyplot as plt
import webbrowser
import json

# Coordonnées géographiques des points sous forme de liste de tuples
points1 = [
    (-18.779688, 48.988831),
    (-18.77979, 48.954928),
    (-18.802379, 48.941925),
    (-18.815744, 48.938878),
    (-18.865916, 48.961772),
    (-18.877032, 49.054663),
    (-18.863348, 49.0646),
    (-18.820859, 49.069484)
 
]

points2 = [
        (-11.959261, 49.258062),
        (-12.411231, 48.748312),
        (-13.586976, 47.886391),
        (-14.678406, 47.453221),
		(-16.181331, 44.467457),
		(-17.486246, 43.929380),
		(-19.967902, 44.479226),
		(-21.318934, 43.506645),
        (-22.243263, 43.228708),
        (-22.839073, 43.385624),
		(-24.370979, 43.678085),
		(-25.051437, 44.105064),
		(-25.577100, 45.189491),
		(-25.553470, 45.511293),
        (-25.165287, 46.686799),
        (-24.966473, 47.097561),
		(-23.786216, 47.573825),
		(-18.142213, 49.401813),
        (-16.893635, 49.941527),
		(-15.274859, 50.460820),
		(-13.057403, 49.897307),
		(-11.959261, 49.258062)

]

# Créer une carte centrée sur Brickaville, Antsinanana
m = folium.Map(location=(-18.820859, 49.069484), zoom_start=12)

# Ajouter le polygone avec les coordonnées
folium.Polygon(locations=points1, color='red', fill=True, fill_color='b').add_to(m)
folium.Polygon(locations=points2, color='blue', fill=True, fill_color='b').add_to(m)

#webbrowser.open('https://www.bing.com/maps?cp=-18.819531%7E49.071049&lvl=17.3&style=h')

# Enregistrer/ouvrir la carte au format HTML
carte = 'carte_avec_polygon.html'
m.save(carte)
webbrowser.open(carte)

print("La carte a été enregistrée sous le nom 'map_with_polygon.html'")