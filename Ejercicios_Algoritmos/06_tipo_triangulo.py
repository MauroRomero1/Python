a = float(input("Ingrese el primer lado del triangulo: "))
b = float(input("Ingrese el segundo lado del triangulo: "))
c = float(input("Ingrese el tercer lado del triangulo: "))

if a == b == c:
    print("el triangulo es quilatero. ")
elif a == b or a == c or b == c:
    print("el triangulo es isosceles. ")
else: 
    print("el tringulo es escalento. ")