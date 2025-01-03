# my_file = open("fruits.txt")  #Leer el archivo con open("nombre del archivo") en el mismo directorio 
# content = my_file.read()  #.read es para leer el archivo y mostrarlo en pantalla
# my_file.close()  #.close es para cerrar el archivo

#Cuando el archivo no esta en la misma carpeta, se debe poner la ruta del archivo, en este caso files/fruits.txt

# #Otra forma de abrir el archivo es con el método with, que se encarga de cerrar el archivo
# with open("files/fruits.txt", "r") as my_file:  #with es para abrir y cerrar el archivo de archivo de manera automatica "r" es para leer el archivo
#     content = my_file.read()

# print(content)  


# #Otra forma de abrir el archivo es con el método with, que se encarga de cerrar el archivo
# with open("files/vegetables.txt", "w") as my_file:  #Se usa "w" para escribir en el archivo y si no esta creado , lo crea
#     my_file.write("Tomato\nCucumber\nOnion\n")
#     my_file.write("Garlic")

# my_file_2 = open("files/vegetables.txt")
# content = my_file_2.read()
# print(content)  #Se imprime el contenido del archivo


# def foo(character, filepath="bear.txt"):  #Esta funcion recibe un caracter y un archivo por defecto
#     file = open(filepath)  #Abre el archivo
#     content = file.read()  #Lee el archivo almacenado en la variable content
#     return content.count(character)  #Count(character) cuenta cuantas veces aparece el caracter en el archivo y lo devuelve


# with open("file.txt", "w") as file:  #Aqui podemos crear el archivo
#     file.write("snail")  #Esribimos en el archivo
# file = open("file.txt")  #Abrimos el archivo creado
# content = file.read()  #Almacenamos el contenido del archivo en la variable content
# print(content)  #Imprimimos el contenido del archivo


with open("bear.txt") as file:  #abrimos el archivo
    content = file.read()  #Aqui se almacena el contenido del archivo en la variable content

with open("first.txt", "w") as file:  #Aqui se crea el archivo
    file.write(content[:90])  #Se escriben los primeros 90 caracteres del archivo almacenado en la variable content y esos se escriben en el archivo first.txt