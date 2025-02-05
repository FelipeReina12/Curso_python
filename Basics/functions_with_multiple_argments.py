# def area(a, b):
#     return a * b

# print(area(4, 5))

# def foo(c, d):
#     return c + d

# print(foo("c", "d"))


# def foo(*args):  #*args es un parámetro que recibe cualquier número de argumentos
#     return sum(args) / len(args)  #aqui se calcula la media de los argumentos que es la suma sobre el número de argumentos
# print(foo(10, 20, 30, 40))


# def foo(*args):
#     args = [i.upper() for i in args]  #Aqui se convierte a mayúscula cada uno de los argumentos
#     return sorted(args)  #Sorted se usa para ordenar los argumentos de manera ascendente
# print(foo("snow", "glacier", "iceberg"))


# def mean_2(**kwargs):  #Kwwards es un parámetro que recibe argumentos con nombre y valor como un diccionario
#     return kwargs
# print(mean_2(a = 1, b = 2, c = 3))  #Por eso devuelve un diccionario con los argumentos que se le pasaron


# def find_sum(**kwargs):
#     return sum(kwargs.values())  #Devuelve la suma de las values de los argumentos que se lepasaremos sin importar cauntos hay ni el nombre
    
# print(find_sum(a = 1, b = 2, c = 4, d = 2))


# # Las funciones pueden tener más de un parámetro
# def volume(a, b, c):
#     return a * b * c
# print(volume(2, 3, 4))


# # Las funciones pueden tener parámetros predeterminados
# def converter(feet, cohefficient = 3.2808):
#     meters = feet / cohefficient
#     return meters
# print(converter(10))  #10 es el valor de feet y 3.2808 es el valor de cohefficient que ya está definido en la función


# # Los argumentos se pueden pasar como argumentos que no son palabras clave (posicionales) (por ejemplo, a) o como argumentos de palabras clave.
# def foo(a, b, c):
#     return a + b + c
# print(foo(1, b = 2, c = 3))  #Aqui se le pasan los argumentos que uno quiera con el nombre que uno quiera


# Un parámetro *args permite llamar a la función con un número arbitrario de argumentos que no son palabras clave
def find_max(*args):  #Aqui se define una función que recibe un número indefinido de argumentos 
    return max(args)  #Retornamos max para encontrar el número mayor de los argumentos que pasaremos
print(find_max(1, 5, 8, 24))


# Un parámetro **kwargs permite llamar a la función con un número arbitrario de argumentos de palabras clave:
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)  #kwargs.get es una función que devuelve el valor de un argumento de palabras clave
print(find_winner(andy = 10, bob = 40, charlie = 30))  #Aqui se le pasan las keys y sus values a la función para saber cual es el ganador 
