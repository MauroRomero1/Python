"""18- Calcular el promedio de los números ingresados, sabiendo que el fin de la entrada de datos se indica ingresando el 
valor cero."""
numeros = []
num = int(input("Ingrese un numero: "))
while num != 0:
    numeros.append(num)
    num = int(input("Ingrese un numero: "))
print(numeros)
longitud = len(numeros)
suma = sum(numeros)
promedio = suma/longitud
print(promedio)