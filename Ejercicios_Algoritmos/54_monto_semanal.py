'''54-El propietario de un comercio se encuentra estresado y desea determinar el día de la semana que sería más adecuado tomar un descanso. 
Para cumplir con el objetivo, al finalizar el mes en curso, el propietario ingresará de cada venta realizada: número de día de la semana (1..7) y monto.
Al finalizar, el usuario tendrá la posibilidad de realizar consultas con respecto a un determinado día.
Ingresando el nombre del día de la semana, se presentará por pantalla, el monto recaudado y el porcentaje sobre el total general que dicho monto representa. La cantidad de consultas es indeterminada.
Las ventas se encuentran desordenadas y para un día determinado pueden tenerse n ventas. Utilizar Arreglos y búsqueda dicotómica.'''

# mi razonamiento respecto al ejercicio puede estar mal 
import numpy as np
arr = np.zeros((7))

while True:
    dia = int(input("Ingrese dia de la semana (0 para salir): "))
    if dia == 0:
        break
    if 1<=dia<=7 :
        monto = float(input("Ingrese monto: "))
        arr[dia-1] += monto
        print(arr)
    continue
dias ={1: "Domingo",2:"Lunes",3:"Martes", 4:"Miercoles", 5:"Jueves", 6:"Viernes", 7:"Sabado" }
while True:
    num = int(input("Ingrese dia de la semana a consultar (0 para salir): "))
    dia = dias[num]

    print(f"El dia {dia} se recaudo un total de: ${arr[num-1]}")



