# palabra = input("Ingresa una palabra: ")
# for i in range(10):
#     print(palabra)


# edad = int(input("Ingresa tu edad:  "))
# for i in range(edad):
#     print("Has cumplido " + str(i + 1) + " años")  #i + 1 se escribe para sumar un digito


# numero = int(input("Ingresa un numero:  "))
# for i in range(1, numero + 1, 2):  #Aqui indicamos que solo queremos los numeros impares
#     print(i, end=" ")


n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1): 
    print(i, end=", ")