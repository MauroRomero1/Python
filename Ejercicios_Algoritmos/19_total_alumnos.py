"""19-Se tiene una nómina de alumnos con número de legajo y año que cursa (6 años), ordenados por número de legajo. 
Obtener e informar el total de alumnos por año. El proceso termina con un número de legajo igual a cero.
"""
def alumnos_por_curso():
    totales = [0] * 6
    legajo = int(input(f"Ingrese legajo: "))
    while legajo != 0:
        a = int(input("Ingrese el año de alumno (0 para terminar): "))
        if  1 > a < 6: 
            print("Numero no valido!")
            a = int(input("Ingrese el año de alumno: "))
        totales[a] += 1
        legajo = int(input(f"Ingrese legajo: "))
    for i, total in enumerate(totales,start=1):
        print(f"Año {i}: {total} alumnos")
alumnos_por_curso()