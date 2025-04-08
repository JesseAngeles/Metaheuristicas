import random
import math

class SimulatedAnnealing:
    def __init__(self, information, energy_function ,initial_solution_function, generate_neighbour_function):
        self.information = information
        self.energy_function = energy_function
        self.initial_solution_function = initial_solution_function
        self.generate_neighbour_function = generate_neighbour_function
        self.solution = self.initial_solution_function(self.information)
        self.energy = self.energy_function(self.solution, self.information)
        self.max_temperature = 1000
        self.min_temperature = 1
        self.alpha = 0.95
        self.max_iter = 100
        self.reset()

    def reset(self):
        self.iter = 0
        self.energy = self.energy_function(self.solution, self.information)
        self.temperature = self.max_temperature
        self.best_solution = self.solution[:]
        self.best_energy = self.energy_function(self.best_solution, self.information)

    def stepSimpleSimulatedAnnealing(self):
        if self.temperature > self.min_temperature:
            if self.iter < self.max_iter:
                neighbour = self.generate_neighbour_function(self.solution)
                neighbour_energy = self.energy_function(neighbour, self.information)

                delta = neighbour_energy - self.energy
                if delta > 0 or random.random() < math.exp(delta / self.temperature):
                    self.solution = neighbour
                    self.energy = neighbour_energy

                    if self.energy > self.best_energy:
                        self.best_solution = self.solution[:]
                        self.best_energy = self.energy

                self.iter += 1
            else:
                self.iter = 0
                self.temperature *= self.alpha
        else:
            return False
        
        return True

    def simpleSimulatedAnnealing(self):
        current_solution = self.solution
        current_energy = self.energy_function(current_solution, self.information)
        best_solution = current_solution[:]
        best_energy = current_energy
        temperature = self.max_temperature

        while temperature > self.min_temperature:
            for _ in range(self.max_iter):
                neighbour = self.generate_neighbour_function(current_solution)
                neighbour_energy = self.energy_function(neighbour, self.information)

                delta = neighbour_energy - current_energy
                if delta > 0 or random.random() < math.exp(delta / temperature):
                    current_solution = neighbour
                    current_energy = neighbour_energy

                    if current_energy > best_energy:
                        best_solution = current_solution[:]
                        best_energy = current_energy
                        
            temperature *= self.alpha

        self.solution = best_solution

    def print(self):
        print(self.solution, self.energy_function(self.solution, self.information))