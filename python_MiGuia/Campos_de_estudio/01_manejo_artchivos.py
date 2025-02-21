'''1. Manejo de Archivos
Aprende a leer, escribir y manipular archivos.
Métodos importantes: open(), read(), write(), with.
Ejemplo práctico : Procesar datos de archivos CSV, logs o configuraciones.
'''
# ABRIR archivos
archivo = open("nombre_archivo", "modo")

"""
Modo |	Descripción
"r"	 |   Modo lectura (predeterminado). Error si no existe.
"w"	 |   Modo escritura. Crea el archivo o lo sobrescribe.
"a"	 |   Modo agregar. Crea el archivo si no existe.
"x"	 |   Modo crear. Error si el archivo ya existe.
"b"	 |   Modo binario (ej.: imágenes, videos).
"t"	 |   Modo texto (predeterminado).
 --  |   ---------------------------
"r+" |   Permite leer y escribir en un archivo.
"r+" |   Sobrescribe el archivo si ya existe o lo crea si no existe.
"r+" |  Agregar contenido al final del archivo y también leerlo.
"x+" |  Permite crear un archivo nuevo y escribir en él.
 --- '  ------------------------
 
 Modos binarios combinados
Modo  |	Descripción
"rb"  |	Leer un archivo binario. Error si no existe.
"wb"  |	Escribir en un archivo binario. Lo sobrescribe o lo crea si no existe.
"ab"  |	Agregar a un archivo binario. Lo crea si no existe.
"r+b" |	Leer y escribir en un archivo binario. Error si no existe.
"w+b" |	Escribir y leer en un archivo binario. Lo sobrescribe o lo crea si no existe.
"a+b" |	Agregar y leer en un archivo binario. Lo crea si no existe.

 """
# LEER archivos
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Leer línea por línea:
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())  # `.strip()` elimina espacios en blanco y saltos de línea.

# Leer líneas como una lista:
with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)  # Cada línea será un elemento de la lista.

# SOBREESCRIBIR archivos  ("w")

with open("archivo.txt", "w") as archivo:
    archivo.write("Esto sobrescribe el archivo.\n")
    archivo.write("Línea adicional.")

# AGREGAR contenido ("a"):
with open("archivo.txt", "a") as archivo:
    archivo.write("\nEsto se agrega al final.")

# CREAR un archivo ("x"): para crearlo
try:
    with open("nuevo_archivo.txt", "x") as archivo:
        archivo.write("Este archivo fue creado.")
except FileExistsError:
    print("El archivo ya existe.")

# Manejo de archivos binarios ("b")
with open("imagen.jpg", "rb") as archivo:
    contenido = archivo.read()
    print(contenido)  # Muestra bytes del archivo.

#- Escribir binario:
with open("copia_imagen.jpg", "wb") as archivo:
    archivo.write(contenido)

# CERRAR archivos
archivo = open("archivo.txt", "r")
contenido = archivo.read()
archivo.close()

#ELIMINAR archivos
import os

if os.path.exists("archivo.txt"):
    os.remove("archivo.txt")
else:
    print("El archivo no existe.")

#Renombrar o mover archivos: 
os.rename("archivo_viejo.txt", "archivo_nuevo.txt")
os.replace("archivo.txt", "nueva_ruta/archivo.txt")


"""
Errores comunes con modos avanzados
    Sobrescribir archivos sin intención:
        Usar "w" o "w+" elimina el contenido previo del archivo.
        Usa "r+" o "a+" si necesitas conservar el contenido.
    Trabajar con archivos inexistentes:
        "r" o "r+" dan error si el archivo no existe.
        Usa "a" o "w" para crearlo si no estás seguro de su existencia.
    Error con "x":
        "x" o "x+" fallan si el archivo ya existe.
"""