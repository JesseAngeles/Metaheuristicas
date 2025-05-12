import random

from Algorithms.Metaheuristic import Metaheuristic
from Algorithms.GASelectionFunctions import SelectionFunctions as Selection
from Algorithms.GACrossoverFunctions import CrossoverFunctions as Crossover
from Algorithms.GAMutationFunctions import MutationFunctions as Mutation
from Algorithms.GAReplaceFunctions import ReplaceFunctions as Replace

class GeneticAlgorithm(Metaheuristic):
    def __init__(self, problem, population_size: int = 16):
        super().__init__(problem)
        self.population_size = population_size
        self.selection_functions = Selection
        self.crossover_functions = Crossover
        self.mutation_functions = Mutation
        self.replace_functions = Replace
        
        self.resetProblem()
    
    # Abstract methods 
    def resetProblem(self):
        super().resetProblem()
        self.population = [self.problem.generateInitialSolution() for _ in range(self.population_size)]

    def optimize(self, epochs: int = 1, stationary: float = 0,
                 selection:callable = Selection.tournament,
                 crossover:callable = Crossover.singlePoint,
                 mutation:callable = Mutation.singlePoint,
                 replace:callable = Replace.randomChange):
        for _ in range(epochs):
            population_sample = random.sample(self.population,self.population_size - int(self.population_size * stationary))
            
            population_sample = selection(population_sample, self.problem.objective)
            population_sample = crossover(population_sample)
            population_sample = mutation(population_sample, self.problem)
            self.population = replace(self.population, population_sample) 
        
    def bestIndividual(self):
        objectives = [self.problem.objective(individual) for individual in self.population]
        return max(objectives)