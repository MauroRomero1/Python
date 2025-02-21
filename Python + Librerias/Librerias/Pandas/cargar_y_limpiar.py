import pandas as pd

df = pd.read_csv(r'C:\Users\CPU\Desktop\Proyectos_Automatizacion\guias_librerias\pandas\datos_edad.csv')
df.dropna(inplace=True) #elimina valores nulos

df=df[df['Edad'] > 18] # Filtrar mayores de edad

print(df.describe())