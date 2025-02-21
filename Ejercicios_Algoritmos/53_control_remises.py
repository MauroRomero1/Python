'''52-Una empresa de remises desea llevar un control más estricto sobre cada unidad. Por ello, al iniciar la jornada, se ingresará el precio por km y para cada unidad se ingresará el kilometraje actual.
En el transcurso del día, los clientes realizan un llamado a la central solicitando un vehículo, en este momento la 
recepcionista ingresará los siguientes datos: km del viaje y unidad asignada (1..15), se deberá emitir un ticket donde se presentarán los datos del viaje: Km, Unidad e Importe a cobrar.
Suponer que todos los viajes solicitados se realizan. La cantidad de viajes es desconocida.
Al finalizar la jornada laboral, se listará un informe que detallará: Unidad, Cantidad de Viajes Realizados, Importe 
Recaudado y Kilometraje Teórico Actual (km al inicio de la jornada más los correspondientes a los viajes realizados por el vehículo). El listado deberá presentarse ordenado por recaudación en forma decreciente.'''

precio_km = float(input("Ingrese precio por km: "))
km_inicial = [0] * 15
km_actual = [0] * 15
recaudacion = [0]*15
cant_viajes = [0]*15

for i in range(15):
    km_inicial[i] = int(input(f"Ingrese km actual de la unidad {i+1} : "))
    km_actual[i] = km_inicial[i]
while True:
    unidad = int(input('Ingrese número de unidad (1 a 15, 0 para finalizar): '))
    if unidad == 0:
        break
    if 1<= unidad <=15:
        km_viaje = int(input('Ingrese km del viaje: '))
        importe = km_viaje * precio_km

        cant_viajes[unidad-1] +=1
        recaudacion[unidad-1] += importe
        km_actual[unidad -1] += km_viaje

        print("-------------")
        print("|    Tiket   |")
        print("-------------")
        print(f"Unidad :{unidad} ")
        print(f"km del viaje :{km_viaje}")
        print(f"Importe a pagar: ${importe:.2f}")

        print("-------------")
    else:
        print("unidad no encontrada. ")
datos_unidades = []
for i in range(15):
    datos_unidades.append((i + 1, cant_viajes[i], recaudacion[i], km_actual[i] ))

datos_unidades.sort(key=lambda x:x[2], reverse=True)

for unidad, viajes, total_recaudado, km_teorico in datos_unidades:
    print(f"\nUnidad: {unidad}")
    print(f"Cantidad de viajes: {viajes}")
    print(f"Recaudación total: ${total_recaudado:.2f}")
    print(f"Kilometraje teórico actual: {km_teorico} km")

