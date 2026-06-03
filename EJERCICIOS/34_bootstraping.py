import numpy as np
# Datos originales
data = np.array([10, 12, 13, 15, 18, 20])
# Número de remuestras
n_boot = 1000
# Almacenar medias
boot_means = []
for _ in range(n_boot):
    sample = np.random.choice(data, size=len(data), replace=True)
    boot_means.append(np.mean(sample))
    print(sample)
# Resultados
print("Media bootstrap:", np.mean(boot_means))
print("Error estándar:", np.std(boot_means))