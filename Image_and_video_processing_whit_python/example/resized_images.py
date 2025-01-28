import cv2 as cv
#Función para leer la imagen y redimensionarla 
def resize_image(imagen):
    rezised_image = cv.resize(imagen,(int(imagen.shape[1] / 2), int(imagen.shape[0] /2)))
    return rezised_image

cv.imshow("Img_1", resize_image(cv.imread('galaxy.jpg', 1)))
cv.waitKey(0)
cv.imwrite ("Galaxy_resized.jpg", resize_image(cv.imread('galaxy.jpg', 1)))

cv.imshow("Img_2", resize_image(cv.imread("kangaroos-rain-australia_71370_990x742.jpg", 1)))
cv.waitKey(0)
cv.imwrite ("Kangaroo_resized.jpg", resize_image(cv.imread("kangaroos-rain-australia_71370_990x742.jpg", 1)))

cv.imshow("Img_3", resize_image(cv.imread("Lighthouse.jpg", 1)))
cv.waitKey(0)
cv.imwrite ("Lighthouse_resized.jpg", resize_image(cv.imread("Lighthouse.jpg", 1)))

cv.imshow("Img_4", resize_image(cv.imread("Moon sinking, sun rising.jpg", 1)))
cv.waitKey(0)
cv.imwrite ("Moon_sinking_sun rising_resized.jpg", resize_image(cv.imread("Moon sinking, sun rising.jpg", 1)))
cv.destroyAllWindows() 


#Otra forma de hacerlo es con un loop for
import glob
# Obtiene una lista de todos los archivos .jpg en el directorio actual
images = glob.glob("*.jpg")

# Itera sobre cada imagen en la lista de imágenes
for image in images:
    img = cv.imread(image, 0)  #Lee la imagen en escala de grises
    re = cv.resize(img, (100, 100))  #Redimensiona la imagen a 100x100 píxeles
    cv.imshow("Hey", re)  #Muestra la imagen redimensionada en una ventana
    cv.waitKey(500)  #Espera 500 milisegundos antes de cerrar la ventana
    cv.destroyAllWindows()  #Cierra todas las ventanas abiertas
    cv.imwrite("resized_" + image, re)  #Guarda la imagen redimensionada con un nuevo nombre

