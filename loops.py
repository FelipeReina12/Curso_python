monday_temperatures = [9.8, 8.7, 7.5, 12.2, 10.9]
print(round(monday_temperatures[0]))  #Redondea la cifra que está de primeras en la lista


for temperature in monday_temperatures:  #Recorre la lista de temperaturas con la variable temperature
    print(round(temperature))  #Redondea cada temperatura en la lista


for letter in "hello":  #Recorre la cadena de texto con la variable letter
    print(letter.title())  #Imprime cada letra en la cadena en mayúscula


colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    print(color)


colors_2 = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for i in colors_2:
    if isinstance(i, int):  #Se utiliza isinstance para verificar si el elemento es de tipo int
        print(i)


colors_3 = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for i in colors_3:
    if isinstance(i, int) and i >= 53:
        print(i)


def celsius_to_kelvin(cels):
    return cels + 273.15
 
for temperature in [9.1, 8.8, -270.15]:
    print(celsius_to_kelvin(temperature))

students = {
    "Marry":19,
    "John": 20,
    "Emma": 18
}
for grades in students.items():  #Lo que hace es recorrer el diccionario Y .items () es para obtener las claves y los valores
    print(grades)


phone_numbers = {
    "Marry": 1234567890,
    "John": 9876543210,
    "Emma": 1111111111
}
for pair in phone_numbers.items():
    print(f"{pair[0]} has as phone number {pair[1]}")  #Aqui se imprime el nombre y el número de teléfono de cada persona el 0 y el 1 son los índices de la tupla que se obtiene con .items()

#Otra forma de hacerlo 
for key, values in phone_numbers.items():
    print(f"{key} has as phone number {values}")


numbers = {
    "John Smith": "+37682929928",
    "Marry Simpons": "+423998200919"
}
for key, values in numbers.items():
    print(f"{key}: {values}")


phone_numbers_2 = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for values in phone_numbers_2.values():
    print(values.replace("+", "00"))