import sqlite3

class Database:
    
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, ibn integer)")
        self.conn.commit()

    def insert(self, title, author, year, ibn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)", (title, author, year, ibn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title= "", author= "", year="", ibn=""):
        self.cur.execute("SELECT * FROM book WHERE title= ? OR author= ? OR year= ? OR ibn= ?", (title, author, year, ibn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id= ?", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, ibn):
        self.cur.execute("UPDATE book SET title= ?, author= ?, year= ?, ibn= ? WHERE id= ?", (title, author, year, ibn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
    # insert("The Sun", "John Marston", 1925, 913124521)
    # delete(3)
    # update(4, "The Moon", "Pipe", 2002, 153488613)
    # print(view())
    # print(search(author= 'John Smith'))  
