import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")  #Aqui lo que hacemos es cargar el archivo xml que contiene el clasificador de caras
cap = cv.VideoCapture(0)  #Inicializamos la camara de la pc

while True:
    _, img = cap.read()  #_, es para ignorar el valor de retorno de la funcion read
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #Convertimos la imagen a escala de grises
    faces = face_cascade.detectMultiScale(gray, 1.1, minNeighbors=5, 
        minSize=(35, 35)) #MInSize es el tamaño minimo de la cara que queremos detectar

    for (x, y , w, h) in faces:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow("Img", img)
    k = cv.waitKey(30)  #Metodo para verificar si se presiona una tecla
    if k == 27:  #27 es el codigo ASCII de la tecla ESC
        break
cap.release()  #Comando para dejar de usar la camara
