# def saludo():
#     return "Hola, un saludo"
# print(saludo())  # imprime "Hola, un saludo" en la consola


# def otro_saludo(name):
#     return f"Hola, {name}"
# name = "Juan"
# print(otro_saludo(name))  # imprime "Hola, Juan" en la consola


# def factorial(num):
#     temp = 1
#     for i in range(num):
#         temp *= i +1
#     return temp
# print(factorial(24))


# def iva(valor):
#     return valor + (valor * 0.21)
# print(iva(1000))


# def area_circulo(radio, pi = 3.1416):  #Función para hallar el area de un circulo
#     area = pi * (radio ** 2)  #Operacion para calcular el area
#     return area
# def area_cilindro(radio, altura):  #Aqui usamos la funcion anterior para calcular el area de un cilindro
#     return area_circulo(radio) * altura  #Invocamos la funcion anterior y multiplicamos por la altura
# print(area_cilindro(4, 5))  #Le damos los parametros que son el radio y la altura


# def mean(list):
#     return round(sum(list) / len(list),2)  #Para redondear a dos decimales se pine el round primero y luego el sum y el len
# list = [50, 35, 45]
# print(mean(list))


# list = [5, 4, 6, 7, 8]
# def cuadrados_lista(list):
#     list_new = []  #Agregamos una lista vacia para que no se pierda la referencia a la lista original
#     for i in list: #Recorremos la lista original
#         list_new.append(i ** 2)  #Aqui multiplicamos cada elemento por 2 y lo agregamos a la nueva lista
#     return list_new
# print(cuadrados_lista(list))

 
def square(sample):
    list = []
    for i in sample:
        list.append(i**2)
    return list
def stadistics(sample):
    dic = {}
    dic["Media"] = sum(sample) / len(sample)
    dic["Varianza"] = sum(square(sample)) / len(sample) - dic["Media"] ** 2
    dic["Desviacion tipica"] = round(dic["Varianza"] ** 0.5, 2)
    return dic
print(stadistics([1,2,3,4,5]))


def mcd(n, m):
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n
def mcm(n, m):
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))
