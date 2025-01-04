import time  #Importamos el módulo time para poder usar la función sleep

while True:  #Iniciamos un bucle infinito
    with open("files/vegetables.txt") as file:  #Abrimos el archivo en modo lectura
        print(file.read())  #Leemos el contenido del archivo y lo imprimimos por pantalla
        time.sleep(5)  #Esta funcion hace que el programa espere 5 segundos antes de seguir ejecutándose