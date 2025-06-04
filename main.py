from Algorithms.Axolotl import Axolotl

from Problems.KnapsackProblem import KnapsackProblem


ksp = KnapsackProblem(20, 10)

a = Axolotl(ksp)
# a.optimize()
best = -9999
for _ in range(50):
    a.optimize()
    a.printPopulation()    
    print(a.bestIndividual(a.population), ksp.objective(a.bestIndividual(a.population)), "\n")
    