import numpy as np

# generar numeros aleatorios basicos (0,1)
print(np.random.rand(5))

# pueden ser negativos o positivos
print(np.random.randn(5))

# matriz de numeros aleatorios (2x3)
print(np.random.rand(2,3))

# pueden ser negativos o positivos
print(np.random.randn(2,3))

# Numeros enteros aleatorios
print(np.random.randint(1,10,5))# 5 números entre 1 y 10

# Matriz 4x4 con enteros entre 10 y 50
print(np.random.randint(10,50,(4,4)))

'''Distribuciones de probabilidad '''
# Generar 10 valores con distribución normal (media=50, desviación=10)
data = np.random.normal(50, 10, 10)

uniforme= np.random.uniform(5, 20, 10)

print(data)
print(uniforme)

""" Barajar y muestrear datos ( shuffle, choice) """
arr = np.array([1, 2, 3, 4, 5])
np.random.shuffle(arr)
print(arr)  # Los elementos están en un orden diferente [3, 1, 5, 2, 4]

arr = np.array([10, 20, 30, 40, 50])
np.random.choice(arr, 3)  # Selecciona 3 valores aleatorios del array [30, 10, 50]

'''Semillas aleatorias (seed)'''
np.random.seed(45) #fijamos la semilla
print(np.random.rand(5))
# Si no usas seed(), cada vez que corras el código, obtendrás resultados diferentes.
