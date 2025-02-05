# print("Hola mundo")


# saludo = "Hola mundo"
# print(saludo)


# name = input("Enter your name: ")
# print("Hello,", name)


# x = ((3 +2) / 2.5) ** 2
# print(x)


# def work(hours, pay):
#     return hours * pay
# hours = int(input("Enter the number of hours:  "))
# pay = int(input("Enter the pay per hour:  "))

# print("Your salary is: ", work(hours, pay))


# def suma(num):
#     out = num * ((num + 1) / 2)
#     return out
# num = int(input("Enter a number: "))
# print(suma(num))


# def imc(peso, estatura):
#     var = round((peso)/(estatura)** 2, 2)  #Para redondear a 2 decimales
#     return var
# peso = float(input("Ingrese su peso en kg: "))
# estatura = float(input("Ingrese su estatura en metros: "))
# print("Su IMC es: ", imc(peso, estatura))


# def div(num_1, num_2):
#     cociente = num_1 / num_2
#     result = num_1 % num_2
#     return cociente, result

# num_1 = int(input("Ingrese el primer número: "))
# num_2 = int(input("Ingrese el segundo número: "))

# # Llamar a la función div y almacenar los resultados
# cociente, result = div(num_1, num_2)  #Cociente y result trabajan con los valores de num_1 y num_2
# # Imprimir los resultados
# print("El cociente es: ", cociente, "El resto es: ", result)


# def finca(cantidad, interes, años):
#     operacion = round(cantidad * (interes / 100 + 1) ** años, 2)  #La funcion round debe contener toda la operacion en el parentesis
#     return operacion
# cantidad = float(input("Ingrese la cantidad de dinero: "))
# interes = float(input("Ingrese el interés anual: "))
# años = int(input("Ingrese el numero de años: "))

# print("El capital obtenido es:", finca(cantidad, interes, años))


# peso_payasos = 112
# peso_muñecas = 75

# def juguetes(payasos, muñecas):
#     peso_total = (payasos * peso_payasos) + (muñecas * peso_muñecas)  #Ya definidos los pesos, se pueden usar directamente en nuestra función
#     return peso_total
# payasos = int(input("Ingrese el numero de payasos: "))
# muñecas = int(input("Ingrese el numero de muñecas: "))
# print("El peso total de los juguetes es: ", juguetes(payasos,muñecas))

# interes = 0.04
# plata = float(input("Ingrese su inversion: "))
# balance_1 = round(plata * (1 + interes),2)
# balance_2 = round(balance_1 * (1 + interes),2)
# balance_3 = round(balance_2 * (1 + interes),2)

# print("El balance de su inversion en 1 año es: ", balance_1)
# print("El balance de su inversion en 2 años es: ", balance_2)
# print("El balance de su inversion en 3 años es: ", balance_3)



barras = int(input("Ingrese el numero de barras vendidas que no son frescas: "))
precio_pan = 3.49
descuento = 0.6
coste = round(barras * precio_pan * (1 - descuento), 2)
print(f"El precio de una barra de pan fresco es: {precio_pan} € ")
print(f"El descuento de las barras de pan que no estan frescas es del: " + str(descuento))  #Se puede usar el str() para convertir el valor de descuento a string
print(f"El precio total a pagar es: {coste} €")  #O se puede usar f y {coste} tambien para obtener el valor como un string