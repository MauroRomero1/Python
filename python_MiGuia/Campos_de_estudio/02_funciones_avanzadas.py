'''2. Funciones avanzadas
Escribe funciones con argumentos opcionales, valores por defecto y *args, **kwargs.
Aprende sobre funciones lambda (funciones anónimas).
Ejemplo práctico : Crear funciones reutilizables y más flexibles.'''

#  1. Funciones lambda (Funciones anónimas)
'''Son funciones pequeñas y rápidas que no necesitan ser definidas con def. Se usan para operaciones simples y suelen combinarse con funciones como map, filter, y reduce.'''
# Sintaxis: lambda argumentos: expresión
suma = lambda x, y: x + y
print(suma(5, 3))  # Salida: 8

'''Ejemplo práctico con filter:'''
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6]


# 2. Funciones anidadas
'''Son funciones definidas dentro de otras funciones.
 Se utilizan para encapsular comportamientos o para implementar cierres (closures).'''
def operacion(base):
    def suma(x):
        return base + x
    return suma

sumar10 = operacion(10)
print(sumar10(5))  # Salida: 15

# 3. Closures
'''Un closure ocurre cuando una función anidada "recuerda" las variables del ámbito externo, incluso si ese ámbito ya no está activo.'''
def multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

doble = multiplicador(2)
triple = multiplicador(3)
print(doble(5))   # Salida: 10
print(triple(5))  # Salida: 15

# 4. Decoradores
'''Son funciones que toman otra función como entrada y devuelven una nueva función. Se utilizan para modificar o extender el comportamiento de funciones sin cambiar su código.'''
def decorador(func):
    def envoltura():
        print("Antes de la función.")
        func()
        print("Después de la función.")
    return envoltura

@decorador
def saludo():
    print("¡Hola mundo!")

saludo()

# 5. Recursividad
'''Es cuando una función se llama a sí misma para resolver problemas más pequeños de la misma naturaleza. Es útil para trabajar con estructuras como árboles o resolver problemas matemáticos.'''
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Salida: 120

#6. Manejo dinámico de argumentos (*args y **kwargs)
'''Permite que una función reciba un número arbitrario de argumentos posicionales o de palabras clave.
'''
# *args (Argumentos posicionales):
def suma(*numeros):
    return sum(numeros)

print(suma(1, 2, 3, 4))  # Salida: 10

# **kwargs (Argumentos nombrados):
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")

#7. Funciones como argumentos
'''Puedes pasar funciones como argumentos a otras funciones, lo que permite crear comportamientos dinámicos.'''
def aplicar_funcion(func, valores):
    return [func(valor) for valor in valores]

doble = lambda x: x * 2
print(aplicar_funcion(doble, [1, 2, 3]))  # Salida: [2, 4, 6]

# 8. Retornar funciones
'''Las funciones pueden devolver otras funciones, permitiendo una programación más flexible.'''
def crear_potencia(exponente):
    def potencia(base):
        return base ** exponente
    return potencia

cuadrado = crear_potencia(2)
print(cuadrado(4))  # Salida: 16


# 9. Generadores
'''Son funciones que devuelven un objeto iterable, usando yield en lugar de return. Permiten trabajar con grandes volúmenes de datos de manera eficiente.'''
def contador():
    for i in range(5):
        yield i

for numero in contador():
    print(numero)

#10. Funciones integradas avanzadas
""" map: Aplica una función a cada elemento de un iterable. """
numeros = [1, 2, 3]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9]

""" filter: Filtra elementos de un iterable basándose en una condición. """
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2]

"""reduce: Aplica una función acumulativa a los elementos de un iterable (requiere functools)."""
from functools import reduce

numeros = [1, 2, 3, 4]
suma_total = reduce(lambda x, y: x + y, numeros)
print(suma_total)  # Salida: 10


#11. Anotaciones de tipo
'''Permiten documentar el tipo de datos esperado o retornado por una función.'''
def suma(a: int, b: int) -> int:
    return a + b
