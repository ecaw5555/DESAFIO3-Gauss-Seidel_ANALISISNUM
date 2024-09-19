import numpy as np
A = np.array([[0.52, 0.20, 0.25],
              [0.30, 0.50, 0.20],
              [0.18, 0.30, 0.55]])
b = np.array([4800, 5810, 5690])
x = np.zeros(len(b))
num_itera = 100
tolerancia = 0.0005
for it in range(num_itera):
    x_old = x.copy()   
    for i in range(len(b)):
        sum_ax = np.dot(A[i, :], x) - A[i, i] * x[i]
        x[i] = (b[i] - sum_ax) / A[i, i]
    if np.allclose(x, x_old, atol=tolerancia):
        print(f"Convergencia en {it + 1} iteraciones")
        break
print("Solución:")
print(f"Cantera 1: {x[0]:.2f} m³")
print(f"Cantera 2: {x[1]:.2f} m³")
print(f"Cantera 3: {x[2]:.2f} m³")
