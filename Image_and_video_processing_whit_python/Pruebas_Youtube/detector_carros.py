import cv2 as cv

cars_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")  #Aqui lo que hacemos es cargar el archivo xml que contiene el clasificador de carros
cap = cv.VideoCapture("El ruido - Carretera.mp4")

while True:
    _, img = cap.read()  #_, es para ignorar el valor de retorno de la funcion read
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #Convertimos la imagen a escala de grises
    cars = cars_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w, h) in cars:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow("Img", img)
    k = cv.waitKey(30)  #Metodo para verificar si se presiona una tecla
    if k == 27:  #27 es el codigo ASCII de la tecla ESC
        break
cap.release()  #Comando para dejar de usar la camara
