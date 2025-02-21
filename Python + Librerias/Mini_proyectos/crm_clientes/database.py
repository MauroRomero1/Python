import sqlite3

# Conectar a la base de datos
def conectar():
    return sqlite3.connect("clientes.db")

# Crear tabla si no existe
def crear_tabla():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefono TEXT NOT NULL
        )
    """)
    con.commit()
    con.close()

# Agregar un cliente
def agregar_cliente(nombre, email, telefono):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("INSERT INTO clientes (nombre, email, telefono) VALUES (?, ?, ?)", (nombre, email, telefono))
    con.commit()
    con.close()

# Obtener todos los clientes
def obtener_clientes():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    con.close()
    return clientes

# Buscar cliente
def buscar_cliente(texto):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM clientes WHERE nombre LIKE ? OR email LIKE ? OR telefono LIKE ?", (f"%{texto}%", f"%{texto}%", f"%{texto}%"))
    clientes = cursor.fetchall()
    con.close()
    return clientes

# Eliminar cliente
def eliminar_cliente(id_cliente):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    con.commit()
    con.close()

# Crear la tabla al iniciar
crear_tabla()
