def setence_maker(phrase):
    capitalized = phrase.capitalize()  # Se usa para volver mayuscula la primera letra de la frase
    if phrase.startswith(('how', 'what', 'why')):  # startswith es una función que devuelve True si el string comienza con el argumento que está en la tupla
        # Otra forma de hacerlo es almacenando las palabras de la tupla en una variable y compararla con el string
        return "{}?".format(capitalized)  # Si en la frase está una de las palabras de la tupla, añade el ? al final de la frase
    else:
        return "{}".format(capitalized)  # Retorna la frase capitalizada sin añadir el ?

results = []  # Inicializa una lista vacía para almacenar los resultados
while True:  # Inicia un bucle infinito
    user_input = input("Say something: ")  # Solicita al usuario que ingrese algo
    if user_input == "\end":  # Verifica si la entrada del usuario es "\end"
        break  # Si es así, sale del bucle
    else:
        results.append(setence_maker(user_input))  # Llama a setence_maker y añade el resultado a la lista
print(" ".join(results))  # Imprime la lista de resultados con un espacio entre cada elemento para eso se usa el join, es para unirlos