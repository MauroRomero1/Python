import sqlite3
conn=sqlite3.connect("mi_base.db")
cursor = conn.cursor()


# Filtrar usuarios mayores de 25 años
cursor.execute("SELECT * FROM usuarios WHERE edad > ?", (25,))
print(cursor.fetchall())


# Buscar nombres que contengan "a"
cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE ?", ("%a%",))
print(cursor.fetchall())

# Buscar usuarios con edad entre 20 y 40
cursor.execute("SELECT * FROM usuarios WHERE edad BETWEEN ? AND ?", (20,40))
print(cursor.fetchall())

cursor.execute("SELECT * FROM usuarios WHERE edad in (?,?,?)", (15,30,25))
print(cursor.fetchall())

conn.close()