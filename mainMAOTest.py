import csv
import statistics
import numpy as np
import multiprocessing as mp
from Algorithms.Axolotl import Axolotl
from Problems.KnapsackProblem import KnapsackProblem
from Problems.SumFunctionProblem import SumFunctionProblem

# sfp = KnapsackProblem(50, 50)
sfp = SumFunctionProblem(50, -50, 50)
iterations = 50

with open("results/mao_dataset_sfp.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Problem", "Damage", "Regeneration", "Tournament_size", "alpha",
        "BestScore", "WortsScore", "MeanScore","StdDev"
    ])

def run_single_iteration(args):
    problem, damage, regeneration, tournament, alpha = args

    mao = Axolotl(problem, 32, damage, regeneration, tournament, alpha)
    mao.optimize(50)
    return max({problem.objective(mao.bestIndividual(mao.males)), problem.objective(mao.bestIndividual(mao.females))})

def main():
    with open("results/mao_dataset_sfp.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Problem", "Damage", "Regeneration", "Tournament_size", "alpha",
            "BestScore", "WortsScore", "MeanScore","StdDev"
        ])
   
        for damage in np.arange(0, 1.01, 0.1):
            print(damage)
            for regeneration in np.arange(0, 1.01, 0.1):
                for tournament in range(2, 17):
                    for alpha in np.arange(0, 1.01, 0.1):
                        arg_list = [ (sfp, damage, regeneration, tournament, alpha) for _ in range(iterations) ]

                        with mp.Pool(mp.cpu_count()) as pool:
                            scores = pool.map(run_single_iteration, arg_list)

                        try:
                            if isinstance(scores, list) and len(scores) > 0:
                                best = max(scores)
                                worst = min(scores)
                                mean = statistics.mean(scores)
                                stddev = statistics.stdev(scores) if len(scores) > 1 else 0.0

                                writer.writerow([
                                    "sfp", round(damage, 1), round(regeneration, 1),
                                    tournament, round(alpha, 1),
                                    best, worst, mean, stddev
                                ])
                            else:
                                print(f"[WARNING] Empty score list.")

                        except Exception as e:
                            print(f"[ERROR] Skipping entry due to exception: {e}")


if __name__ == "__main__":
    mp.set_start_method("fork")  # Asegura compatibilidad en Linux
    main()

                
