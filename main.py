import copy
from Algorithms.Axolotl import Axolotl
from Algorithms.GeneticAlgorithm import GeneticAlgorithm

from Problems.KnapsackProblem import KnapsackProblem
from Problems.SumFunctionProblem import SumFunctionProblem

ksp = KnapsackProblem(20, 20)
sfp = SumFunctionProblem(100, -100, 100)

a = Axolotl(sfp, damage=0.5, regeneration=0.5)

b = -999

for _ in range(100):
    a.optimize(100)

    m = a.bestIndividual(a.males)
    f = a.bestIndividual(a.females)

    bf = a.bestIndividual(a.females)
    bm = a.bestIndividual(a.males)
    be = max({a.problem.objective(bf), a.problem.objective(bm)})
    a.printPopulation()
    
    if be > b:
        b = be
        print(b) 

print(b) 

ksp2 = copy.deepcopy(ksp)

# a = Axolotl(ksp, damage=0.8, regeneration=0.8)
# g = GeneticAlgorithm(ksp2)

# # a.optimize()
# best = -9999
# for _ in range(50):
#     a.optimize(100)    
#     g.optimize(100)

#     bf = a.bestIndividual(a.females)
#     bm = a.bestIndividual(a.males)

#     a.printPopulation()

#     print(f"f:{a.problem.objective(bf)} - m:{a.problem.objective(bm)}")

# # print(f"a: {ksp.objective(a.bestIndividual(a.females))}")
# # print(f"g:{g.bestIndividual()}")
