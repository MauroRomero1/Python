'''53-El organizador de una fiesta cuenta con la lista de invitados (450) la cual se encuentra totalmente desordenada, y 
en ella se detalla: DNI y Número de mesa. Una vez finalizada la carga de la lista al sistema, al momento de llegar un invitado, se ingresará su DNI y si el mismo es hallado se le indicará el número de mesa que le corresponde.
La cantidad de consultas no está determinada, en caso de no encontrarse registrado el invitado se deberá emitir el 
alerta correspondiente. Implementar búsqueda dicotómica.'''

def busqueda_binaria(lista, dni):
    """búsqueda binaria en la lista de invitados ordenada por DNI."""
    inicio = 0 
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin)/2
        if lista[medio][0] == dni:
            return lista[medio][1] #num mesa
        elif lista[medio][0] < dni:
            inicio = medio + 1 
        else:
            fin = medio + 1
    return None #si no encuentra dni

import random

invitados = [(random.randint(10000000, 50000000), random.radint(1,30)) for _ in range(450)]
invitados.sort() #ordena la lista por dni

while True:
    try:
        dni_consulta = int(input("Ingrese DNI o (0 para salir):"))
        if dni_consulta == 0:
            break
        
        resultado = busqueda_binaria(invitados, dni_consulta)

        if resultado is not None:
            print(f"Invitado encontrado. Su numero de mesa es: {resultado}.")
        else:
            print('invitado no encontrado.')
    except ValueError:
        print("Por favor, ingrese numero de dni valido.")
print("Fin")
