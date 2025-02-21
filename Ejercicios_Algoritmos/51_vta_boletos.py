'''51-La empresa Bus S.A., dedicada al transporte de pasajeros, es una entidad que recién comienza con su actividad comercial. Por tal motivo solo cuenta con 3 unidades.
Cada unidad tendrá asociado un Código de destino y su capacidad, los cuales serán asignados al iniciar el día.
Al presentarse un cliente se ingresa su DNI y Código de Destino. Si la unidad para el destino seleccionado no cuenta con espacio disponible o el destino es inexistente se deberá presentar el alerta mensaje correspondiente.
Los precios del boleto según el destino (1, 2, 3) son: $5, $7 y $10 respectivamente.
Se le deberá informar a cada pasajero su importe y al finalizar se listarán las unidades, cada una con su
correspondiente recaudación (ordenadas por recaudación en forma decreciente).
Utilizar al menos un arreglo de dos dimensiones y fijar un criterio para finalizar la carga de datos.'''

unidades = [ # Destino, Capacidad, Recaudación 0
    [1, 3, 0], 
    [2, 2, 0],
    [3, 4, 0]
]
precios = {
    1:5,
    2:7,
    3:10
}

print("Sistema de venta de boletos de Bus S.A.")

while True:
    dni=input("ingrese DNI o ('0' para finalizar):")
    if dni == '0':
        break
    try:
        destino = int(input("Ingrese codigo de destino (1, 2, o 3): "))
    except ValueError:
        print("Entrada invalida. intente nuevamente. ")
        continue
    unidad_encontrada = False
    for unidad in unidades:
        if unidad[0] == destino:
            unidad_encontrada = True
            print(unidad_encontrada)
            if unidad[1] > 0:
                importe = precios[destino]
                print(f"El importe a pagar es: {importe}")
                unidad[1] -= 1
                unidad[2] += importe
        else:
            print("No hay espacio disponible. ")
        break
    if not unidad_encontrada:
        print("El destino no existe.")
   
unidades.sort(key=lambda x: x[2], reverse=True)

print("\n Recaudacion final por unidad.")
for i, unidades in enumerate(unidades, 1):
    print(f"Unidad {i} - destino {unidad[0]}: recaudacion{unidad[2]}")




