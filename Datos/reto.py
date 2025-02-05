import pandas as pd

datos = {
    "Producto": ["A", "B", "C", "D", "E", "F"],
    "Categoría": ["Ropa", "Calzado", "Camisas", "Accesorios", "Medias", "Canilleras"],
    "Precio": [35, 55, 15, 28, 45, 12],
    "Unidades vendidas": [500, 148, 256, 845, 486, 123]
}

ventas = pd.DataFrame(datos)
print(ventas)
print(f"El producto mas costoso: \n {ventas.nlargest(1, 'Precio')}")  # Mostrar el producto más costoso se pone el 1 para que solo muestre el producto más costoso
print(f"El producto que mas se ha vendido es \n {ventas.nlargest(1, 'Unidades vendidas')}") 