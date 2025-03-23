import pandas as pd

df = pd.read_excel("DataSet/SuperStoreUS-Clean.xlsx", sheet_name="Sheet1")


# Encontrar productos con margen de ganancia menor al 10%
# - Calcular el margen de ganancia
df["Profit Margin"]= (df["Profit"]/df["Sales"])*100

# - Filtrar productos con margen bajo
productos_no_rentables  = df[df["Profit Margin"]<10]

""" Ranking de Productos """
# Contar la cantidad de ventas por producto
ranking_ventas = df.groupby("Product Name").agg({"Sales":"sum", "Order ID":"count"}).reset_index()
ranking_ventas.rename(columns = {"Order ID":"Cantidad Vendida"}, inplace=True)
# Ordenar de mayor a menor
ranking_ventas = ranking_ventas.sort_values(by="Sales", ascending=False)

""" Rentabilidad por categoría """

df_categoria = df.groupby("Product Category").agg({
    "Sales":"sum",
    "Profit":"sum"
}).reset_index()

df_categoria["Profit_Margin(%)"] = (df_categoria["Profit"]/df_categoria["Sales"]) * 100

#Guardar en un archivo excel 
with pd.ExcelWriter("Reportes_Ventas.xlsx", engine="openpyxl") as writer:
    productos_no_rentables.to_excel(writer, sheet_name= "Productos_no_rentables")
    ranking_ventas.to_excel(writer, sheet_name="Ranking_Ventas")
    df_categoria.to_excel(writer, sheet_name="Rentabilidad_Categoria")
