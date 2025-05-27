import csv
import statistics
import numpy as np
import multiprocessing as mp

from Algorithms.GeneticAlgorithm import GeneticAlgorithm
from Problems.KnapsackProblem import KnapsackProblem
from Problems.TravelSalesmanProblem import TravelSalesManProblem
from Problems.SumFunctionProblem import SumFunctionProblem

from Problems.Cec2017 import Cec2017  # Asegúrate de tener esta clase bien definida
import os

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

# ======= FUNCIÓN GLOBAL fuera de main_cec2017 =======
def run_cec_iteration(args):
    function, dimension, sel_func, cross_func, mut_func, rep_func, stationary, epochs = args
    cec = Cec2017(function=function, dimention=dimension)
    ga = GeneticAlgorithm(cec, 32)
    ga.setSelection(sel_func(ga))
    ga.setCrossover(cross_func(ga))
    ga.setMutation(mut_func(ga))
    ga.setReplace(rep_func(ga))
    ga.optimize(epochs, stationary)
    return ga.bestIndividual()

def main_cec2017():
    from Problems.cec2017.cec2017.functions import all_functions

    selection = {
        "UniversalRandom": select_universal,
        "Tournament": select_tournament,
        "Proportional": select_proportional,
        "NegativeAssortative": select_negative
    }

    crossover_real = {
        "Arithmetic": cross_arithmetic,
        "Blend": cross_blend,
        "SimulatedBinary": cross_sim_binary
    }

    mutation = {
        "SinglePoint": mutate_single_point
    }

    replace = {
        "Random": replace_random,
        "Elitism": replace_elitism,
        "DeterministCrowding": replace_determinist,
        "RestrictedTournament": replace_restricted
    }

    iterations = 100
    epochs = 1000
    dimension = 100

    os.makedirs("results", exist_ok=True)

    with open("results/ga_cec2017_dataset.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "FunctionIndex", "Stationary", "Selection", "Crossover", "Mutation", "Replacement",
            "BestScore", "WorstScore", "MeanScore", "StdDev"
        ])

        for function_index, function in enumerate(all_functions[:11]):
            for sel_name, sel_func in selection.items():
                for cross_name, cross_func in crossover_real.items():
                    for mut_name, mut_func in mutation.items():
                        for rep_name, rep_func in replace.items():
                            for stationary in np.arange(0, 1.01, 0.1):
                                args_list = [
                                    (function, dimension, sel_func, cross_func, mut_func, rep_func, stationary, epochs)
                                    for _ in range(iterations)
                                ]

                                with mp.Pool(mp.cpu_count()) as pool:
                                    scores = pool.map(run_cec_iteration, args_list)

                                try:
                                    if isinstance(scores, list) and len(scores) > 0:
                                        best = max(scores)
                                        worst = min(scores)
                                        mean = statistics.mean(scores)
                                        stddev = statistics.stdev(scores) if len(scores) > 1 else 0.0

                                        writer.writerow([
                                            function_index, round(stationary, 1), sel_name, cross_name, mut_name, rep_name,
                                            best, worst, mean, stddev
                                        ])
                                    else:
                                        print(f"[WARNING] Skipping stats for function {function_index} — invalid scores.")

                                except Exception as e:
                                    print(f"[ERROR] Skipping function {function_index} due to: {e}")


if __name__ == "__main__":
    mp.set_start_method("fork")
    main_cec2017()
