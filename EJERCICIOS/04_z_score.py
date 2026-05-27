import pandas as pd

datos = [10, 20, 14, 15, 18, 10, 12, 14, 15, 18, 10, 12, 14, 15, 18, 100, 101, 50]

serie = pd.Series(data=datos)

media = serie.mean() # media # 19.68
std = serie.std() # desviación estándar # 21.63

z_scores = (serie - media) / std

umbral = 0.8

outliers = serie[z_scores.abs() > umbral]

print(outliers.values)

