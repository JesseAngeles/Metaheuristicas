from Algorithms.Axolotl import Axolotl

from Problems.KnapsackProblem import KnapsackProblem


ksp = KnapsackProblem(10, 100)

a = Axolotl(ksp)
a.optimize()

for _ in range(1000):
    a.optimize()
    print(a.bestIndividual(a.population), ksp.objective(a.bestIndividual(a.population)))