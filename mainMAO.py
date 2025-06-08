import statistics
from Algorithms.Axolotl import Axolotl
from Algorithms.GeneticAlgorithm import GeneticAlgorithm

from Problems.KnapsackProblem import KnapsackProblem
from Problems.SumFunctionProblem import SumFunctionProblem

mao_scores = []
ga_scores = []

NUM_RUNS = 250

for _ in range(NUM_RUNS):
    sfp = SumFunctionProblem(50, -50, 50)

    # Configuración de MAO
    axolotl = Axolotl(sfp, 32, 0.9, 1.0, 2, 0.5)
    axolotl.optimize(250)

    # Configuración de GA
    ga = GeneticAlgorithm(sfp)
    ga.setSelection(ga.selection_functions.negativeAssortativeMating)
    ga.setCrossover(ga.crossover_functions.blend)
    ga.setReplace(ga.replace_functions.restrictedTournament)
    ga.optimize(250, 0.3)

    # Obtener mejor individuo para MAO (entre machos y hembras)
    best_m = sfp.objective(axolotl.bestIndividual(axolotl.males))
    best_f = sfp.objective(axolotl.bestIndividual(axolotl.females))
    best_a = max(best_m, best_f)

    # Obtener mejor individuo para GA
    best_ga = ga.bestObjective()

    # Guardar resultados
    mao_scores.append(best_a)
    ga_scores.append(best_ga)

    # print(f"Run {_+1}: MAO = {best_a}, GA = {best_ga}")

# Calcular estadísticas
def summary_stats(scores):
    return {
        "Best": max(scores),
        "Worst": min(scores),
        "Mean": round(statistics.mean(scores), 4),
        "StdDev": round(statistics.stdev(scores), 4)
    }

mao_stats = summary_stats(mao_scores)
ga_stats = summary_stats(ga_scores)

# Mostrar resumen
print("\n=== Estadísticas comparativas (sfp) ===")
print("Algoritmo\tBest\tWorst\tMean\tStdDev")
print(f"MAO\t\t{mao_stats['Best']}\t{mao_stats['Worst']}\t{mao_stats['Mean']}\t{mao_stats['StdDev']}")
print(f"GA\t\t{ga_stats['Best']}\t{ga_stats['Worst']}\t{ga_stats['Mean']}\t{ga_stats['StdDev']}")
