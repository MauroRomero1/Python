import numpy as np
import matplotlib.pyplot as plt
'''Ejemplo 1: Simulación de lanzamiento de un dado'''

dado = [1,2,3,4,5,6]
tirada = np.random.choice(dado, 1)
print(tirada)

# Simula 10 lanzamientos de un dado

print(np.random.randint(1,7 ,10))

'''Ejemplo 2: Seleccionar una muestra aleatoria de un conjunto de datos '''

alumnos = np.array(["Ana", "Luis", "Carlos", "Sofía", "Miguel"])

print(np.random.choice(alumnos, 2, replace=False))

''' Ejemplo 3: Distribución de edades en una empresa (normal)'''

edades = np.random.normal(35,10,12)  # Media 35 años, desviación 10 años, 12 empleados
print(edades)

plt.hist(edades,bins=30, edgecolor='black')
plt.show()