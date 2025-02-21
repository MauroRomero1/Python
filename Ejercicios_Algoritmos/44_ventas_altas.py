"""44-Una empresa tiene a sus vendedores codificados con números consecutivos enteros de 1 a 15. Por cada uno de 
ellos se tienen los siguientes datos:
 número de identificación e importe total vendido en el mes. Esta información 
viene desordenada. 
Se requiere saber los números de los vendedores cuya venta haya sido superior a la venta promedio de la empresa.
"""
ventas_vendedores=[0] * 15

def carga_de_datos():
    while True:
        codigo = int(input("Ingrese numero de identificacion - 0 para salir : "))
        if codigo == 0:
            break
        if not codigo in range(16): 
            print("Numero de identificacion no valido. ")
            continue
        ventas_vendedores[codigo - 1] = float(input("Ingrese importe total vendido este mes: "))
    print("Ventas cargadas:", ventas_vendedores)

def calcular_promedio():
    total_ventas = 0 
    for i in range(15):
        total_ventas += ventas_vendedores[i]
    promedio = total_ventas / 15
    for i in range(15):
        if ventas_vendedores[i] > promedio:
            print(f"El vendedor {i + 1} supera el promedio. ")

    
carga_de_datos()
calcular_promedio()

