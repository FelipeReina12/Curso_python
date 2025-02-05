# name = input("Ingrese su nombre: ")
# num = int(input("Ingrese un numero: "))
# print((name + "\n") * num)  #\n se usa para saltar a la siguiente linea


# name = input("Ingrese su nombre:  ")
# apellido = input("Ingrese su apellido:  ")
# print(name.lower(), apellido.lower())  #Siempre debe tener parentesis al final de la función
# print(name.upper(), apellido.upper())  #Upper es para poner en mayusculas
# print(name.title(), apellido.title())  #Título es para poner la primera letra en mayuscula


# name = input("Ingrese su nombre:  ")
# numero_de_letras = name.__len__()  #Ojo como se escribe len __len__
# print(f"Su nobre tiene {numero_de_letras} letras")  #len() es para saber cuantas letras tiene un str
# #Otra forma de hacer este ejercicio es 
# print(f"su nombre tiene {len(name)} letras")  #Para no escribir __len__ mejor escribir len(name)


# telefono = input("Ingrese su numero telefonico con prefijo:  ")
# print(f"Su numero de telefono es {telefono [3:]}")  #[3:] indica que comience a contar desde la posicion 3 hasta el final del str


# frase = input("Introduce una frase:  ")
# print(frase[::-1])  #Se pone [::-1] que indica que se debe leer de derecha a izquierda


# frase = input("Introduce una frase:  ")
# vocal = input("Ingresa una vocal en minuscula:  ")
# print(frase.replace(vocal, vocal.upper()))  #Definimos una variable vocal, luego reemlazamos esa vocal con vocal.upper


# correo = input("Ingresa tu correo electronico: ")
# print(correo[:correo.find("@")] + "@ceu.es")  #Correo.find ("@") busca la posicion del "@" y lo devuelve, luego se imprime el correo con el "@"


# precio = input("Introduzca el precio en Euros con 2 decimales:  ")
# # Encuentra la posición del punto decimal en la cadena 'precio'
# # y extrae la parte entera (euros) desde el inicio hasta el punto decimal
# euros = precio[:precio.find('.')]
# # Extrae la parte decimal (céntimos) desde el carácter después del punto decimal hasta el final de la cadena
# centimos = precio[precio.find('.')+1:]
# print(euros, 'euros y', centimos, 'céntimos.')


# fecha = input("Ingrese su fecha de nacimiento dd/mm/aaaa:  ")
# print(f"Su fecha de nacimiento es {fecha[:2]}/{fecha[2:4]}/{fecha[4:]} ")
# print(f"Dia: {fecha[:2]}")
# print(f"Mes: {fecha[2:4]}")
# print(f"Año: {fecha[4:]}")
# #Otra forma de hacerlo:
# fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
# dia = fecha[:fecha.find('/')]
# mesaño = fecha[fecha.find('/')+1:]
# mes = mesaño[:mesaño.find('/')]
# año = mesaño[mesaño.find('/')+1:]
# print('Día', dia)
# print('Mes', mes)
# print('Año', año)


# productos = input("Ingrese sus productos separados por un coma:  ")

# print(productos.replace(',', '\n'))  # Reemplaza las comas en la cadena 'productos' por saltos de línea y los imprime
# # Otra forma de hacerlo
# # Divide la cadena 'productos' en una lista usando la coma como delimitador
# # Luego, une los elementos de la lista en una sola cadena, separándolos con saltos de línea
# print("\n".join(productos.split(",")))


# producto = input('Introduce el nombre del producto: ')
# precio = float(input('Introducde el precio unitario: '))
# unidades = int(input('Introduce el número de unidades: '))
# print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))