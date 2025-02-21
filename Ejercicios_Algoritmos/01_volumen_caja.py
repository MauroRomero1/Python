""" 01-Ingresar el alto, ancho y profundidad de una caja y presentar su volumen.
"""

alto = float(input("Ingrese el alto de la caja: "))
ancho =  float(input("Ingrese el ancho de la caja: "))
profundidad = float(input("Ingrese la profundidad de la caja: "))

volumen = alto * ancho *profundidad
print(f"El volumen de la caja es {volumen}")