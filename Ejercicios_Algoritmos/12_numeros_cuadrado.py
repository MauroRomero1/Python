""" 12-Se leen de a uno por vez 5 valores. Calcular y exhibir el cuadrado de cada uno de ellos."""

def cuadrado():
    for i in range (1,26):
        valor  = float(input(f"Ingresa el valor {i}: "))
        print(f"El cuadrado del valor {valor} es {valor**2}")
         
cuadrado()