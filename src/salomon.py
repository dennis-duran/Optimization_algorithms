from scipy.optimize import differential_evolution, dual_annealing
from functions import salomon
import time

start_time = time.time()

D=2
bounds = [(-100, 100) for i in range(D)]

# Aplicar el algoritmo genetico
#result = differential_evolution(salomon, bounds)
result = differential_evolution(salomon, bounds)
end_time = time.time()

# Calcula el tiempo de ejecución
execution_time = end_time - start_time

# Imprime el resultado
print("Solución óptima: ", result.x)
print("Valor de la función objetivo en la solución óptima: ", result.fun)
print("Número de iteraciones: ", result.nit)
print("Tiempo de ejecución: ", execution_time, "segundos")