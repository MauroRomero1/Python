import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear una Serie y un DataFrame
serie = pd.Series([1, 2, 3])
print(serie)

df = pd.DataFrame({'columna1': [1, 2, 3, 4], 'columna2': ['a', 'b', 'c', 'd']})
print(df)

# Tamaño del DataFrame
print("Filas y columnas:", df.shape)

# Cargar DataFrame desde un archivo
df = pd.read_csv('iris/iris.data', header=None)

# Definir nombres de columnas
columnas = ['longitud_sepalo', 'ancho_sepalo', 'longitud_petalo', 'ancho_petalo', 'clase']
df.columns = columnas

# Mostrar información del DataFrame
print("Primeras dos filas:\n", df.head(2))
print("Últimas dos filas:\n", df.tail(2))
print("Columnas:\n", df.columns)
print("Índice:\n", df.index)
print("Estadísticas básicas de cada columna:\n", df.describe())
print("Cantidad de casos de cada clase:\n", df['clase'].value_counts())
print("Invertir columnas y filas:\n", df.T)

# Ordenar DataFrame de forma descendente por ancho_sepalo
df_ordenado = df.sort_values('ancho_sepalo', ascending=False)
print("Ordenado por ancho_sepalo:\n", df_ordenado)

# Seleccionar columnas específicas
print("\nSelección de columnas:\n", df[['longitud_sepalo', 'ancho_sepalo']])

# Selección de filas y columnas específicas
print("Filas específicas (4 y 10):\n", df.iloc[[4, 10]])
print("Filas y columnas específicas (fila 4 y 10, columna 0 y 2):\n", df.iloc[[4, 10], [0, 2]])

# Aplicar filtros
print("Filas con longitud_sepalo > 5:\n", df[df['longitud_sepalo'] > 5])
print("Filas con longitud_sepalo > 5 y longitud_petalo < 4:\n", df[(df['longitud_sepalo'] > 5) & (df['longitud_petalo'] < 4)])

# Operaciones con columnas
print("Restar valores:\n", df['longitud_sepalo'] - df['longitud_petalo'])

# Manejo de valores nulos
df.loc[:1, 'longitud_petalo'] = np.nan  # Usar loc para evitar el warning
print("Cantidad de valores nulos:\n", df.isna().sum())
df['longitud_petalo'] = df['longitud_petalo'].fillna(2)  # Reemplazo de nulos
print(df.head())

# Funciones estadísticas
print("Media:\n", df['longitud_petalo'].mean())
print("Mediana:\n", df['longitud_petalo'].median())

# Aplicar funciones con apply
print("Valores negativos:\n", df['longitud_petalo'].apply(lambda x: -x))
print("Cuadrado de los valores:\n", df['longitud_petalo'].apply(lambda x: x**2))

# Agrupar por clase y calcular media del ancho_petalo
df_group = df.groupby('clase')['ancho_petalo'].mean()
df_group.name = 'media_ancho_petalo'

# Unir el DataFrame original con la media calculada
df_join = df.join(df_group, on='clase', how='inner')
print(df_join)

# Gráfica de la media del ancho_petalo por clase
df_join['media_ancho_petalo'].plot()
plt.show()

df_join['longitud_petalo'].plot()
plt.show()

df_join.plot()
plt.show()

df_join['longitud_petalo'].plot(kind='bar')
plt.show()