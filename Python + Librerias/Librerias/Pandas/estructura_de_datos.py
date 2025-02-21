import pandas as pd

""" SERIE (Datos Unidimensionales )"""
#Las series en pandas son como arreglos unidimencionales con un indice

data = [10,20,30,40]
serie = pd.Series(data, index=['a','b','c','d'])
print(serie)

'''
salida: 
a    10
b    20
c    30
d    40
dtype: int64'''

""" DataFrame (Datos tabulares) """

#Un DataFrame es una tabla bidimensional (como una hoja de cálculo de Excel).
data = {'Nombre':['Ana','Juan','Pablo'], 'Edad':[25,30,35],'Ciudad':['Argentina','Uruguay','Peru']}

df= pd.DataFrame(data)

print(df)
""" salida:
  Nombre  Edad     Ciudad
0    Ana    25  Argentina
1   Juan    30    Uruguay
2  Pablo    35       Peru
"""