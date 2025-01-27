import cv2 as cv
img = cv.imread("galaxy.jpg", 1)  #Aqui el 1 indica que la imagen se lee a color

print(type(img))  #Imprimimos el tipo de dato de la imagen
print(img)  #Imprimimos la imagen 
print(img.shape)  #Shape se utiliza para obtener la dimension de la imagen
print(img.ndim)  #ndim se utiliza para obtener el número de dimensiones de la imagen

#Vamos a redimensionar la imagen
# rezised_image = cv.resize(img,(500, 1000))  #El primer valor es de ancho y el segundo de alto 
rezised_image = cv.resize(img,(int(img.shape[1] / 2), int(img.shape[0] /2)))  #Esto indica que el ancho se reduce a la mitad y el alto a la mitad 
#Asi usamos el metodo shape, hay que tener cuidado con los parentesís

cv.imwrite ("Galaxy_resized.jpg", rezised_image)  #imwrite se utiliza para guardar la imagen en un archivo nuevo 

cv.imshow("Galaxy", rezised_image)  #imshow se utiliza para mostrar la imagen en una ventana
cv.waitKey(0)  #waitKey se utiliza para esperar a que el usuario cierre la ventana osea muestra la imagen durante el tiempo que se le indique en milisegundos
#Como lo dejamos en 0, entonces la imagen se cerrará cuando el usuario presione una tecla
cv.destroyAllWindows()  #destroyAllWindows se utiliza para cerrar todas las ventanas que se hayan abierto