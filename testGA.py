import csv
import statistics
import numpy as np
import multiprocessing as mp

from Algorithms.GeneticAlgorithm import GeneticAlgorithm
from Problems.KnapsackProblem import KnapsackProblem
from Problems.TravelSalesmanProblem import TravelSalesManProblem
from Problems.SumFunctionProblem import SumFunctionProblem

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

# ======= Función paralela =======
def run_single_iteration(args):
    problem_name, problem_params, sel_func, cross_func, mut_func, rep_func, stationary, epochs = args

    if problem_name == "SumFunction":
        problem = SumFunctionProblem(*problem_params)
    elif problem_name == "Knapsack":
        problem = KnapsackProblem(*problem_params)
    elif problem_name == "TSP":
        problem = TravelSalesManProblem(*problem_params)

    g = GeneticAlgorithm(problem)
    g.setSelection(sel_func(g))
    g.setCrossover(cross_func(g))
    g.setMutation(mut_func(g))
    g.setReplace(rep_func(g))
    g.optimize(epochs, stationary)
    return g.bestIndividual()


def main():
    problems = {
        "SumFunction": (SumFunctionProblem, [50, -5, 5]),
        "Knapsack": (KnapsackProblem, [50, 50]),
        "TSP": (TravelSalesManProblem, [50])
    }

    selection = {
        "UniversalRandom": select_universal,
        "Tournament": select_tournament,
        "Proportional": select_proportional,
        "NegativeAssortative": select_negative
    }

    crossover_bin = {
        "OnePoint": cross_one_point,
        "TwoPoint": cross_two_point,
        "Uniform": cross_uniform
    }

    crossover_real = {
        "Arithmetic": cross_arithmetic,
        "Blend": cross_blend,
        "SimulatedBinary": cross_sim_binary
    }

    crossover_per = {
        "UniformOrderBased": cross_uniform_order,
        "OrderBased": cross_order_based
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

    with open("ga_dataset_parallel.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Problem", "Stationary", "Selection", "Crossover", "Mutation", "Replacement",
            "BestScore", "WorstScore", "MeanScore", "StdDev"
        ])

        for problem_name, (problem_class, problem_args) in problems.items():

            if problem_name == "Knapsack":
                crossover_set = crossover_bin
            elif problem_name == "TSP":
                crossover_set = crossover_per
            elif problem_name == "SumFunction":
                crossover_set = crossover_real

            for sel_name, sel_func in selection.items():
                for cross_name, cross_func in crossover_set.items():
                    for mut_name, mut_func in mutation.items():
                        for rep_name, rep_func in replace.items():
                            for stationary in np.arange(0, 1.01, 0.1):
                                args_list = [
                                    (problem_name, problem_args, sel_func, cross_func, mut_func, rep_func, stationary, epochs)
                                    for _ in range(iterations)
                                ]

                                with mp.Pool(mp.cpu_count()) as pool:
                                    scores = pool.map(run_single_iteration, args_list)

                                try:
                                    if isinstance(scores, list) and len(scores) > 0:
                                        best = max(scores)
                                        worst = min(scores)
                                        mean = statistics.mean(scores)
                                        stddev = statistics.stdev(scores) if len(scores) > 1 else 0.0

                                        writer.writerow([
                                            problem_name, round(stationary, 1), sel_name, cross_name, mut_name, rep_name,
                                            best, worst, mean, stddev
                                        ])
                                    else:
                                        print(f"[WARNING] Skipping stats for {problem_name} | {round(stationary,1)} — insufficient or invalid scores.")

                                except Exception as e:
                                    print(f"[ERROR] Skipping entry due to exception: {e}")


if __name__ == "__main__":
    mp.set_start_method("fork")  # Asegura compatibilidad en Linux
    main()
