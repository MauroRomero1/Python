""" 03-Desarrolle un algoritmo que permita determinar el volumen de un cilindro de radio (R) y altura (H). 
"""

import math
radio = float(input("ingrese el radio del cilindro: "))
altura = float(input("ingrese la altura del cilindro: "))

volumen_cilindro = math.pi * radio**2 * altura
print(f"El volumen del cilindro es : {volumen_cilindro}")