import random
from functools import partial

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
        self.selection = Selection.tournament
        self.crossover = Crossover.onePoint
        self.mutation = Mutation.singlePoint
        self.replace = Replace.random

    def optimize(self, epochs: int = 1, stationary: float = 0):
        for _ in range(epochs):
            population_sample = random.sample(self.population,self.population_size - int(self.population_size * stationary))
            
            population_sample = self.selection(population_sample, self.problem.objective)
            population_sample = self.crossover(population_sample)
            population_sample = self.mutation(population_sample, self.problem)
            self.population = self.replace(self.population, population_sample, self.problem.objective) 
        
    def bestIndividual(self):
        objectives = [self.problem.objective(individual) for individual in self.population]
        return max(objectives)

    # SET functions
    def setSelection(self, selection, selection_rate = None):
        if selection_rate:
            self.selection = partial(selection, selection_rate = selection_rate)
        else:
            self.selection = selection

    def setCrossover(self, crossover, crossover_rate = None):
        if crossover_rate:
            self.crossover = partial(crossover, crossover_rate = crossover_rate)
        else:
            self.crossover = crossover

    def setMutation(self, mutation, mutation_rate = None):
        if mutation_rate:
            self.mutation = partial(mutation, mutation_rate = mutation_rate)
        else:
            self.mutation = mutation

    def setReplace(self, replace):
        self.replace = replace

    # Display
    def printConfiguration(self):
        selection_name = self.selection.func.__name__ if hasattr(self.selection, 'func') else self.selection.__name__
        crossover_name = self.crossover.func.__name__ if hasattr(self.crossover, 'func') else self.crossover.__name__
        mutation_name = self.mutation.func.__name__ if hasattr(self.mutation, 'func') else self.mutation.__name__

        print("=== Configuration ===")
        print(f"Selection: {selection_name}")
        print(f"Crossover: {crossover_name}")
        print(f"Mutatation: {mutation_name}")
        print(f"Replace: {self.replace.__name__}")
        print(f"Population size: {self.population_size}\n")