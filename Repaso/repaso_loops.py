primes = [2, 3, 5, 7]
for prime in primes:  #Aqui se itera sobre cada elemento de la lista y se imprime
    print(prime)


"""
With index
"""
animals = ['cat', 'dog', 'bird']
for i, value in enumerate(animals):  #Recorre la lista y enumera cada elemento
    print(i, value)


"""
Range
"""
for i in range(4):
    print(i)  #Imprime del 0 al 3

for i in range(4, 9):  #Imprime del 4 al 8
    print(i)


"""
For y else
"""
nums = [60, 100, 200, 300, 400, 500]
for num in nums:  #Recorremos la lista con la variable num
    if num > 100:
        print(f"{num} es mayor que 100")
    else:
        print(f"{num} es menor o igual a 100")


"""
While
"""
i = 0
while i < 5:  #Mientras que i sea menor a 5
    print(i)  #Imprimimos los numeros del 0 al 4
    i += 1  #Incrementamos i para que el bucle se termine