"""Se cuenta con una matriz de 5x5 cargada de números positivos, negativos y nulos. Presentar un listado con los 5 
números mayores (sin repetición)."""
import numpy as np
print(np.__version__)

matriz = np.random.randint(-10,11,(5,5))
# Generar una matriz 5x5 con números positivos, negativos y nulos

print("Matriz 5x5 generada:")
print(matriz)

valores_unicos = list(set(matriz.flatten()))
# Aplanar la matriz a una lista y eliminar duplicados

# Ordenar la lista en orden descendente
valores_unicos.sort(reverse=True)

# Obtener los 5 números mayores (sin repetición)
top_5 = valores_unicos[:5]
print("\nLos 5 números mayores (sin repetición) son:")
print(top_5)
