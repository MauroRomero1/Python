"""
41-Un negocio de ventas al por mayor y por menor comercializa 100 productos distintos (identificados por un número 
entre 1 y 100). Al iniciar, para cada producto se ingresa: código de identificación, cantidad en stock y cantidad mínima 
requerida en stock.
En el transcurso del día se ingresarán las operaciones comerciales pertinentes, de cada una de ellas se ingresará: 
código de artículo, tipo de operación (I: ingreso / E: egreso) y cantidad de unidades. Al finalizar, se espera obtener un 
listado donde se detalle para los 100 productos: stock actual y situación (Con Faltante / Sin Faltante)."""


producto = {}
for i in range(2):
    codigo = int(input('Ingrese codigo de producto: '))
    stock =  int(input("ingrese cantidad requerida en Stock: "))
    minimo =  int(input("ingrese cantidad minima: "))
    producto[codigo] = {"stock" : stock, "minimo" : minimo}

while True:
    codigo =  int(input("Ingrese código del artículo (1-100, o 0 para finalizar): "))
    if codigo == 0:
        break
    if codigo not in producto:
        print("Codigo no valido.")
        continue
    
    operacion = input(("Ingrese tipo de operación | I: ingreso / E: egreso :").upper())
    cantidad_unidades =  int(input("Ingrese cantidad de unidades: "))
    if operacion == "I":
        producto[codigo]["stock"] += cantidad_unidades
    elif operacion == "E":
        if producto[codigo]["stock"] >=  cantidad_unidades:
            producto[codigo]["stock"] -= cantidad_unidades
        else:
            print(f"No hau suficionete stock, unidades disponibles {stock}")
    else:
        print("operacion no valida")

print("\n listado final")
for codigo, datos in producto.items():
    stock_actual = datos["stock"]
    minimo_requerido = datos["minimo"]
    if stock_actual < minimo_requerido:
       situacion = "con faltante"
    else:
        situacion = "sin faltante"
    print(f"Producto {codigo}: Stock Actual = {stock_actual}, Situación = {situacion}")


        


