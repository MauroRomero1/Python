import numpy as np

arr = np.array([1,2,3,4])
arr = arr + 5

print(arr)  #salida: [6 7 8 9]

''' Operaciones element-wise entre arrays '''
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

result = arr1 + arr2

print(result) #salida [5 7 9]

''' Indexación y Corte '''

arr = np.array([1,2,3,4,5])

print(arr[2]) # salida 3
print(arr[1:3]) #salida [2 3]  

"""
Funciones comunes de NumPy
np.mean(): Promedio
np.sum(): Suma
np.std(): Desviación estándar
np.min() y np.max(): Mínimo y máximo
np.dot(): Producto punto
"""

print(np.mean(arr)) # 3.0
print(np.sum(arr))  # 15
print(np.std(arr))  # 1.4142135623730951
print(np.min(arr))  # 1
print(np.max(arr))  # 5
# print(np.dot(arr))  