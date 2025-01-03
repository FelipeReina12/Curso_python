# temps = [221, 234, 340, 230]  #Tenemos nuestra lista
# new_temps = []  #Creamos una nueva lista vacía
# for temp in temps:  #Esto se usa para recorrer cada elemento en la lista osea temp recorre cada elemento
#     new_temps.append(temp /10)  #Usamos nuestra lista vacia para agregar los elementos de la lista original pero divididos por 10
# print(new_temps)
#Otra forma de hacerlo es mediante list comprehension
# temps = [221, 234, 340, 230] 
# new_temps = [temp / 10 for temp in temps] #Esto significa que para cada elemento en la lista original, lo dividimos por 10 y lo agregamos a la nueva lista 
#Es como decir una variable va a recorrer la lista y la va a dividir en 10 y lo va a agregar a la nueva lista y luego la llamamos para que recorra en la lista original
# print(new_temps)  #Esto es lo mismo que el for pero en una sola línea


# temps = [221, 234, 340, 230, -999, -455] 
# new_temps = [temp / 10 for temp in temps if temp > 0]  #Esto se hace para que solo se divida por 10 los números positivos
# print(new_temps)


# def foo(list):
#     return [i for i in list if  isinstance(i, int)]  #isinstance es para saber si es un número entero
# list = [99, 'no data', 95, 94, 'no data']
# print(foo(list))  #Esto es para que solo se muestren los números enteros


# def foo(list_2):  #Definimos la función 
#     return [i for i in list_2 if i > 0]  #Retornamos una lista con los números mayores a 0
# list_2 = [-5, 3, -1, 101]
# print(foo(list_2))


# temps =[221, 234, 340, -999, 230]
# new_temps = [temp / 10 if temp != -999 else 0 for temp in temps]  #Esta linea hace lo mismo que el for pero en una sola línea y si encuentra un -999 lo reemplaza por 0
# #Se debe poner primero el else y luego se agrega el for para que se cumpla la condición de que si encuentra un -999 lo reemplaza por 0
# print(new_temps)


# def foo(list_3):
#      return [i if not isinstance(i, str) else 0 for i in list_3 ]  #Tomamos el parametro i y si no es una cadena de texto lo dejamos como está, si es una cadena de texto lo reemplazamos por 0 con el else
# list_3 = [99, 'no data', 95, 94, 'no data']
# print(foo(list_3))  


def foo(list_4):
     return sum([float(i) for i in list_4])  #Usamos la funcion sum para sumar todos los elementos de la lista y convertimos cada elemento a float para que se puedan sumar entre si
list_4 = ['1.2', '2.6', '3.3']
print(foo(list_4))


#Cheatsheet: List Comprehensions
#Basic
list_5 = [i * 2 for i in [1, 5, 10]]  #Multiplica por 2 cada elemento de la lista
print(list_5)


#With if condition 
list_6 = [i * 2 for i in [4, 5, 6, 2] if i > 5]  #Multiplica por 2 cada elemento de la lista pero solo si es mayor a 5
print(list_6)


#With if and else 
list_7 = [i *2  if i >2 else 0 for i in [2, 4, 1, 3, 5]]  #Multiplica por 2 cada elemento de la lista pero si es menor a 2 lo reemplaza por 0
print(list_7)