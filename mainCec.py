import numpy as np
import pandas as pd
import time

from Algorithms.GeneticAlgorithm import GeneticAlgorithm
from Problems.Cec2017 import Cec2017
from Problems.cec2017.cec2017.functions import all_functions

# ======= Funciones de selección =======
def select_universal(g): return g.selection_functions.universalRandom
def select_tournament(g): return g.selection_functions.tournament
def select_proportional(g): return g.selection_functions.proportional
def select_negative(g): return g.selection_functions.negativeAssortativeMating

# ======= Funciones de cruza binaria =======
def cross_one_point(g): return g.crossover_functions.onePoint
def cross_two_point(g): return g.crossover_functions.twoPoint
def cross_uniform(g): return g.crossover_functions.uniform

# ======= Funciones de cruza real =======
def cross_arithmetic(g): return g.crossover_functions.arithmetic
def cross_blend(g): return g.crossover_functions.blend
def cross_sim_binary(g): return g.crossover_functions.simulatedBinary

# ======= Funciones de cruza permutación =======
def cross_uniform_order(g): return g.crossover_functions.uniformOrderBased
def cross_order_based(g): return g.crossover_functions.orderBased

# ======= Funciones de mutación =======
def mutate_single_point(g): return g.mutation_functions.singlePoint

# ======= Funciones de reemplazo =======
def replace_random(g): return g.replace_functions.random
def replace_elitism(g): return g.replace_functions.elitism
def replace_determinist(g): return g.replace_functions.deterministCrowding
def replace_restricted(g): return g.replace_functions.restrictedTournament

# === Mapear strings a funciones reales ===
selection_map = {
    "UniversalRandom": select_universal,
    "Proportional": select_proportional,
    "Tournament": select_tournament
}

crossover_map = {
    "Blend": cross_blend,
    "Arithmetic": cross_arithmetic
}

mutation_map = {
    "SinglePoint": mutate_single_point
}

replacement_map = {
    "RestrictedTournament": replace_restricted,
    "DeterministCrowding": replace_determinist,
    "Elitism": replace_elitism
}

# === Cargar la mejor configuración por función ===
best_configs = {
    1:  {"stationary": 0.0, "selection": "UniversalRandom", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "RestrictedTournament"},
    2:  {"stationary": 0.0, "selection": "Proportional", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "DeterministCrowding"},
    3:  {"stationary": 0.6, "selection": "Tournament", "crossover": "Arithmetic", "mutation": "SinglePoint", "replacement": "RestrictedTournament"},
    4:  {"stationary": 0.0, "selection": "Proportional", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "DeterministCrowding"},
    5:  {"stationary": 0.0, "selection": "Proportional", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "DeterministCrowding"},
    6:  {"stationary": 0.0, "selection": "Proportional", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "DeterministCrowding"},
    7:  {"stationary": 0.0, "selection": "Proportional", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "RestrictedTournament"},
    8:  {"stationary": 0.0, "selection": "Proportional", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "DeterministCrowding"},
    9:  {"stationary": 0.2, "selection": "Proportional", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "DeterministCrowding"},
    10: {"stationary": 0.0, "selection": "UniversalRandom", "crossover": "Blend", "mutation": "SinglePoint", "replacement": "Elitism"},
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

    # Crear GA con configuración vacía
    ga = GeneticAlgorithm(problem=cec, population_size=32)
    ga.stationary = config["stationary"]

    # Asignar operadores
    ga.setSelection(selection_map[config["selection"]])
    ga.setCrossover(crossover_map[config["crossover"]])
    ga.setMutation(mutation_map[config["mutation"]])
    ga.setReplace(replacement_map[config["replacement"]])

    solutions = []
    times = []

    for _ in range(20):
        ga.resetProblem()
        start = time.time()
        ga.optimize(100)
        end = time.time()

        times.append(end - start)
        solutions.append(float(ga.bestIndividual()))

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
pd.DataFrame(results_dataset).to_csv("results/energy_GA_CEC2017.csv", index=False)
pd.DataFrame(time_dataset).to_csv("results/time_GA_CEC2017.csv", index=False)

# === Mostrar en consola ===
print("=== Resultados ===")
print(pd.DataFrame(results_dataset))
print("\n=== Estadísticas de Tiempos ===")
print(pd.DataFrame(time_dataset))
