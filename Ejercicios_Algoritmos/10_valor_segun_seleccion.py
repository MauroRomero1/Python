"""
10-Una automotriz desea determinar el precio de venta adecuado para una línea nueva donde el cliente puede 
seleccionar el color del mismo y su tapizado. Para ello se deberán tener en cuenta las siguientes tablas: 
Valor Auto
    Auto $ 5000
Color Importe
    Negro $ 250
    Rojo $ 200
    Blanco $ 180
    Azul $ 190

Tapizado Importe
    Vinilo $ 150
    Cuero $ 750
    Tela $ 200
"""
auto = 5000

color= input("Ingresa un color del auto (Negro/Rojo/Blanco/Azul): ").lower()
tapizado = input("Ingrese el tipo de tapizado (vinilo/Cuero/tela): ").lower()

precio_color= { "negro" : 250, "rojo" : 200, "blanco" : 180, "azul" : 190}

precio_tapizado = { "vinilo" : 150, "cuero" : 750, "tela" : 200}

precio_total = auto + precio_color.get(color, 0) + precio_tapizado.get(tapizado, 0)

print(f"El precio total del auto es: ${precio_total}")