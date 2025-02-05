my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",
}
"""
Acceder a los elememtos del diccionario
"""
print(my_dict["key1"])  #Esto imprime el valor de "key1"
#Tambien podemos usar el metodo get() para acceder a los elementos del diccionario sin que nos muestre error en caso de no encontrar el elemento
print(my_dict.get("key4"))


"""
Recorrer elementos de un diccionario usando el ciclo for
"""
dict ={
    "Juan": 25,
    "Maria": 30,
    "Pedro": 35,
    "Jhoana ": 20,
}
for key in dict.keys():  #Esto recorre las keys del diccionario
#Siempre se debe poner dict.keys() con paraentesís para que funcione correctamente
    print(key)

#Tambien podemos recorrer los valores del diccionario
for value in dict.values():
    print(value)  #Esto recorre los valores del diccionario

#Asi mismo podemos recorrer tanto las keys como los valores del diccionario
for key, value in dict.items():
    print(f"La key es {key} y el valor es {value}")  #Esto recorre las keys y los valores del diccionario

#Otra forma de hacerlo es recorrer tanto las keys como los valores del diccionario con el metodo items
for i in dict.items():
    print(i)  #Esto recorre las keys y los valores del diccionario


"""
Añadir elementos a un diccionario 
"""
numeros = {
    "Uno": 1,
    "Dos": 2,
    "Tres": 3
}
numeros["Cuatro"] = 4  #Aqui se añade un nuevo elemento al diccionario en la posicion final
numeros["Cinco"] = 5
print(numeros)  #Esto imprime el diccionario con el nuevo elemento


"""
Modiicar elementos de un diccionario 
"""
colores = {
    "Rojo": "Red",
    "Azul": "Blue",
    "Verde": "Green"
}
colores["Rojo"] = "Rojo"  #Aqui se modifica el valor
colores["Azul"] = "Azul"
colores["Verde"] = "Verde"
print(colores)


"""
Eliminar elementos de un diccionario
"""
frutas = {
    "Manzana": "Apple",
    "Platano": "Banana",
    "Naranja": "Orange",
    "Piña": "Pineapple",
    "Fresa": "Strawberry",
    "Uva": "Grapes"
}
frutas.pop("Manzana")  #Pop elimina una key y su valor del diccionario
frutas.pop("Platano")
print(frutas)


"""
Numero de elementos en un diccionario
"""
consolas = {
    "PlayStation": "PS5",
    "Xbox": "Xbox Series X",
    "Nintendo": "Nintendo Switch"
}
print(len(consolas))


"""
Comprobar si un elemento esta en un diccionario
"""
juegos = {
    "Clash of clans": "CoC",
    "Clash royale": "CR",
    "PUBG": "PlayerUnknown's Battlegrounds",
    "Fortnite": "Fortnite Battle Royale",
}
print("Clash of clans" in juegos)  # Si Clash of clans esta en juegos, devuelve True, si no devuelve False

#Verificar si un elemento esta y eliminarlo con del
if "Clash of clans" in juegos:  #Si Clash of clans esta en juegos
    del juegos["Clash of clans"]  #Elimina Clash of clans de juegos
print(juegos)


"""
Obtener una lista con las claves de un diccionario 
"""
instrumentos = {
    "Guitarra": "Fender",
    "Bajo": "Fender",
    "Bateria": "Pearl",
    "Piano": "Yamaha",
    "Teclado": "Yamaha"
}
print(list(instrumentos.keys()))  #Imprime una lista con las claves del diccionario instrumentos
print(list(instrumentos.values()))  #Imprime una lista con los valores del diccionario instrumentos