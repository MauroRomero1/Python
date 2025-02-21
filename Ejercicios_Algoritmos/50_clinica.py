'''50-Crazy es una clínica de salud mental. Con la finalidad de responder a pedidos efectuados por el director, se deberá emitir un listado con los siguientes datos: código que identifica el desorden mental (1..10) y porcentaje de recuperación, presentándose ordenado en forma decreciente según porcentaje de recuperación. Para ello, se ingresará de cada paciente: código de padecimiento, número de historia clínica y estado actual (R: Recuperado / NR: No Recuperado). La cantidad de ingresos no está determinada. Utilizar al menos un arreglo de dos dimensiones y fijar un criterio para finalizar la carga de datos.'''

lista = [[codigo, 0,0] for codigo in range(1,11)]

print("Ingrese los datos de los pacientes. Ingrese '0' como código para finalizar.\n")

while True:
    codigo = int(input("Código de padecimiento (1-10, 0 para salir): "))
    if codigo == 0:
        break
    if not (1 <= codigo <= 11):
        print("⚠ codigo invalido. debe estar entre el 1 y el 10. ")
        continue
    historial_clinico = input("Numero de historial clinica: ")
    estado = input("Ingrese estado ('R'= Recuperado, 'NR' = No recuperado): ")
    if estado not in ["R", "NR"]:
        print("Estado invalido ingrese 'R' o 'NR'. ")
        continue

    lista[codigo-1][1] += 1
    if estado == "R":
        lista[codigo-1][2] += 1
    print(lista)

resultados = []
for codigo, total_paciente, total_recuperado in lista:
    if total_paciente > 0:
        porcentaje_recuperacion = (total_recuperado/ total_paciente)*100
        resultados.append([codigo, porcentaje_recuperacion])

# Ordenar en orden decreciente por porcentaje de recuperación
resultados.sort(key=lambda x:x[1], reverse=True) 

print("\n Listado de porcentaje d erecuperacion: ")
print("-----------------------------------------")
print("Codigo | Porcentaje de Recuperacion")
print("-----------------------------------------")

for codigo, porcentaje in resultados:
    print(f" {codigo}  |  {porcentaje:.2f}%")

if not resultados:
    print("No se registran datos.")