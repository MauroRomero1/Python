import sqlite3
conn = sqlite3.connect("mi_base.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               edad INTEGER);
""")
conn.commit()
conn.close()

