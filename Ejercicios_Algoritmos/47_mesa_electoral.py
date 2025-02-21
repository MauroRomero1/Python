"""47-Finalizados los comicios, en una mesa electoral se abrirán las urnas y comenzará el recuento de votos. Los votos se 
ingresarán al sistema uno por uno, la cantidad total de votos no se encuentra determinada. Los partidos políticos se 
encuentran enumerados de 1 a 13. Al finalizar, se deberá presentar un informe que especifique los partidos más 
votados del 1er al 5to puesto, junto con el porcentaje de votos obtenido por cada uno de ellos."""


from collections import Counter 

def recuento_votos():
    votos = []

    while True:
        entrada = input("Ingrese el numero de partido politico (1-13) o 'fin': ")
        
        if entrada.lower() == 'fin':
            break
        if entrada.isdigit():
            partido = int(entrada)
            if 1 <= partido <= 13:
                votos.append(partido)
            else:
                print('el numero es invalido, ingrese un numero entre 1 y 13: ')
        else: 
            print("entrada no valida. ingrese un numero entre 1 y 13 o 'fin' para salir")

    if not votos:
        print('no se registran votos')
        return
    
    #contador de votos por partido
    conteo = Counter(votos)
    total_votos = sum(conteo.values())



    # ordenar los partidos por num de votos
    partidos_ordenados = conteo.most_common() # Devuelve los elementos más comunes como lista de tuplas (elemento, frecuencia).


    print("\nResultados de los comicios:\n")
    print("Posición | Partido | Votos | Porcentaje")
    print("-------------------------------------")

    for i, (partido, cantidad) in enumerate(partidos_ordenados[:5], start = 1):
        porcentaje= (cantidad / total_votos)*100 
        print(f"{i:^9}|{partido:^9}|{cantidad^7}|{porcentaje:>9.2f}%")

print("\nRecuento finalizado.")

if __name__ == "__main__":
    recuento_votos()