import cv2 as cv

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")  #Aqui importamos el archivo xml que contiene las características de los rostros
img = cv.imread("photo.jpg")  #Leemos la imagen que contiene el rostro
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  #Aqui convertimos la imagen a escala de grises 

faces = face_cascade.detectMultiScale(gray_img, 
scaleFactor= 1.05,  #Aqui configuramos el factor de escalado para detectar los rostros el 1.05 indica que se detectara el rostro en escalas de 1.05 veces la escala original
minNeighbors= 5)  #Aqui detectamos los rostros en la imagen el numero 5 indica que se detectara el rostro cuando tenga al menos 5 vecinos cercanos, esto ayuda a evitar falsos positivos

for x, y, w, h in faces:
    img = cv.rectangle(img, (x,y),  #Aqui dibujamos un rectángulo en la imagen que contiene el rostro
    (x + w, y + h),  #El primer par de coordenadas (x,y) es el punto superior izquierdo del rectángulo (x + w, y + h) es el punto inferior derecho del rectángulo
    (0, 255, 0), 3)  #El tercer par de coordenadas (0, 255, 0), 3 indica que el rectángulo será verde y tendrá un grosor de 3 pixeles

print(faces)  #Imprimimos las coordenadas de los rostros detectados
print(type(faces))  #Imprimimos el tipo de dato de los rostros detectados en la imagen

resized = cv.resize(img,(int(img.shape[1] / 2), int(img.shape[0] /2)))  #Aqui redimensionamos la imagen a la mitad del tamaño original

cv.imshow("Imagen 1", resized)  #Mostramos la imagen con el rectangulo verde que detecta la cara
cv.waitKey(0)
cv.destroyAllWindows()

#Leemos la otra imagen para detectar rostros
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")  #Aqui importamos el archivo xml que contiene las características de los rostros
img_2 = cv.imread("news.jpg")
gray_img_2 = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)

faces_2 = face_cascade.detectMultiScale(gray_img_2, 
scaleFactor= 1.1, 
minNeighbors= 3,
minSize= (30, 30))  #minSize es el tamaño mínimo que debe tener el rostro para ser detectado

for x, y, w, h in faces_2:
    img = cv.rectangle(img_2, (x,y),  
    (x + w, y + h),
    (0, 255, 0), 3) 

print(faces_2)  
print(type(faces_2))
resized_2 = cv.resize(img_2,(int(img_2.shape[1] / 2), int(img_2.shape[0] /2)))  #Aqui redimensionamos la imagen a la mitad del tamaño original

cv.imshow("Imagen 2", resized_2)  #Mostramos la imagen con el rectangulo verde que detecta la cara
cv.waitKey(0)
cv.destroyAllWindows()