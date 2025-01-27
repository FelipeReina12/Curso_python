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

#Otra forma de hacerlo
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv.imread(image,0)
    re=cv.resize(img,(100,100))
    cv.imshow("Hey",re)
    cv.waitKey(500)
    cv.destroyAllWindows()
    cv.imwrite("resized_"+image,re)

