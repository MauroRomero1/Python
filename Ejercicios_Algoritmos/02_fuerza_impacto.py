""" 02-Informar la fuerza con la cual impacta un cuerpo de masa M si el mismo se desplaza con una aceleración A. 
"""

masa = float(input("Ingrese la masa del cuerpo (KG): "))
 
aceleracion = float(input("Ingresa la aceleracion (m/s^4): "))

fuerza = masa * aceleracion 
print(f" LA fuerza con la que impacta el cuerpo es: {fuerza}N")