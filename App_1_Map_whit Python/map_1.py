import folium as flm
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
# print(data)
lat = list(data["LAT"])  #Agregamos las latitudes a una lista
lon = list(data["LON"])  #Agregamos las longitudes a una lista
name = list(data["NAME"])  #Agregamos los nombres a una lista
loc = list(data["LOCATION"])  #Agregamos las ubicaciones a una lista
type = list(data["TYPE"])  #Agregamos el tipo de volcanes a una lista
elev = list(data["ELEV"])  #Agregamos las elevaciones a una lista

#Creamos el mapa, le damos una ubicacion inicial, un zoom y un titulo
map = flm.Map(location= [17.728806417081415, -43.23802464428199] , zoom_start= 3, titles = "Stamen Terrain" )


volcanes = flm.FeatureGroup(name= "Volcanes") #Creamos una capa para los volcanes
elevaciones = flm.FeatureGroup(name= "Elevaciones") #Creamos una capa para las elevaciones
type_volcan = flm.FeatureGroup(name= "Tipo de volcanes") #Creamos una capa para el tipo de volcanes
loacalitation = flm.FeatureGroup(name= "Ubicación")  #Creamos una capa para las ubicaciones

#Recorremos la lista de volcanes y los agregamos a la capa
for lt, ln, na in zip(lat, lon, name):
    volcanes.add_child(flm.Marker(location=[lt, ln],
    popup=str(na),icon=flm.Icon(color='green')))

for lt, ln, el in zip(lat, lon, elev):
    elevaciones.add_child(flm.CircleMarker(location=[lt, ln],
    radius= 7, popup= str(el) + "m", fill_color = "blue", color= "white", fill_opacity= 0.5))

for lt, ln, tp in zip(lat, lon , type):
    type_volcan.add_child(flm.CircleMarker(location=[lt, ln],
    radius= 7, popup= str(tp), fill_color= "orange", color= "white", fill_opacity= 0.5 ))

for lt, ln, locat in zip(lat, lon, loc):
    loacalitation.add_child(flm.Marker(location=[lt, ln],
    popup=str(locat),icon=flm.Icon(color='red')))



map.add_child(loacalitation)
map.add_child(volcanes)
map.add_child(elevaciones)
map.add_child(type_volcan)
map.add_child(flm.LayerControl())
map.save("map_1.html")