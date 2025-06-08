import numpy as np
import pandas as pd
import time

from Algorithms.Axolotl import Axolotl

from Problems.Cec2017 import Cec2017
from Problems.cec2017.cec2017.functions import all_functions

# === Carmaor la mejor configuración por función ===
best_configs = {
    1:  {"damage": 1.0, "regeneration": 0.8, "tournament": 2, "alpha": 0.2},
    2:  {"damage": 1.0, "regeneration": 0.8, "tournament": 10, "alpha": 0.6},
    3:  {"damage": 0.6, "regeneration": 0.8, "tournament": 2, "alpha": 0.4},
    4:  {"damage": 1.0, "regeneration": 1.0, "tournament": 2, "alpha": 0.0},
    5:  {"damage": 0.8, "regeneration": 0.2, "tournament": 6, "alpha": 0.6},
    6:  {"damage": 0.8, "regeneration": 0.6, "tournament": 2, "alpha": 0.4},
    7:  {"damage": 0.8, "regeneration": 1.0, "tournament": 2, "alpha": 0.2},
    8:  {"damage": 0.4, "regeneration": 0.6, "tournament": 4, "alpha": 0.2},
    9:  {"damage": 0.2, "regeneration": 0.0, "tournament": 2, "alpha": 0.2},
    10: {"damage": 0.8, "regeneration": 0.2, "tournament": 6, "alpha": 0.4},
}

# === Inicialización de datasets ===
results_dataset = []
time_dataset = []

# === Ejecución por función ===
for i in range(11):
    func_id = i + 1
    if func_id not in best_configs:
        print(f"Skipping function {func_id} (no config)")
        continue

    config = best_configs[func_id]
    dimension = 100
    function = all_functions[i]
    cec = Cec2017(function=function, dimention=dimension)

    # Crear mao con configuración vacía
    mao = Axolotl(problem=cec, population_size=32, 
                  damage= config["damage"], 
                  regeneration= config["regeneration"],
                  tournament_size=config["tournament"],
                  alpha=config["alpha"])

    solutions = []
    times = []

    mao.best()

    for _ in range(20):
        mao.resetProblem()
        start = time.time()
        mao.optimize(100)
        end = time.time()

        times.append(end - start)
        solutions.append(float(mao.best()))

    # Guardar resultados
    results_dataset.append({
        "function_id": func_id,
        "best": np.min(solutions),
        "worst": np.max(solutions),
        "mean": np.mean(solutions),
        "median": np.median(solutions),
        "std_dev": np.std(solutions)
    })

    time_dataset.append({
        "function_id": func_id,
        "min_time_sec": np.min(times),
        "max_time_sec": np.max(times),
        "mean_time_sec": np.mean(times),
        "median_time_sec": np.median(times),
        "std_time_sec": np.std(times)
    })

# === Guardar en CSV ===
pd.DataFrame(results_dataset).to_csv("results/energy_mao_CEC2017.csv", index=False)
pd.DataFrame(time_dataset).to_csv("results/time_mao_CEC2017.csv", index=False)

# === Mostrar en consola ===
print("=== Resultados ===")
print(pd.DataFrame(results_dataset))
print("\n=== Estadísticas de Tiempos ===")
print(pd.DataFrame(time_dataset))
