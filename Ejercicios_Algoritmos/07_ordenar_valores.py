""" 07-Desarrolle un algoritmo que permita leer tres valores y presentarlos en orden creciente. Constatar que los tres 
valores introducidos sean distintos entre sí, y presentar un mensaje de alerta en este caso."""

valor1 = float(input("ingrese el primer valor: "))
valor2 = float(input("ingrese el segundo valor: "))
while valor1 == valor2:
    valor2 = float(input("ingrese el segundo valor: "))
valor3 = float(input("ingrese el tercer valor: "))
while valor1 == valor3 or valor2 == valor3:
    valor3 = float(input("ingrese el tercer valor: "))

valores = sorted([valor1, valor2, valor3])
print(valores)
valores = sorted([valor1, valor2, valor3], reverse=True)
print(valores)
