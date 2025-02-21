"""16-En una cooperativa agraria dispone de los datos correspondientes a las cosechas obtenidas desde el año 2000 al 
2009 de trigo, maíz, girasol y soja. Desarrollar un algoritmo que permite determinar, para cada año, cuales fueron los 
cultivos que han superado su cosecha correspondiente al año 1979.
"""
def cultivos_cosecha():
    periodo = range(2000,2004)
    cosecha1979 = {"trigo":0, "maiz":0,"girazol":0,"soja":0}

    for clave in cosecha1979:
        cosecha1979[clave] = float(input(f"Ingresa la cosecha de {clave} del año 1979: "))
    print(cosecha1979)

    for a in periodo:
        print(f"Año {a}:")
        cosechas = {}
        for i in cosecha1979.keys():
            cosecha_actual = float(input(f"Ingrese la cosecha de {i}: "))
            cosechas[i] = cosecha_actual
        
        print("Cultivos que superaron la cosecha de 1979:")
        for i, cantidad in cosechas.items():
            if cantidad > cosecha1979[i]:
                print(f"  - {i} con {cantidad}")
     
cultivos_cosecha()