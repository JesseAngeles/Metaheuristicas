import random 
import math

from Algorithms.Metaheuristic import Metaheuristic 

class SimulatedAnnealing(Metaheuristic):
    def __init__(self, problem, max_temperature:float = 100, min_temperature:float = 1, alpha:float = 0.95, max_iter:int = 100):
        super().__init__(problem)
        self.max_temperature = max_temperature
        self.min_temperature = min_temperature
        self.alpha = alpha
        self.max_iter= max_iter
        self.resetProblem()

    # Abstract methods
    def resetProblem(self):
        super().resetProblem()
        self.iter = 0
        self.energy = self.problem.objective(self.solution)
        self.temperature = self.max_temperature

    def optimize(self, epochs: int = 1):
        if not self.is_best:
            for _ in range(epochs):
                if self.temperature > self.min_temperature:
                    if self.iter < self.max_iter:
                        neighbour = self.problem.getRandomNeighbour(self.solution)
                        neighbour_energy = self.problem.objective(neighbour)

                        delta = neighbour_energy - self.energy
                        if delta > 0 or random.random() < math.exp(delta / self.temperature):
                            self.solution = neighbour
                            self.energy = neighbour_energy

                        self.iter += 1
                    else:
                        self.iter = 0
                        self.temperature *= self.alpha

    def printSolution(self):
        print(f'Solution: {self.solution}: {self.evaluate(self.solution)}|{self.temperature}')