import pandas as pd 


# Cargar el archivo
file_path = "DataSet/SuperStoreUS-2015.xlsx"
xls = pd.ExcelFile(file_path)

# Ver hojas disponibles
print("Hojas en el archivo", xls.sheet_names)


# Cargar la primera hoja (Orders)
df = xls.parse("Orders")

# Tamaño del DataFrame 
print("Filas y columnas:",df.shape)

# Ver primeras filas
print(df.head(2))

# Ver información general
print(df.info())

# Datos Faltantes o Erróneos
print(df.isnull().sum())

# Rellenar con el promedio
'''df["Product Base Margin"].fillna(df["Product Base Margin"].mean(), inplace=True)'''

# Rellenar con valor fijo( cero )
df["Product Base Margin"] = df["Product Base Margin"].fillna(0)

print(df.isnull().sum())

# Revisar Formato de Datos (Fechas, Números, Texto)
''' 
Errores comunes en Excel:
    Fechas en formato texto en vez de datetime.
    Números como texto, lo que impide cálculos.
'''


#Convertir fechas
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")



df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")

# Asegurar que Ventas es numérico
df["Sales"] = pd.to_numeric(df["Sales"],errors="coerce")

df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
"""errors="coerce" convertirá fechas inválidas en NaT"""
# Eliminar Duplicados
df.drop_duplicates(inplace = True)

df.to_csv("DataSet/SuperStoreUS-Clean.csv", index=False)
df.to_excel("DataSet/SuperStoreUS-Clean.xlsx", index=False)

print(df.dtypes)