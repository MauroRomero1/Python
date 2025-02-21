import tkinter as tk
from tkinter import ttk, messagebox 
import database
#funcion para actualizar la lista de clientes 
def actualizar_lista():
    for row in tabla.get_children():
        tabla.delete(row)
    
    clientes = database.obtener_clientes()
    for cliente in clientes:
        tabla.insert("", "end", values = clientes)

def agregar():
    nombre = entry_nombre.get()
    email = entry_email.get()
    telefono = entry_telefono.get()

    if nombre and email and telefono:
        database.agregar_cliente(nombre, email, telefono)