import cv2 as cv 

first_frame = None  #Creamos una variable para almacenar la primera imagen

video = cv.VideoCapture(0)  #Aqui podemos poner el nombre de un archivo de video o 0 para la cámara que nuestro ordenador tiene por defecto

while True:

    check, frame = video.read()  #Check y frame son variables que se crean para almacenar la información de la imagen
    status = 0 #Creamos una variable para almacenar el estado de la imagen
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  #Convertimos la imagen a escala de grises
    gray = cv.GaussianBlur(gray, (21, 21), 0)  #GaussianBlur es para que la imagen no tenga tanto ruido

    if first_frame is None:  #Si la primera imagen no ha sido creada
        first_frame = gray  #Entonces la primera imagen es la imagen actual
        continue  #Continue significa que pasamos a la siguiente iteración del bucle, es decir , a la siguiente imagen

    delta_frame = cv.absdiff(first_frame, gray)  #Aqui lo que hacemos es que la primera imagen se resta de la imagen actual y obtenemos la diferencia entre ambas
    thresh_frame = cv.threshold(delta_frame, 30, 255, cv.THRESH_BINARY)[1]
    thresh_frame = cv.dilate(thresh_frame, None, iterations= 2)

    (cnts, _) = cv.findContours(thresh_frame.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv.contourArea(contour) < 1000:
            continue
        status = 1  
        (x, y, w, h) = cv.boundingRect(contour)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv.imshow("Gray frame", gray)
    cv.imshow("Delta Frame", delta_frame)  #Aqui mostramos la imagen actual y la diferencia entre la primera imagen y la imagen actual
    cv.imshow("Threshold frame", thresh_frame)
    cv.imshow("Color frame", frame)
    
    key = cv.waitKey(1)  #En la variable key se almacena la tecla que cuando se pulse hará que se detenga la ejecución del programa
    
    if key == ord("q"):  #ord () es una función que nos permite convertir un caracter en un número
        break  #La tecla q rompera el loop y el programa se detendrá
    print(status)
    

video.release()  #En esta parte se cierra la cámara o el archivo de video que se estaba leyendo
cv.destroyAllWindows()  #En esta parte se cierran todas las ventanas que se han abierto


