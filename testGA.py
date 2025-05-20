from functools import partial

from Algorithms.GeneticAlgorithm import GeneticAlgorithm

from Problems.KnapsackProblem import KnapsackProblem
from Problems.TravelSalesmanProblem import TravelSalesManProblem
from Problems.SumFunctionProblem import SumFunctionProblem

ksp = KnapsackProblem(100, 100)
tsm = TravelSalesManProblem(7)
sfp = SumFunctionProblem(10, -5, 5)

g = GeneticAlgorithm(ksp)

g.setSelection(g.selection_functions.proportional)
g.setCrossover(g.crossover_functions.onePoint)
g.setMutation(g.mutation_functions.singlePoint, mutation_rate = 0.1)
g.setReplace(g.replace_functions.elitism)

g.printConfiguration()

max = -1000
for _ in range(1000):
    g.optimize(1, 0)
    if max < g.bestIndividual():
        max = g.bestIndividual()
        print(max)
        
