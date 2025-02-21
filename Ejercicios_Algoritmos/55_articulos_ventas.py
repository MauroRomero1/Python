'''55-Un comercio cuenta con su lista de 30 artículos destinados para la venta, registrados en una matriz donde se detalla: 
código del artículo, 
cantidad en stock, 
punto de pedido y 
precio unitario. 
La matriz se encuentra ordenada por 
código de articulo en forma creciente y dichos códigos son números enteros no consecutivos.
Cuando un cliente llega a la caja, se ingresará de cada artículo: código y cantidad, emitiéndose la correspondiente línea en el ticket que especifica el importe a abonar por este artículo, al finalizar la carga de artículos se emitirá en el ticket el monto total a abonar.
La cantidad de clientes no está determinada. La búsqueda del artículo debe realizarse implementando búsqueda dicotómica. Si el articulo no es hallado se presentará el alerta correspondiente.
Al finalizar, se presentará un informe detallado de los artículos que se encuentran con faltante de stock'''

import numpy as np

matriz = np.zeros((30,4))
for i in range(30):
    matriz[i][0] = i
    matriz[i][1] = i+4
    matriz[i][2] = i+2
    matriz[i][3] = i+1



def busqueda_binaria(matriz, cod):
    d, h = 0, len(matriz) - 1
    while d <= h:
        m = (d+h)//2
        if matriz[m][0] == cod:
            return m
        elif matriz[m][0] < cod:
            d = m + 1
            
        else:
            h = m - 1
    return -1

while True:
    try:
        cod = int(input("Ingrese codigo del articulo: "))
        if cod == -1:
            break
        resultado = busqueda_binaria(matriz, cod)
        if resultado != -1:
            cantidad = int(input("Ingresa cantidad: "))
            if matriz[resultado][1] >= cantidad:
                print(f"Codigo de articulo: {matriz[resultado][0]}")
                print(f"cantidad: {cantidad}")
                print(f"Precio total: {matriz[resultado][3] * cantidad}")
                matriz[resultado][1] = matriz[resultado][1] - cantidad
            else: 
                print("No hay stock suficiente")
        else:
            print(f"El número {resultado} no está en la lista.")
    except ValueError:
        print("Error")

# Generar informe de artículos con stock insuficiente
print("\n📢 Informe de artículos con stock insuficiente:")
print("Código | Stock | Punto de pedido")
for i in range(len(matriz)):
    if matriz[i][1] < matriz[i][2]:  # Stock menor que el punto de pedido
        print(f"{int(matriz[i][0])}  | {int(matriz[i][1])}  | {int(matriz[i][2])}")
