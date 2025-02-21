'''Crea un sistema de gestión de inventario donde:
✅ Los productos están almacenados en un DataFrame de pandas.
✅ Se pueden agregar, eliminar y actualizar productos.
✅ Se puede buscar un producto por código utilizando búsqueda binaria.
✅ Se genera un informe de productos con stock bajo.'''

import pandas as pd
import numpy as np

# Crear DataFrame con datos iniciales
productos = pd.DataFrame({
    "Codigo":np.arange(100,130,1), 
    "Nombre":[f"producto {i}" for i in range(30)],
    "Stock":np.random.randint(5, 50, 30),
    "Precio":np.random.uniform(10, 200, 30),
    "Punto_Pedido":np.random.randint(10, 20, 30)
})  
productos = productos.sort_values(by="Codigo").reset_index(drop=True)# Ordenar por código



# Búsqueda binaria en DataFrame
def busqueda_binaria(df, codigo):
    d,h = 0, len(df) - 1
   
    while d <= h:
        m = (d+h)//2 
        if (df.loc[m, "Codigo"] == codigo):
            return m 
        elif  codigo > df.loc[m, "Codigo"]:
            d = m + 1
        else:
            h = m - 1
    return -1
    
codigo = int(input("ingrese codigo del producto: "))
indice = busqueda_binaria(productos,codigo)

if indice != -1:
    cantidad = int(input("ingrese la cantidad a comprar: "))
    if productos.loc[indice, "Stock"] >= cantidad:
        total = float([productos.loc[indice, "Precio"] * cantidad])
        productos.loc[indice,"Stock"] -= cantidad
        print(f"✅ Compra realizada. Total a pagar: ${total}")
    else:
        print("No hay suficiente stock. ")
else:
    print("Producto no encontrado.")

# Informe de productos con stock bajo
print("\n Productos con bajo stock: ")

print(productos[productos["Stock"]<productos["Punto_Pedido"]])


