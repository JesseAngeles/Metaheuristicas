import numpy as np
import pandas as pd
import time

from Algorithms.GeneticAlgorithm import GeneticAlgorithm
from Problems.Cec2017 import Cec2017
from Problems.cec2017.cec2017.functions import all_functions

# Datasets separados
results_dataset = []
time_dataset = []

# Iterar sobre funciones
for i in range(11):
    dimension = 100
    function = all_functions[i]

    cec = Cec2017(function=function, dimention=dimension)
    ga = GeneticAlgorithm(cec, 32)

    solutions = []
    times = []

    for _ in range(20):
        ga.resetProblem()
        start = time.time()
        ga.optimize(100)
        end = time.time()

        times.append(end - start)
        solutions.append(float(ga.bestIndividual()))

    # Resultados de la función
    results_dataset.append({
        "function_id": i + 1,
        "best": np.min(solutions),
        "worst": np.max(solutions),
        "mean": np.mean(solutions),
        "median": np.median(solutions),
        "std_dev": np.std(solutions)
    })

    # Estadísticas de tiempos
    time_dataset.append({
        "function_id": i + 1,
        "min_time_sec": np.min(times),
        "max_time_sec": np.max(times),
        "mean_time_sec": np.mean(times),
        "median_time_sec": np.median(times),
        "std_time_sec": np.std(times)
    })

# Guardar archivos
pd.DataFrame(results_dataset).to_csv("Resultados_GA_CEC2017.csv", index=False)
pd.DataFrame(time_dataset).to_csv("Tiempo_Ejecucion_GA_CEC2017.csv", index=False)

# Mostrar en consola
print("=== Resultados ===")
print(pd.DataFrame(results_dataset))
print("\n=== Estadísticas de Tiempos ===")
print(pd.DataFrame(time_dataset))
