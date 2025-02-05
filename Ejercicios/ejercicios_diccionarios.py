monedas = {
    'Euro':'€', 
    'Dollar':'$', 
    'Yen':'¥'
    }
moneda = input("Ingresa la moneda que deseas buscar:  ")
print(monedas.get(moneda.title(), "Moneda no encontrada"))