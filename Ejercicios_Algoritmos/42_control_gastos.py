"""
42-Se requiere controlar los gastos de mantenimiento de cinco edificios identificados como A, B, C, D y E.
Para ello se dispone de un conjunto de comprobantes con los datos necesarios: 
    identificación del edificio, 
    gastos de limpieza, 
    gastos de servicio y 
    gastos por sueldo.
La cantidad de comprobantes es desconocida y está totalmente desordenado.
Se desea emitir un listado donde conste para cada edificio: 
    identificador, 
    gastos de limpieza, 
    gastos de servicio, 
    gastos por sueldo y 
    total.

"""

edificio = {"A" : [0,0,0],"B" : [0,0,0],"C" : [0,0,0],"D" : [0,0,0],"E" : [0,0,0] }

while True:
    edificios = input("Edificio (A,B,C,D,E), X para terminar: ").upper()
    if edificios == "X":
        break
    limpieza = float(input("Gastos de limpieza: "))
    servicio = float(input("Gastos de servicio: "))
    sueldo = float(input("Gastos por sueldo: "))
    edificios[edificio][0] += limpieza
    edificios[edificio][1] += servicio
    edificios[edificio][2] += sueldo


for edificio, gastos in edificios.items():
        total = sum(gastos)
        print(f"Edificio {edificio}: Limpieza={gastos[0]}, Servicio={gastos[1]}, Sueldo={gastos[2]}, Total={total}")
