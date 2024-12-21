# x = 1 
# if x == 1:
#     print("Yes")
# else:
#     print("No")

# #Operador And
# x = 5
# y = 5

# if x == 5 and y == 5:
#     print("Yes")
# else:
#     print("No")

# #Operador or 
# x = 2
# y = 3
# if x == 1 or y == 2:
#     print("Yes")
# else:
#     print("No")

# def temp(foo):
#     if foo > 7:
#         return "Warm"
#     elif foo <= 7:
#         return"Cold"
#     return temp
# print(temp(10))

# Controlador de contraseña (E)
# Defina una función que:
# (1) toma una cadena como parámetro
# (2) devuelve False si la cadena contiene menos de 8 caracteres
# (3) devuelve Verdadero si la cadena contiene 8 o más caracteres
# En otras palabras, si llamo a su función con foo("mypass") devolverá False. Si lo llamé con foo("mylongpassword") devolvería True, y así sucesivamente.

def str(foo):
    length = len(foo)
    if length < 8:
        return False
    if length >= 8:
        return True
print(str("mypass"))