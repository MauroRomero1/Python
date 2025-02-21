import pandas as pd
#Leer Archivo CSV
df=pd.read_csv('archivo.csv')

""" ACCEDER A LAS COLUMNAS """

df['Nombre']  # Devuelve una Serie

df[['Nombre', 'Edad']]  # Devuelve un DataFrame

""" ACCEDER A LAS FILAS """

df.loc[0]   # Accede por índice de etiqueta
df.iloc[1]  # Accede por posición numérica

""" FILATRAR DATOS """

df[df['Edad']>25]


