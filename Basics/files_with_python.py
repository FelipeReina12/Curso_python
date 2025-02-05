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


# with open("bear.txt") as file:  #abrimos el archivo
#     content = file.read()  #Aqui se almacena el contenido del archivo en la variable content

# with open("first.txt", "w") as file:  #Aqui se crea el archivo
#     file.write(content[:90])  #Se escriben los primeros 90 caracteres del archivo almacenado en la variable content y esos se escriben en el archivo first.txt


with open ("files/fruits.txt", "a+") as my_file:  #Con "a" se puede agregar contenido al archivo en el ultimo lugar
    my_file.write("\nBanana")  #Se escribe el caracter en el archivo y si no existe, se crea el archivo
    my_file.seek(0)  #Se usa seek para mover el cursor del archivo a la posicion 0, es decir, al principio del archivo
    content = my_file.read()
print(content)


#Agregue el texto de oso1.txt a oso2.txt. En otras palabras, oso2.txt debe contener su texto y el texto de oso1.txt después de eso.
with open("bear1.txt") as file:  #Aqui se abre el archivo
    content = file.read()  #Aqui se lee el contenido del archivo y se almacena en la variable content

with open("bear2.txt", "a") as file:  #En esta parte se abre el archivo y se le agrega contenido al final del archivo
    file.write(content)

with open("data.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)


#You can read an existing file with Python:
with open("file.txt") as file:
    content = file.read()


#You can create a new file with Python and write some text on it:
with open("file.txt", "w") as file:
    content = file.write("Sample text")


#You can append text to an existing file without overwriting it:
with open("file.txt", "a") as file:
    content = file.write("More sample text")


#You can both append and read a file with:
with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()