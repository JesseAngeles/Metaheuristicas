import random

from Problems.Problem import Problem

class SumFunctionProblem(Problem):
    def __init__(self, size: int, min: int, max:int):
        super().__init__()
        self.generateInformation(size, min, max)

    def generateInformation(self, size: int, min: int, max: int):
        self.information = {
            "size": size,
            "min": min,
            "max": max
        }

    def objective(self, solution):
        total_sum:float = 0
        
        for val in solution:
            total_sum += val**2
    
        return -total_sum

    def generateInitialSolution(self):
        solution = [random.randint(self.information['min'], self.information['max']) for _ in range(self.information['size'])]
        return solution
        
    def getRandomNeighbour(self, solution):
        neighbour = solution[:]
        index = random.randint(0, len(solution) - 1)
        sign = random.choice([-1 , 1])
        neighbour[index] += sign

        if neighbour[index] > self.information['max']:
            neighbour[index] = self.information['min']

        if neighbour[index] < self.information['min']:
            neighbour[index] = self.information['max']

        return neighbour

    def getNextNeighbour(self, solution, *args, **kwargs):
        return super().getNextNeighbour(solution, *args, **kwargs)
    
    def getNeighbours(self, solution):
        return super().getNeighbours(solution)
    
    def printInformation(self):
        print("-- INFORMATION --")
        print(f"Size: {self.information.get('size')}")
        print(f"Min: {self.information.get('min')}")
        print(f"Max: {self.information.get('max')}")
        print("------------------")