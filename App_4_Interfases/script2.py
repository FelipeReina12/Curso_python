import sqlite3

def create_table():  #Funcion para crear la tabla
    conn = sqlite3.connect("lite.db")  #Aqui se crea la conexión con la base de datos la cual será llamada "lite.db"
    cur = conn.cursor()  #Aqui se crea el cursor para ejecutar las sentencias SQL
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, picre REAL )")  #Aqui se crea la tabla llamada "store" con las columnas item, quantity y price
    conn.commit()  #Commit para guardar los cambios
    conn.close()  #Close se usa para cerrar la conexión con la base de datos

def insert(item, quantity, price):  #Se crea una función para insertar datos en la tabla
    conn = sqlite3.connect("lite.db")  #Añadimos la conexión con la base de datos
    cur = conn.cursor()  #Añadimos tambien el cursor que es para ejecutar las sentencias SQL
    cur.execute("INSERT INTO store VALUES(?, ?, ?)", (item, quantity, price))  #Aqui se insertan los datos en la tabla, cada ? es un parámetro que se reemplaza con los datos que se le pasan a
    conn.commit()  #Commit para guardar los cambios
    conn.close()  #Close se usa para cerrar la conexión con la base de datos
insert("Coffe Cup", 10, 5)  #Se insertan los datos en la tabla

def view():  #Creamos una vriable para mostrar los datos de la tabla
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")  #Aqui se seleccionan todos los datos de la tabla
    rows = cur.fetchall()  #rows es una lista de tuplas que contiene todos los datos de la tabla
    conn.close()
    return rows
print(view())  