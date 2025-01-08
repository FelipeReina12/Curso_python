"""
Repaso de listas en Python
"""
#Append en python se usa para agregar elementos a una lista
lista = [1, 2, 3, 4, 5]
lista.append(6)  #Aqui añadimos el elemento 6 a la lista en la ultima posición 
#Esto no se puede poner directamente en un print 
print(lista)


#Remove se usa para eliminar elementos de una lista
lista_1 = [1, 2, 3, 4, 5]
lista_1.remove(3)  #Aqui eliminamos el elemento 3 de la lista
print(lista_1)


#Inserte se usa para insertar elementos en una lista en una posición específica
lista_7 = [1, 2, 3, 4, 5]
lista_7.insert(2, 6)  #Aqui insertamos el elemento 6 en la poscición 2
print(lista_7)


#Acceder a un elemento de una lista
lista_2 = [1, 3, 5, 7, 9, "h", "o", "l", "a"]
print(lista_2[3])  #Accedemos al elemento en la posición 3 de la lista 
print(lista_2[-1])  #Accedemos al último elemento de la lista
print(lista_2[2:3])  #Accedemos a los elementos entre la posición 2 y 3 -1 de la lista
print(lista_2[2:4])  #Accedemos a los elementos entre la posición 2 y 4 -1 de la lista
print(lista_2[:])  #Todos los elementos de la lista 
print(lista_2[1:])  #Todos los elementos de la lista a partir de la posición 1
print(lista_2[:-3])  #Accedemos desde los primeros elementos de la lista hasta la posición 4
print(lista_2[1:5])  #Accedemos a los elementos entre la posición 1 y 5 -1 de la lista
print(lista_2[5:8])
print(lista_2[-4: -2])  #Accedemos a los elementos entre la posición -4 y -2-1 de la lista
print(lista_2[::2])  #Accedemos a todos los elementos de la lista con un paso de 2
print(lista_2[1:6:2])  #Accedemos a los elemento desde la posición 1 hatsa la 6 con un paso de 2

"""
Importante: Los índices de las listas en Python comienzan en 0
Tambien cuando vamos a acceder a unos elementos de una lista, cuando tenemos [2:7] significa que va desde el elemento en la posición 2 hasta la posisción 6
Cunado tenemos [1:-8] significa que va desde el elemento en la posicíon 1 hasta la posicion 7 (Esto con los numeros negativos)
Ahora cuando tenemos [1:5] significa que va desde el elemento en la posición 1 hasta la posición 4 contando el 1 y el 4

En conclusón, cuando tomamos un rango de elementos, estos siempre cuentan desde la poscicion que enviemos primero y la segunda poscicion cuenta un elemento menos 
"""


#Sort y reverse
lista_3 = [5, 2, 8, 1, 9, 4, 7, 6, 3]
lista_3.sort()
print(lista_3)  #La lista se ordena de menor a mayor
lista_3.reverse()
print(lista_3)  #La lista se ordena de mayor a menor


#Count
lista_4 = [1, 2, 3, 4, 5]
print(lista_4.count(2))  #Count se usa para contar cuantos elementos de una lista son iguales a un elemento determinado


#Len
lista_5 = [1, 2, 3, 4, 5]
print(len(lista_5))  #Len se usa para saber cuantos elementos tiene una lista


#Repeating
lista_6 = [1, 2, 3, 4, 5] * 3
print(lista_6)  #Repeating se usa para repetir una lista un número determinado de veces


"""
Recorrer una lista con un ciclo For
"""
colores = ["rojo", "verde", "azul", "amarillo", "negro"]
for color in colores:
    print(color)  #Recorremos la lista y mostramos cada elemento de la lista


"""
Buscar un elemento en la lista 
"""
lista_8 = [1, 2, 3, 4, 5]
if 2 in lista_8:
    print("Si está en la lista")
else:
    print("No está en la lista")  #Buscar un elemento en la lista con el oper