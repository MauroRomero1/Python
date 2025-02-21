import sqlite3 

conn= sqlite3.connect("mi_base.db")

cursor = conn.cursor()

cursor.execute("UPDATE usuarios SET edad = ? WHERE nombre = ?", (15, "Juan"))

conn.commit()
conn.close()