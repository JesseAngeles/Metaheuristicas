import random
from functools import partial

from Algorithms.Metaheuristic import Metaheuristic
from Algorithms.GeneticFunctions.GASelectionFunctions import SelectionFunctions as Selection
from Algorithms.GeneticFunctions.GACrossoverFunctions import CrossoverFunctions as Crossover
from Algorithms.GeneticFunctions.GAMutationFunctions import MutationFunctions as Mutation
from Algorithms.GeneticFunctions.GAReplaceFunctions import ReplaceFunctions as Replace

class GeneticAlgorithm(Metaheuristic):
    def __init__(self, problem, population_size: int = 32):
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

    def optimize(self, epochs: int = 1, stationary: float = 0, alpha: float = 0.0):
        if stationary == 1:
            return
    
        i = 0
        while i < epochs:
            i += 1

            best = self.bestObjective() * (1 + alpha)

            population_sample_size = self.population_size - int(self.population_size * stationary)
            population_sample_size -= population_sample_size % 2  # Asegurar que sea múltiplo de 2
            population_sample = random.sample(self.population, population_sample_size)
            
            population_sample = self.selection(population_sample, self.problem.objective)
            population_sample = self.crossover(population_sample)
            population_sample = self.mutation(population_sample, self.problem)
            self.population = self.replace(self.population, population_sample, self.problem.objective) 

            if(best > self.bestObjective() and i == epochs):
                i -= 1

    def bestIndividual(self, population):
        return max(population, key=lambda ind: self.problem.objective(ind))

    def bestObjective(self):
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

    def setReplace(self, replace, replace_rate = None):
        if replace_rate:
            self.replace = partial(replace,replace_rate =replace_rate)
        else:
            self.replace = replace

    # Display
    def printConfiguration(self):
        selection_name = self.selection.func.__name__ if hasattr(self.selection, 'func') else self.selection.__name__
        crossover_name = self.crossover.func.__name__ if hasattr(self.crossover, 'func') else self.crossover.__name__
        mutation_name = self.mutation.func.__name__ if hasattr(self.mutation, 'func') else self.mutation.__name__
        replace_name = self.replace.func.__name__ if hasattr(self.replace, 'func') else self.replace.__name__

        print("=== Configuration ===")
        print(f"Selection: {selection_name}")
        print(f"Crossover: {crossover_name}")
        print(f"Mutatation: {mutation_name}")
        print(f"Replace: {replace_name}")
        print(f"Population size: {self.population_size}\n")
