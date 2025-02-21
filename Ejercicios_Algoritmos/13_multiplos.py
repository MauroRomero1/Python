"""13-Generar e informar los primeros N múltiplos de un número M entero."""
def enteros():
    N = int(input("Ingrese la cantidad de multiplos a generar: "))
    M =  int(input("Ingrese el valor: "))

    for i in range(1, N+1):
        print(f" {i} x {M} = {i*M}")
enteros()
