""" 14-La empresa proveedora de energía eléctrica ingresa por única vez el precio por KwH y pretende conocer para cada 
uno de los 1000 usuarios el consumo del mes y el importe a abonar. Para ello, cuenta con pares de valores que 
indican, para cada medidor, el estado del mismo al final del mes anterior y del mes actual."""

def consumo_energia():
    precio_kwh = float(input("Ingresa el precio KwH: "))
    for usuario in range(1, 1001):
        anterior = float(input(f"Usuario {usuario}: Consumo del mes anterior: "))
        actual = float(input(f"Usuario {usuario}: Consummo del mes actual: "))
        consumo = actual - anterior
        importe = consumo * precio_kwh
        print(f"Usuario {usuario}: Consumo: {consumo} KwH, importe a pagar: ${importe: .2f}")
consumo_energia()

        