import sqlite3

conn=sqlite3.connect("mi_base.db")
cursor=conn.cursor()

cursor.execute("DELETE FROM usuarios where nombre = ?", ("Maria",))

cursor.execute("SELECT* FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conn.commit()
conn.close()