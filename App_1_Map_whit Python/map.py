import folium  #Esta libreia es para crear mapas interactivos
import pandas


data = pandas.read_csv("Volcanoes.txt")  #Importamos los datos del archivo csv
lat = list(data["LAT"])  #Asignamos una variable a la columna de latitudes
lon = list(data["LON"])  #Asignamos una variable a la columna de longitudes
elev = list(data["ELEV"])
  

def color_producer(elevation):
        if elevation > 0 and elevation < 1000:
            return "green"
        elif elevation >= 1000 and elevation < 2000:
               return "orange"
        else:
               return "red"
         

map = folium.Map(location = [17.728806417081415, -43.23802464428199], zoom_start= 3, titles = "Stamen Terrain")  #Alamcenamos la ubicacion del mapa


fgv = folium.FeatureGroup(name = "Volcanoes")
for lt, ln, el in zip(lat, lon, elev):  #Zip se usa para combinar dos o mas listas, los empareja en una tupla
        fgv.add_child(folium.CircleMarker(location = [lt, ln], raius= 7, popup= str(el) + "m",  #Agregamos un marcador al mapa
        fill_color = color_producer(el), color = "grey", fill_opacity = 0.7))


fgv.add_child(folium.CircleMarker(location = [5.082452032134559, -73.60729527912444],
raidus = 1, popup= "House", fill_color = "green", color = "grey", fill_opacity = 0.7)) 


fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data= open("world.json", "r", encoding= "utf-8-sig").read(),  #Abrimos y leemos el archivo json que tiene los datos de los países
style_function= lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000  #Agregamos la función lambda para colorear los países
else "orange" if 1000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map.html")  #Lo guardamos en un archivo html 