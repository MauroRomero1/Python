'''4. Programación Orientada a Objetos (POO)
Aprende a trabajar con clases , objetos , herencia , polimorfismo y encapsulamiento .
Por qué es importante : La POO te permite estructurar programas más grandes y complejos.
Ejemplo práctico : Crear simulaciones, juegos o modelos de datos en proyectos.'''

#Clases y Objetos
# Una clase es como un plano o molde para crear objetos.
# Un objeto es una instancia de una clase (algo creado a partir de ese molde).'''

# Definimos una clase
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre  # Atributo
        self.raza = raza      # Atributo
    
    def ladrar(self):         # Método
        print(f"{self.nombre} está ladrando: ¡Guau guau!")

# Crear objetos (instancias)
mi_perro = Perro("Rex", "Pastor Alemán")
otro_perro = Perro("Max", "Labrador")

# Usar atributos y métodos
print(mi_perro.nombre)  # Rex
mi_perro.ladrar()       # Rex está ladrando: ¡Guau guau!
