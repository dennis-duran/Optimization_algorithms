import numpy as np
from scipy.optimize import minimize
import time
from functions import rosenbrock

start_time = time.time()

D=2

# Punto de inicio para la optimización
x0 = np.random.uniform(low=-30, high=30, size=D)
bounds = [(-30, 30) for i in range(D)]

# Función para la optimización con el método BFGS
result = minimize(rosenbrock, x0, method="BFGS", bounds=bounds)

end_time = time.time()

# Imprimir resultados
print("Resultado de la optimización:")
print("Valor óptimo de la función:", result.fun)
print("Número de iteraciones:", result.nit)
print("Tiempo de ejecución: ", end_time - start_time, "segundos")
print("Punto óptimo:", result.x)
