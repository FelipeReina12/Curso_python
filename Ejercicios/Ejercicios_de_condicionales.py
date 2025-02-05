# def adulto(edad):
#     if edad >= 18:
#         return "Es mayor de edad"
#     else:
#         return "Es menor de edad"
# edad = int(input("Ingrese su edad para verificar si es mayor de edad:  "))  #Ojo con definir la entrada y el tipo de dato
# print(adulto(edad))


# def contraseña(clave):
#     if clave == "coki21ta":
#         return "Contraseña correcta"
#     else:
#         return "Contraseña incorrecta"
# clave = input("Ingresa tu contraseña:  ")
# print(contraseña(clave))


# def numeros(num_1, num_2):
#     if num_1 == 0:
#         return "Error"
#     elif num_2 == 0:
#         return "Error"
#     else:
#         return num_1 / num_2
# num_1 = int(input("Ingresa el primer numero:  "))
# num_2 = int(input("Ingresa el segundo numero:  "))
# print(numeros(num_1, num_2))


# def par(num):
#     if num % 2 == 0:  #% se usa para el resto de una division
#         return "El número es par"
#     else:
#         return "El número es impar"
# num = int(input("Ingresa el numero para verificar si es par o impar:  "))
# print(par(num))


# def tributar(edad, ingresos):
#     if edad >= 16 and ingresos >= 1000:
#         return "Tienes que tributar"
#     else:
#         return "No tienes que tributar"
# edad = int(input("Ingresa tu edad:  "))
# ingresos = int(input("Ingresa tus ingresos:  "))
# print(tributar(edad, ingresos))


# name = input("¿Cómo te llamas? ")
# gender = input("¿Cuál es tu sexo (M o H)? ")
# if gender == "M":
#     if name.lower() < "m":
#         group = "A"
#     else:
#         group = "B"
# else:
#     if name.lower() > "n":
#         group = "A"
#     else:
#         group = "B"
# print("Tu grupo es " + group)


# renta = float(input("Ingresa tu renta:  "))
# if renta < 10000:
#     tipo = 5
# elif renta < 20000:  #Elif siginifica si no se cumple lo anterior, entonces
#     tipo = 15
# elif renta < 35000:
#     tipo = 20
# elif renta <= 60000:
#     tipo = 30
# elif renta > 60000:
#         tipo = 45
# print(f"Tienes que pagar {renta * tipo / 100} €") 


# bonoficacion = 2400
# inaceptable = 0.0
# aceptable = 0.4
# excelente = 0.6

# puntuacion = float(input("Ingresa tu puntuación:  "))
# if puntuacion == inaceptable:
#     nivel = "Inaceptable"
# elif puntuacion == aceptable:
#     nivel = "Aceptable"
# elif puntuacion >= excelente:
#     nivel = "Excelente"
# else:
#     nivel  = " "
#     if nivel == " ":
#         print("No se puede determinar el nivel de la puntuación")
# cobro = bonoficacion * puntuacion
# print(f"Estás en e nivel:  {nivel}")
# print(f"Te corresponde cobrar: {cobro}")


# def entrada(edad):
#     if edad < 4:
#         return "Entras gratis"
#     elif edad < 18:
#         return "Paga 5 euros"
#     else:
#         return "Paga 10 euros"
# edad = int(input("Ingresa tu edad:  "))
# print(entrada(edad))


print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
# Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")
    
    
    