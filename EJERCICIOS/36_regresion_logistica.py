from sklearn.linear_model import LogisticRegression
import numpy as np
# Datos
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([0, 0, 0, 1, 1])
# Modelo
model = LogisticRegression()
model.fit(X, y)
# Probabilidad de clase
prob = model.predict_proba([[3.5]]) # Probabilidad: [[0.5208689 0.4791311]]
# prob = model.predict([[3.5]]) # Probabilidad: [0]
print("Probabilidad:", prob)
