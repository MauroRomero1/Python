import sqlite3
conn= sqlite3.connect("mi_base.db")
cursor=conn.cursor()

# Contar cuántos usuarios hay
cursor.execute("SELECT COUNT(*) FROM usuarios")
print("Total de usuarios: ", cursor.fetchall()[0])

# Promedio de edad
cursor.execute("SELECT AVG(edad) FROM usuarios")
print("Edad promedio:", cursor.fetchone()[0])

# Sumar todas las edades
cursor.execute("SELECT SUM (edad) FROM usuarios")
print("La suma de todas las edades es:", cursor.fetchall()[0])

# Contar usuarios por edad
cursor.execute("SELECT edad, COUNT(*) FROM usuarios GROUP BY edad")
print("Usuarios por edad:",cursor.fetchall())
conn.close()
