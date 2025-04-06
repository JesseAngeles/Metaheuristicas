import random
import math

class SimulatedAnnealing:
    def __init__(self, information, energy_function ,initial_solution_function, generate_neighbour_function):
        self.information = information
        self.energy_function = energy_function
        self.initial_solution_function = initial_solution_function
        self.generate_neighbour_function = generate_neighbour_function

    def simulatedAnnealing(self, temperature, min_temperature, alpha, max_iter):
        current_solution = self.initial_solution_function()
        current_energy = self.energy_function(current_solution, self.information)
        best_solution = current_solution[:]
        best_energy = current_energy

        while temperature > min_temperature:
            for _ in range(max_iter):
                neighbour = self.generate_neighbour_function(current_solution)
                neighbour_energy = self.energy_function(neighbour, self.information)

                delta = neighbour_energy - current_energy
                if delta > 0 or random.random() < math.exp(delta / temperature):
                    current_solution = neighbour
                    current_energy = neighbour_energy

                    if current_energy > best_energy:
                        best_solution = current_solution[:]
                        best_energy = current_energy

            temperature *= alpha
        
        return best_solution, best_energy, current_solution, current_energy 