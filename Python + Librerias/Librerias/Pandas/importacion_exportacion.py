import pandas as pd

#Leer Archivo CSV
df=pd.read_csv('archivo.csv')

#Guardar archivo CSV
df.to_csv('salida.csv', index=False)

#Leer archivo Excel
df= pd.read_excel('archivo.xlsx')

#Guardar archivo Excel
df.to_excel('salida.xlsx', index=False)

#Leer desde SQL
df = pd.read_sql('SELECT * FROM tabla', conexion) # type: ignore
