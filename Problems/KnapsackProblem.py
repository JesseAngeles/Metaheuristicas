import random

class KnapsackProblem:
    def __init__(self):
        self.information = {}

    def generate_information(self, items, capacity):
        self.information = {
            "items": items,
            "values": [(random.randint(1,10), random.randint(1, 10)) for _ in range(items)],
            "capacity": capacity
        }

    def energy(self, solution, information):
        total_weight = total_value = 0
        for i in range(len(solution)):
            if solution[i] == 1:
                total_weight += information['values'][i][0]
                total_value += information['values'][i][1]
        
        if total_weight > information['capacity']:
            return information['capacity'] - total_weight
        return total_value
        
    def generate_initial_solution(self, information):
        while True:
            solution = [random.randint(0,1) for _ in information['values']]
            if self.energy(solution, information) > 0:
                return solution

    def random_neighbour(self, solution):
        neighbour = solution[:]
        index = random.randint(0, len(solution) - 1)
        neighbour[index] = 1 - neighbour[index]
        return neighbour        