import sqlite3
import pandas as pd

conn = sqlite3.connect("mi_base.db")

df=pd.read_sql("SELECT * FROM usuarios", conn)
print(df)


''' Exportar datos de SQLite a CSV/Excel '''
# Guardar en CSV
df.to_csv("usuarios.csv", index=False)
# Guardar en Excel
df.to_csv("usuarios.xlsx", index=False)

print("Datos exportados correctamente.")
conn.close()