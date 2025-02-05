def mean(my_list):  #Definición de la función 'mean' que toma un argumento 'my_list'
    the_mean = sum(my_list) / len(my_list)  #Calcula la media sumando los elementos de 'my_list' y dividiendo por la cantidad de elementos
    return the_mean  #Devuelve el valor de la media calculada

my_mean = mean([1, 2, 3, 4, 5])
print(my_mean + 10)  #Llama a la función 'mean' con una lista de números y imprime el resultado

print(type(mean), type(sum), type(len))  #Nos muestra que tipo de variables son 

def convert(amount):
    output = amount *1.75
    return output
print(convert(10))

def temp(foo):
    if foo > 7:
        print("Warm")
    elif foo <= 7:
        print("Cold")
    return temp
print(temp(10))

def temp(foo):
    if foo > 25:
        return 'Hot'
    elif foo >= 15 and foo <= 25:
        return 'Warm'
    elif foo < 15:
        return 'Cold'
print(temp(10))