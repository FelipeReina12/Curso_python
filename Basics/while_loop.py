# user_name = " "
# while user_name != "pypy":  #Esto significa que el usuario debe ingresar "pypy" para que el juego comience
#     user_name = input("Enter your name: ")  #De lo contrario , el juego no comienza

#Otra forma de hacerlo 
while True:  #Minetras que la condición sea verdadera, el bucle se repite
    username = input("Enter your name: ")
    if username == "pypy":
        break  #Break es una función que rompe el bucle y sale de él
    else:
        continue  #Si no se cumple, sigue con el bucle