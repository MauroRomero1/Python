import pandas as pd
#Leer Archivo CSV
df=pd.read_csv('archivo.csv')
df2=pd.read_csv('archivo2.csv')

# Combinar DataFrames
df.marge(df2, on='id', how='inner')

# Tablas dinamicas

df.pivot_table(values='Edad', index='Ciudad', aggfunc='mean')

# Aplicacion de funciones

df['Edad'] = df['Edad'].apply(lambda x:x *2) # Duplicar valores de Edad