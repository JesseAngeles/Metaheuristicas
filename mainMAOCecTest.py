import csv
import statistics
import numpy as np
import multiprocessing as mp
import os

from Algorithms.Axolotl import Axolotl
from Problems.Cec2017 import Cec2017
from Problems.cec2017.cec2017.functions import all_functions  # Asegúrate que esté bien importado

# ======= FUNCIONES =======
def run_mao_cec_iteration(args):
    function, dimension, damage, regeneration, tournament, alpha = args

    problem = Cec2017(function=function, dimention=dimension)
    mao = Axolotl(problem, 32, damage, regeneration, tournament, alpha)
    mao.optimize(50)

    best_m = problem.objective(mao.bestIndividual(mao.males))
    best_f = problem.objective(mao.bestIndividual(mao.females))
    return max(best_m, best_f)

def main_mao_cec():
    iterations = 50
    dimension = 100

    os.makedirs("results", exist_ok=True)

    with open("results/mao_cec2017_dataset.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "FunctionIndex", "Damage", "Regeneration", "Tournament", "Alpha",
            "BestScore", "WorstScore", "MeanScore", "StdDev"
        ])

        total_combinations = 0
        for function_index, function in enumerate(all_functions[:11]):
            for damage in np.arange(0, 1.01, 0.2):
                for regeneration in np.arange(0, 1.01, 0.2):
                    for tournament in range(2, 16, 2):  # puedes extender a 2–16 si deseas
                        for alpha in np.arange(0, 1.01, 0.2):
                            total_combinations += 1
                            print(f"Func {function_index} — D:{damage} R:{regeneration} T:{tournament} A:{alpha}")

                            arg_list = [
                                (function, dimension, damage, regeneration, tournament, alpha)
                                for _ in range(iterations)
                            ]

                            with mp.Pool(processes=20) as pool:
                                scores = pool.map(run_mao_cec_iteration, arg_list)

                            try:
                                if isinstance(scores, list) and len(scores) > 0:
                                    best = max(scores)
                                    worst = min(scores)
                                    mean = statistics.mean(scores)
                                    stddev = statistics.stdev(scores) if len(scores) > 1 else 0.0

                                    writer.writerow([
                                        function_index, round(damage, 1), round(regeneration, 1),
                                        tournament, round(alpha, 1),
                                        best, worst, mean, stddev
                                    ])
                                else:
                                    print(f"[WARNING] Skipping stats for function {function_index} — invalid scores.")
                            except Exception as e:
                                print(f"[ERROR] Skipping function {function_index} due to: {e}")

    print(f"Total configuraciones probadas: {total_combinations}")


if __name__ == "__main__":
    mp.set_start_method("fork")  # Compatibilidad con sistemas UNIX
    main_mao_cec()
