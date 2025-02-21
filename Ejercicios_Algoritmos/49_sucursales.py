'''49-Mega S.A. es una empresa que cuenta con 3 sucursales (código: 1, 2 ,3). El contador posee en sus manos un listado 
en el que figuran los ingresos y egresos que afectaron a cada sucursal. Una vez registrados, se deberán listar las 
sucursales ordenadas en forma creciente según el saldo en caja, junto con la cantidad de ingresos y egresos de la 
misma, finalmente informar el saldo promedio en ellas.
Los datos no respetan ningún criterio de ordenamiento y una sucursal puede figurar con múltiples ingresos y egresos.'''

sucursales = [[0,0],
              [0,0],
              [0,0]]
promedio = 0
while True: 
    sucursal = int(input('Ingrese sucursal: '))
    if sucursal == 0:
        break
    accion = input('Precione (i)ingreso o (e)egreso: ').upper()
    if accion == 'I':
        monto = int(input('Ingrese monto: '))
        sucursales[sucursal-1][0] = sucursales[sucursal-1][1] + monto
    if accion == 'E':
        monto = int(input('Ingrese monto: '))
        sucursales[sucursal-1][1] = sucursales[sucursal-1][1] - monto
    continue
for sucursal in sucursales:
    print(f'Ingresos: {sucursal[0][0]}')
    print(f'Egresos: {sucursal[0][1]}')
    tot = sucursal[sucursal][1] + sucursal[sucursal][0]
    promedio += tot
    print(f'Total: {tot}')



print(f'Promedio : {promedio/3}')
