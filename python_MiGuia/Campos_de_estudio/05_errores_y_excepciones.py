'''5. Manejo de Errores y Excepciones
Aprende a manejar errores usando try, except, finally, y raise.
Ejemplo práctico : Crear programas que no caigan inesperadamente y den retroalimentación al usuario.'''



'''  ------ LAS EXCEPCIONES --------
Las excepciones son eventos que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de ejecución.

    Ejemplos comunes de excepciones en Python:
        ZeroDivisionError: Dividir un número entre cero.
        ValueError: Conversión inválida de tipos.
        FileNotFoundError: Archivo inexistente.
        IndexError: Acceso a un índice fuera de rango en una lista.'''

# Estructura de try-except
try:
    # Código que puede generar una excepción
    x = int(input("Ingresa un número: "))
    print(10 / x)
except ZeroDivisionError:
    print("No puedes dividir entre cero.")
except ValueError:
    print("Debes ingresar un número válido.")

# Bloque else: El bloque else se ejecuta si no ocurre ninguna excepción.
try:
    x = int(input("Ingresa un número: "))
except ValueError:
    print("Entrada inválida.")
else:
    print(f"Ingresaste el número: {x}")


#Bloque finally:El bloque finally se ejecuta siempre, ocurra o no una excepción. Es útil para liberar recursos
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("El archivo no existe.")
finally:
    print("Cerrando el programa.")
    archivo.close()

#Capturar excepciones genéricas: Usar except Exception captura cualquier excepción, pero es importante usarlo con precaución para no ocultar errores inesperados.
try:
    resultado = 10 / 0
except Exception as e:
    print(f"Ocurrió un error: {e}")
'''🔑 Buena práctica: Captura excepciones específicas siempre que sea posible para evitar capturar más de lo necesario.'''

#Lanzar excepciones manualmente: Puedes usar raise para generar tus propias excepciones:
x = -5
if x < 0:
    raise ValueError("El número debe ser positivo.")

#Crear excepciones personalizadas: para manejar casos específicos de tu programa.
class MiErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

try:
    raise MiErrorPersonalizado("Este es un error personalizado.")
except MiErrorPersonalizado as e:
    print(f"Error: {e.mensaje}")

#Contexto avanzado: Registrar excepciones en archivos
try:
    x = int("no_numero")
except ValueError as e:
    with open("errores.log", "a") as log:
        log.write(f"Error: {e}\n")

#Reintentar operaciones: En ciertos casos, puedes intentar que el usuario corrija su error:
while True:
    try:
        x = int(input("Ingresa un número: "))
        print(f"Número válido: {x}")
        break
    except ValueError:
        print("Entrada no válida. Intenta de nuevo.")

#Usar librerías como logging
import logging

logging.basicConfig(filename="app.log", level=logging.ERROR)

try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    logging.error(f"Error: {e}")

'''Buenas prácticas para manejo de errores
🔑 Sé específico: Captura excepciones particulares (ZeroDivisionError, ValueError, etc.).
🔑 Evita bloques vacíos: No dejes un bloque except sin manejar el error.
🔑 Documenta las excepciones esperadas: Escribe comentarios o docstrings que describan las excepciones posibles.
🔑 Limpia los recursos: Usa finally para cerrar archivos o liberar memoria.
🔑 Maneja solo lo necesario: No abuses de try-except para cubrir todos los problemas; encuentra y corrige los errores donde se originan.
'''