"""
17-Ingresada una lista de 10 números, determinar e informar el valor máximo y mínimo junto con el orden en el que 
fueron ingresados.
"""

lista = []

for i in range(1, 11):
    numero= float(input(f"Ingrese el valor {1}: "))
    lista.append(numero)

maximo = max(lista)
minimo = min(lista)

print(f"El valor máximo es {maximo} en la posición {lista.index(maximo) + 1}")

print(f"El valor mínimo es {minimo} en la posición {lista.index(minimo) + 1}")
