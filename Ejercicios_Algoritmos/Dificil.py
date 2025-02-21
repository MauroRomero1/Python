'''Algoritmos
1. La comisión de un club desea obtener estadísticas sobre los socios que practican dos deportes. Por 
ello, de cada socio se ingresará: deporte principal, deporte secundario, edad y sexo.
Los deportes pueden ser: tenis, vóley, básquet, natación y futbol.
Al finalizar, informar: 
1-edad promedio de las mujeres que practican voley como principal deporte.
2-cantidad de adolescentes (de 12 a 17 años) que practican tenis y no hacen futbol.
2. El sector de informática tiene la tarea de determinar la cantidad y tipo de impresoras a adquirir para 
renovar las existentes en los 7 deptos. con los que cuenta la empresa. 
Cada empleado de cada depto. indicó la cantidad aprox. de copias que él imprime por mes. 
Al finalizar la carga de datos se deberá informar cuantas impresoras de hasta 1000 pag., cuantas de 
hasta 3000 y cuantas más de 3000 pag. mensuales son necesarias adquirir para cubrir la demanda de 
copias, pensando ubicar una única impresora por depto.
Tener en cuenta que cada impresora debe superar en un 15% la cantidad realmente requerida en el 
depto.
La cantidad de empleados es desconocida y se ingresan ordenados por depto'''


'''1. El directivo de una clínica ha solicitado un informe sobre de los pacientes con covid19. De cada paciente 
se ingresará: Edad, Sexo y Estado (En Tratamiento/Recuperado/Fallecido).
Al finalizar con la carga de datos se pide presentar el informe donde se detalle:
 Edad promedio de los fallecidos.
 Porcentaje de recuperados.
 Cantidad de Mujeres mayores de 60 en tratamiento.
2. El gobierno ha optado por repatriar a todos los turistas argentinos que han quedado varados en 5 países.
Se aprovechará cada vuelo para enviar a dichos países los turistas extranjeros que lo deseen.
Para un país en particular, se ingresará por cada vuelo: cantidad de butacas y cantidad de repatriados 
que allí abordaron.
Indicar para cada destino, la cantidad de vuelos que han retornado con una ocupación inferior al 80%.
Al finalizar la carga de datos, la aplicación deberá informar el destino con mayor cantidad de repatriados.
Tener en cuenta:
 La cantidad de vuelos es desconocida y se ingresan ordenados por destino.
 No hay destinos con igual cantidad de repatriados'''


"""
1)	Diseñar un algoritmo que permita llevar el control del movimiento diario de un balneario costero.

•	El balneario dispone de 250 carpas.
•	De cada una de ellas se indicará, al final del día, si la misma estuvo alquilada ($20000). En caso de que sí se indicará si se contrató algún servicio adicional:
	Alquiler de Sillas: en este caso se agregará la cantidad, el costo por silla es de $300.
	Alquiler de Mesa: el costo es de $1500 (sólo se permite una por carpa).
	Alquiler de Sombrilla: el costo es de $1700 (sólo se permite una por carpa).

Se requiere:
•	El monto que pagará cada cliente.
•	La cantidad de artículos alquilados en total (sin contar las carpas como un artículo, sólo mesa, sillas y sombrillas).
•	El promedio recaudado por carpa (teniendo en cuenta sólo aquellas que fueron alquiladas).

Los datos se presentan ordenados por número de carpa.

"""

'''Un comercio dedicado al expendio de comidas rápidas cuenta con 15 menúes diferentes enumerados 
de 1 a 15. Al iniciar el día se ingresará de cada uno de ellos el precio de venta por única vez. 
En el transcurso del día se irá ingresando de cada pedido: nro de menú solicitado y cantidad de 
unidades. Un pedido puede estar compuesto por varios menús.
Al finalizar la jornada se deberá emitir un listado que presente: Nro de Menú, Recaudación y
Unidades Pedidas, ordenado por recaudación en forma descendente.
Notas: 
Los pedidos ingresados no respetan ningún criterio de ordenamiento. 
Utilizar arreglos, vectores o una única matriz'''