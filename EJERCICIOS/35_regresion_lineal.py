from sklearn.linear_model import LinearRegression
import numpy as np
# Datos
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])
# Modelo
model = LinearRegression()
model.fit(X, y)
# Predicción
prediction = model.predict([[6]])
print("Coeficiente:", model.coef_)
print("Intercepto:", model.intercept_)
print("Predicción:", prediction)