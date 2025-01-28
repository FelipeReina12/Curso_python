import cv2 as cv, time 

video = cv.VideoCapture(0)  #Aqui podemos poner el nombre de un archivo de video o 0 para la cámara que nuestro ordenador tiene por defecto
a = 0

while True:
    a = a + 1

    check, frame = video.read()  #Check y frame son variables que se crean para almacenar la información de la imagen

    print(check)
    print(frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  #Convertimos la imagen a escala de grises
    # time.sleep(2)  #Aqui podemos poner el tiempo que queramos que dure la ejecución del programa
    cv.imshow("Capturing", gray)
    
    key = cv.waitKey(1)  #En la variable key se almacena la tecla que cuando se pulse hará que se detenga la ejecución del programa
    if key == ord("q"):  #ord () es una función que nos permite convertir un caracter en un número
        break  #La tecla q rompera el loop y el programa se detendrá
print(a)
video.release()  #En esta parte se cierra la cámara o el archivo de video que se estaba leyendo
cv.destroyAllWindows()  #En esta parte se cierran todas las ventanas que se han abierto