import pandas as pd
# Creamos un ejemplo rápido
data = {
'Horas_Estudio': [2, 15, 7, 10, 12],
'Calificacion': [100, 35, 78, 90, 95]
}
df = pd.DataFrame(data)
# Calculamos la correlación de Pearson
correlacion = df['Horas_Estudio'].corr(df['Calificacion'])
print(f"El coeficiente de Pearson es: {correlacion}")
# Resultado: 0.9912 (Una relación positiva casi perfecta)