import pandas

df = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Quantity", "Value"], index=["A", "B"])  #Asignamos el nobre de las columnas y filas, index es fila
print(df)
print(df.mean())  #Obtener la media de los datos
print(df.median().mean())  #Obtener la media total
print(f"La media de precios es: \n{df.Price.mean()}")  #btener la media de una columna en especifico

#Crear un dataframe con diccionario
df2 = pandas.DataFrame([{"Name": "Juan", "Surname": "Reina", "Age": 20}, {"Name": "Ana", "Surname": "Sanchez", "Age": 23}])
print(df2)
