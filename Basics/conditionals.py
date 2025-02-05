# Definición de la función 'mean' que calcula la media de un conjunto de valores
def mean(value):
    # Verifica si el tipo de 'value' es un diccionario
    if isinstance(value, dict):  #Instance compara dos cosas equivale a ==
        # Si es un diccionario, calcula la media de sus valores
        # Suma todos los valores del diccionario y los divide por la cantidad de elementos
        the_mean = sum(value.values()) / len(value)
    else:
        # Si 'value' no es un diccionario (por ejemplo, una lista), calcula la media de los elementos
        # Suma todos los elementos y los divide por la cantidad de elementos
        the_mean = sum(value) / len(value)
    # Devuelve la media calculada
    return the_mean

# Lista de temperaturas del lunes
monday_temps = [8.8, 9.4, 7.5]

# Diccionario que contiene las calificaciones de los estudiantes
students_gades = {"Marry": 9.1, "Bob": 8.8, "John": 7.5}

# Llama a la función 'mean' con la lista de temperaturas del lunes y imprime el resultado
print(mean(monday_temps)) 

# Llama a la función 'mean' con el diccionario de calificaciones de los estudiantes y imprime el resultado
print(mean(students_gades))