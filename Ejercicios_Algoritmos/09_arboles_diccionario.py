""" 09-Ingresada la especie del árbol, informar su expectativa de vida sabiendo que la especie tipo “A” cuenta con una 
esperanza de vida de 45 años, “B” de 80 años, “C” de 75 años, “D” de 150 años y en cualquier otro caso es 
desconocida."""

especie = input("Ingrese especie de arbol (A/B/C/D): ").upper()

expectativa = {"A" : 45, "B" : 80, "C" : 75, "D" : 150}.get(especie, "Desconocida")
"""
.get() devuelve el valor de una clave si existe en el diccionario.
Si la clave no existe, devuelve un valor por defecto que puedes especificar ("Desconocida") .

"""
print(f"La expectativa de vida de la especie es: {expectativa}")