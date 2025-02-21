import sqlite3
conn = sqlite3.connect("mi_base.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO usuarios(nombre, edad) VALUES (?,?)", ("Pedro", 25))#(?,?) evita inyeccion sql
cursor.execute("INSERT INTO usuarios(nombre, edad) VALUES (?,?)", ("Maria", 30))

cursor.execute("SELECT* FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conn.commit()
conn.close()