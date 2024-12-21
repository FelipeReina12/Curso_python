students = {
    "Marry": 9.1,
    "Sim": 8.4,
    "John": 7.8
}
print(students["John"])  #Buscamos la key "John" y nos devuelve el valor asociado a esa key

#Conversion de una tupla a una lista
cool_tuple = (1, 3, 4,)
cool_list = list(cool_tuple)  #Convertimos la tupla a una lista
print(cool_list)  

#Convertir una lista en una tupla 
other_list = [4, 2, "Hello", 1.0]
other_tuple = tuple(other_list)  #Convertimos la lista a una tupla
print(other_tuple)

#Convertir un str en una lista 
my_str = "Zetawise"
my_list = list(my_str)  #Convertimos el str en una lista
print(my_list)  

#Convertir una lista en un str
my_new_list = ["Z", "E", "T", "A", "W", "I", "S", "E"]
my_new_str = str.join("", my_new_list)  #Convertimos la lista en un str
print(my_new_str)

data = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
}
print(data["b"][2])  #Siempre se escribe el nombre del diccionario para imprirlo 
