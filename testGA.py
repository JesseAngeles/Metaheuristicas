import csv
import statistics
import numpy as np

from Algorithms.GeneticAlgorithm import GeneticAlgorithm
from Problems.KnapsackProblem import KnapsackProblem
from Problems.TravelSalesmanProblem import TravelSalesManProblem
from Problems.SumFunctionProblem import SumFunctionProblem

ksp = KnapsackProblem(100, 100)
tsm = TravelSalesManProblem(100)
sfp = SumFunctionProblem(100, -5, 5)

problems = {
    "Knapsack": ksp,
    "TSP": tsm,
    "SumFunction": sfp
}

# Selección
selection = {
    "UniversalRandom": lambda g: g.selection_functions.universalRandom,
    "Tournament": lambda g: g.selection_functions.tournament,
    "Proportional": lambda g: g.selection_functions.proportional,
    "NegativeAssortative": lambda g: g.selection_functions.negativeAssortativeMating
}

# Cruzas
crossover_bin = {
    "OnePoint": lambda g: g.crossover_functions.onePoint,
    "TwoPoint": lambda g: g.crossover_functions.twoPoint,
    "Uniform": lambda g: g.crossover_functions.uniform
}

crossover_real = {
    "Arithmetic": lambda g: g.crossover_functions.arithmetic,
    "Blend": lambda g: g.crossover_functions.blend,
    "SimulatedBinary": lambda g: g.crossover_functions.simulatedBinary
}

crossover_per = {
    "UniformOrderBased": lambda g: g.crossover_functions.uniformOrderBased,
    "OrderBased": lambda g: g.crossover_functions.orderBased
}

# Mutación
mutation = {
    "SinglePoint": lambda g: g.mutation_functions.singlePoint
}

# Reemplazo
replace = {
    "Random": lambda g: g.replace_functions.random,
    "Elitism": lambda g: g.replace_functions.elitism,
    "DeterministCrowding": lambda g: g.replace_functions.deterministCrowding,
    "RestrictedTournament": lambda g: g.replace_functions.restrictedTournament
}

iterations = 100
epochs = 1000

# Archivo CSV
with open("ga_dataset.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Problem", "Stationary","Selection", "Crossover", "Mutation", "Replacement",
        "BestScore", "WorstScore", "MeanScore", "StdDev"
    ])

    for problem_name, problem in problems.items():
        g = GeneticAlgorithm(problem)

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
                        scores = []

                        for stationary in np.arange(0, 1.01, 0.1):
                            
                            for _ in range(iterations):  # puedes subir a 100 si gustas
                                g.resetProblem()
                                g.setSelection(sel_func(g))
                                g.setCrossover(cross_func(g))
                                g.setMutation(mut_func(g))
                                g.setReplace(rep_func(g))
                                g.optimize(epochs, stationary)
                                score = g.bestIndividual()
                                scores.append(score)

                            best = max(scores)
                            worst = min(scores)
                            mean = statistics.mean(scores)
                            stddev = statistics.stdev(scores) if len(scores) > 1 else 0.0

                            writer.writerow([
                                problem_name, round(stationary,1), sel_name, cross_name, mut_name, rep_name,
                                best, worst, mean, stddev
                            ])

                            print(f"{problem_name} | {stationary} | {sel_name} | {cross_name} | {mut_name} | {rep_name} => B: {best} | W: {worst} | M: {mean:.2f} | SD: {stddev:.2f}")
