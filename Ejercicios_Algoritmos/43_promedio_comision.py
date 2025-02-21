"""
43-En un instituto de enseñanza superior hay 5 comisiones de primer año (identificadas con las letras M, C, Q, K y E 
según las especialidades). De cada alumno que rindió un parcial de Análisis, se ingresará la comisión y nota obtenida. 
Los datos son dados en forma desordenada, respecto a la comisión. Obtener e informar la nota promedio de cada una 
de las comisiones y la cantidad total de alumnos del instituto que se presentaron a rendir. Con comisión “X” se da por 
terminado el proceso.
"""
datos = {"M": [0, 0], "C": [0, 0], "Q": [0, 0], "K": [0, 0], "E" : [0, 0] }

while True:
    comision = input("Ingrese comision  (M, C, Q, K, E) X para salir :").upper()


    if comision == "X":
        break
    if comision not in datos:
        print("Comisión no válida. Intente nuevamente.")
        continue 
    
    nota = int(input("Ingrese nota: "))
    datos[comision][0] += 1 
    datos[comision][1] += nota
tot = 0
for clave, valor in datos.items():
    tot += valor[0]
    if valor[0] == 0:
         promedio = 0
    else: 
        promedio = valor[1]/valor[0]
    print(f"Comision: {clave} - Promedio {promedio} ")
    

print(f"Cantidad total de alumnos que realizaron el examen: {tot}")

    

