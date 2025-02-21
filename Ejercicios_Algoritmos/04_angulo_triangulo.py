"""04-Ingresados los ángulos de un triangulo, informar si el mismo es un triangulo rectángulo."""

a = float(input("Ingresa lado a del triangulo: "))
b = float(input("Ingresa lado b del triangulo: "))
c = float(input("Ingresa lado c del triangulo: "))

if a + b + c == 180 and ( 90 in [a, b, c]):
    print("El triangulo es rectangulo.")
else: 
    print("El triangulo no es rectangulo.")