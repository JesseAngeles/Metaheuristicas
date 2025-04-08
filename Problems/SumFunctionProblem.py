import random

class SumFunctionProblem:
    def __init__(self):
        self.information = {}

    def generate_information(self, size, min, max):
        self.information = {
            "size": size,
            "min": min,
            "max": max
        }
        
    def energy(self, solution, _):
        total_sum:float = 0
        
        for val in solution:
            total_sum += val**2
    
        return -total_sum

    def generate_initial_solution(self, information):
        solution = [random.randint(information['min'], information['max']) for _ in range(information['size'])]
        return solution

    def random_neighbour(self, solution):
        neighbour = solution[:]
        index = random.randint(0, len(solution) - 1)
        sign = random.choice([-1 , 1])
        neighbour[index] += sign

        if neighbour[index] > self.information['max']:
            neighbour[index] = self.information['min']

        if neighbour[index] < self.information['min']:
            neighbour[index] = self.information['max']

        return neighbour