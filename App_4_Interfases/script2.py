import psycopg2

def create_table():  # Función para crear la tabla
    conn = psycopg2.connect("dbname = 'Database 1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")  # Conexión con la base de datos
    cur = conn.cursor()  # Cursor para ejecutar sentencias SQL
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")  # Se crea la tabla con columnas correctas
    conn.commit()  # Guardar los cambios
    conn.close()  # Cerrar la conexión

def insert(item, quantity, price):  # Función para insertar datos
    conn = psycopg2.connect("dbname = 'Database 1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO store (item, quantity, price) VALUES ('%s', '%s', '%s')" % (item, quantity, price))  # Insertar datos con nombres de columnas
    conn.commit()
    conn.close()

def view():  # Función para mostrar los datos de la tabla
    conn = psycopg2.connect("dbname = 'Database 1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):  # Función para borrar los datos de la tabla
    conn = psycopg2.connect("dbname = 'Database 1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):  # Función para borrar los datos de la tabla
    conn = psycopg2.connect("dbname = 'Database 1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()





# Crear la tabla y agregar un registro
create_table()
# # insert("Apple", 10, 5)
# insert("Watter", 15, 2)
update(20, 4, "Watter")
# delete("Apple")
# delete("Coffe Cup")
# Mostrar los registros
# print(view())
