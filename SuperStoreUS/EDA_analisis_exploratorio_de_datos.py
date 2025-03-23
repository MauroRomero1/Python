import pandas as pd
import matplotlib.pyplot as plt
file_path = "DataSet/SuperStoreUS-Clean.xlsx"
xls = pd.ExcelFile(file_path)

print("Hojas del archivo", xls.sheet_names)

df=xls.parse("Orders")
print("Columns", df.columns)
# Guardar con el nuevo nombre de hoja "Orders"
'''with pd.ExcelWriter(file_path, engine="openpyxl", mode="w") as writer:
    df.to_excel(writer, sheet_name="Orders", index=False)'''

# Obtener estadísticas descriptivas
print(df.describe(include="all"))

# Contar valores únicos en columnas categóricas
print(df["Product Category"].value_counts())

# Detectar valores atípicos en ventas o ganancias con gráficos de caja
df.boxplot(column = ["Sales", "Profit"])
plt.show()

#Correlación entre ventas y ganancias
print(df[["Sales", "Profit"]].corr())
