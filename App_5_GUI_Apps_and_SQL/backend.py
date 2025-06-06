import sqlite3

def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, ibn integer)")
    conn.commit()
    conn.close()

def insert(title, author, year, ibn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, ibn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title= "", author= "", year="", ibn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title= ? OR author= ? OR year= ? OR ibn= ?", (title, author, year, ibn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id= ?", (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, ibn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title= ?, author= ?, year= ?, ibn= ? WHERE id= ?", (title, author, year, ibn, id))
    conn.commit()
    conn.close()





connect()
# insert("The Sun", "John Marston", 1925, 913124521)
# delete(3)
# update(4, "The Moon", "Pipe", 2002, 153488613)
# print(view())
# print(search(author= 'John Smith'))  
