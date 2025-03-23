import pandas as pd
import sqlite3 
df = pd.read_excel("DataSet/SuperStoreUS-Clean.xlsx", sheet_name="Sheet1")

print(df.head())

conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

# Los clientes pueden repetirse en varias órdenes, así que primero insertamos clientes únicos. y eliminar duplicados
customers = df[["Customer ID", "Customer Name" ,"Segment", "Region"]].drop_duplicates()

# Insertar en sqlite
for _, row in customers.iterrows():
    cursor.execute("""
INSERT OR IGNORE INTO Customers (CustomerID, CustomerName, Segment, Region)
VALUES (?, ?, ?, ?)
()""", (row["Customer ID"], row["Customer Name"], row["Segment"], row["Region"]))

conn.commit()