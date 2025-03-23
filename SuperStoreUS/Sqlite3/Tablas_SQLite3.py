import sqlite3

conn = sqlite3.connect("superstore.db")
cursor = conn.cursor()

# Activar claves foráneas
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders(
               OrderID TEXT PRIMARY KEY,
               OrderDate DATE,
               CustomerID TEXT,
               Sales REAL,
               Profit REAL,
               ProductID TEXT, 
               Quantity INTEGER, 
               Discount REAL,
               FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
               FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers(
               CustomerID TEXT PRIMARY KEY,
               CustomerName TEXT, 
               Segment TEXT,
               Region TEXT
)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS products(
               ProductID TEXT PRIMARY KEY,
               ProductName TEXT, 
               Category TEXT,
               SubCategory TEXT
)""")
conn.commit()
conn.close()
print("Tablas creadas con éxito.")

