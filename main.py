import copy
from Algorithms.Axolotl import Axolotl
from Algorithms.GeneticAlgorithm import GeneticAlgorithm

from Problems.KnapsackProblem import KnapsackProblem

ksp = KnapsackProblem(20, 10)

ksp2 = copy.deepcopy(ksp)

a = Axolotl(ksp)
g = GeneticAlgorithm(ksp2)

# a.optimize()
best = -9999
for _ in range(50):
    a.optimize()    
    g.optimize(100)

print(f"a: {ksp.objective(a.bestIndividual(a.population))}")
print(f"g: {g.bestIndividual()}")
