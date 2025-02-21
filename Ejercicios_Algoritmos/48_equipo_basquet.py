'''48-El entrenador de un equipo de básquet desea obtener un listado completo de los jugadores que especifique el 
código del jugador y su efectividad en tiros de campos. Para ello se ingresará de cada uno de los 15 jugadores que 
conforma el plantel, la siguiente información: Código de Jugador (1..15), Intentos y Conversiones. Finalizada la carga de datos, emitir el listado.
El ingreso de datos no respeta ningún criterio de ordenamiento.'''

matrix =[[0,0,0],
         [0,0,0],
         [0,0,0]]

cod = int(input("Ingrese codigo de jugador: "))
while True:
    if cod == 0:
        break
    if 1 <= cod <=3:
        matrix[cod-1][0] = cod
        intentos = int(input("Ingrese intentos: "))
        matrix[cod-1][1] = intentos
        conversiones = int(input("Ingrese Conversiones: "))
        matrix[cod-1][2] = conversiones 
        print(matrix)
        cod = int(input("Ingrese codigo de jugador: ")) 
    continue       
for jugardor in matrix:
    print(f"Jugador numero: {jugardor[0]}")
    print(f"Intentos : {jugardor[1]}")
    print(f"Conversiones : {jugardor[2]}")