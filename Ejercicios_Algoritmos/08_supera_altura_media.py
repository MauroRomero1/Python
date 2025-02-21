""" 08-Dada la estatura y sexo de una persona adulta, determinar si la misma supera la estatura media para las personas de 
su sexo siendo:
-Estatura media de mujeres adultas: 1,65 m.
-Estatura media de hombres adultos: 1,72 m
"""

sexo = input("ingrese sexo (M/F): ").upper()

while sexo != "F" and sexo != "M":
        sexo = input("ingrese sexo (M/F): ").upper()

# metodo .upper() convierte las letras a mayuscula
estatura = float(input("ingrese altura: "))

if (sexo == "M" and estatura >= 1.72) or  (sexo == "F" and estatura >= 1.65):
        print(f"Tu estatura de {estatura} supera el promedio ")
else: 
        print(f"Tu estatura de {estatura} no supera el promedio")