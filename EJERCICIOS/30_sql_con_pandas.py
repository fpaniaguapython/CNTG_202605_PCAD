import sqlite3

import pandas as pd

DB_NAME='db_empleados_optimizado.sqlite3'
conn = sqlite3.connect(database=DB_NAME)
df = pd.read_sql(sql="SELECT * FROM empleados WHERE categoria_programacion='Ingeniero de Software' AND ciudad='Barcelona'",
                 con=conn)
print(df.info())
print(df.head())

conn.close()
