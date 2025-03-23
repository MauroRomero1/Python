import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  

file_path ="DataSet/SuperStoreUS-Clean.xlsx"
xls = pd.ExcelFile(file_path)
df = xls.parse("Orders")

#Identificar los productos más vendidos y los más rentables

top_products = df.groupby("Product Name")[["Sales", "Profit"]].sum().sort_values(by="Sales", ascending=False)
print(top_products.head(10))

#Evaluar Rentabilidad por categoria
category_profit = df.groupby("Product Category")["Profit"].sum()
print(category_profit)

#Visualización de Datos sns y plt
sns.barplot(x="Product Category", y="Sales", data=df)  
plt.xticks(rotation=45)
plt.show()


# Matplotlib (más código, menos estilizado por defecto)
df["Product Category"].value_counts().plot(kind="bar", color="skyblue", edgecolor="black")
plt.title("Ventas por Categoría")
plt.xlabel("Categoría")
plt.ylabel("Cantidad de Ventas")
plt.xticks(rotation=45)
plt.show()


# Seaborn (más simple, mejor diseño por defecto)
sns.set_theme(style="whitegrid")  
sns.barplot(x=df["Product Category"].value_counts().index, y=df["Product Category"].value_counts().values, palette="viridis")  
plt.title("Ventas por Categoría")  
plt.xticks(rotation=45)
plt.show()