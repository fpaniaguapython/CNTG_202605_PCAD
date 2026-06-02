import statistics
import sqlite3

import pandas as pd
import numpy as np

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

# Media con Python
print('Media:',statistics.mean(lista_python))
# Mediana con Numpy
print('Mediana:', np.median(serie_np))
# Moda con Pandas
print('Moda:', serie_pandas.mode())
# Desviación estándar con Python
print('Desviación estándar poblacional con Python:', statistics.pstdev(lista_python))
print('Desviación estándar poblacional con NumPy:', np.std(serie_np))
print('Desviación estándar poblacional con Pandas:', serie_pandas.std(ddof=0))

conn.close()