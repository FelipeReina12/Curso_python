import time  #Importamos el módulo time para poder usar la función sleep
import os
import pandas


# while True:  #Iniciamos un bucle infinito
#     if os.path.exists("files/vegetables.txt"):
#         with open("files/vegetables.txt") as file:  #Abrimos el archivo en modo lectura
#             print(file.read())  #Leemos el contenido del archivo y lo imprimimos por pantalla
#     else:
#         print("El archivo no existe")  #Si el archivo no existe, imprimimos est
#     time.sleep(5)  #Esta funcion hace que el programa espere 5 segundos antes de seguir ejecutándose    


while True:
    if os.path.exists("files/temps_today.csv"):
        data = pandas.read_csv("files/temps_today.csv")  #Abrimos el csv, lo leemos y lo almacenams en la variable data
        print(data.mean()["st1"])  #Imprimimos el contenido del csv por pantalla
        print(data.mean()["st2"])
    else:
        print("El archivo no existe")  #Si el archivo no existe, imprimimos est
    time.sleep(15)  #Esta funcion hace que el programa espere 5 segundos antes de seguir ejecutándose    