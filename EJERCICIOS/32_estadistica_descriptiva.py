import sqlite3

import pandas as pd

DB_NAME='db_empleados_optimizado.sqlite3'
conn = sqlite3.connect(database=DB_NAME)
df = pd.read_sql(sql="SELECT categoria_programacion, ciudad, salario \
                 FROM empleados WHERE ciudad='Madrid'",
                 con=conn)

lista_python = df['salario'].to_list()
serie_pandas = df['salario']
serie_np = df['salario'].to_numpy()
print(type(lista_python)) # list
print(type(serie_pandas)) # pandas.Serie
print(type(serie_np)) # numpy.ndarry

conn.close()