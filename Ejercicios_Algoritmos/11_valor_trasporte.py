"""
11-Una empresa de trasporte de bienes desea conocer el monto a cobrar por el servicio prestado, ingresando el Peso 
y Nivel de Seguridad con el cual debe ser trasladada, teniendo en cuenta las siguientes tablas:

Peso Importe
    Menores a 45 kg $ 150
    Entre 45kg y 90kg $ 300
    Entre 90kg y 150kg $ 550
    Mayores a 150kg NO ADMITIDOS

Nivel de Seguridad Importe
    1 $ 250
    2 $ 100
    3 $ 85
    4 $ 55
    5 $ 35
"""
#la funcion para poder usar el return
def monto_trasporte():
    peso = float(input("Ingresa el peso en Kg del paquete: "))
    nivel_seguridad = int(input("ingrese el nivel de seguridad(Nivel: 1/Nivel: 2/Nivel: 3/Nivel: 4/Nivel: 5): "))
    
    if peso < 45:
        importe_peso = 150
    elif peso <= 90:
        importe_peso = 300
    else:
        importe_peso = 550
    if peso > 150:
        print("No Admitido")
        return

    importe_seguridad = { 1 : 250, 2 : 100, 3 : 85, 4 : 55, 5 : 35}

    importe_total = importe_seguridad.get(nivel_seguridad, 0) + importe_peso

    print(f"El monto total por el servicio es: ${importe_total}")
monto_trasporte()
