# 15-Ingresar un número y exhibir su factorial.


def factorial():
    numero = int(input("Ingrese un numero: "))
    total= 1
    for i in range(1, numero+1):
        total = total * i
    print(f"El factorial de {numero} es {total}")    
factorial()
