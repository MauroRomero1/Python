'''Pandas permite realizar gráficos de forma rápida usando Matplotlib'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'C:\Users\CPU\Desktop\Proyectos_Automatizacion\guias_librerias\pandas\datos_edad.csv')

df['Edad'].plot(kind='bar')
plt.show()
