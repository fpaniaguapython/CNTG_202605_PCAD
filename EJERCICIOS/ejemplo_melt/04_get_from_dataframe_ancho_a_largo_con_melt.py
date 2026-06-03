import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leer CSV
df = pd.read_csv("./datos_ventas_ancho.csv")

# Convertir a formato largo
df_long = df.melt(
    id_vars="mes",
    var_name="comunidad",
    value_name="ventas"
)
df_long.head()

# Gráfico
plt.figure(figsize=(14, 6))

sns.barplot(
    data=df_long,
    x="mes",
    y="ventas",
    hue="comunidad"
)

plt.title("Ventas por comunidad y mes")
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.legend(title="Comunidad", bbox_to_anchor=(1.05, 1), loc="upper left")
plt.tight_layout()

plt.show()

