import random
import numpy as np

from Problems.Problem import Problem

class Cec2017(Problem):
    def __init__(self, function: callable, low:int = -100 , high:int = 100 , dimention:int = 20 , alpha:int = 1):
        super().__init__()
        self.generateInformation(function, low, high, dimention, alpha)

    def generateInformation(self, function: callable, low:int, high:int, dimention:int, alpha:int):
        self.information = {
            "function": function,
            "low" : low,
            "high": high,
            "dimention": dimention,
            "alpha": alpha
        }

    def objective(self, solution):
        return - self.information["function"]([solution])[0]

    def generateInitialSolution(self):
        solution = np.random.uniform(low=self.information["low"],
                                     high=self.information["high"],
                                     size=self.information["dimention"]).tolist()

        return solution

    def getRandomNeighbour(self, solution):
        neighbour = solution[:]
        index = random.randint(0, len(solution) - 1)
        alpha = random.uniform(-self.information["alpha"], self.information["alpha"])

        neighbour[index] += alpha
        return neighbour

    def getNextNeighbour(self, solution, *args, **kwargs):
        return super().getNextNeighbour(solution, *args, **kwargs)
    
    def getNeighbours(self, solution):
        return super().getNeighbours(solution)
    
    def printInformation(self):
        print("-- INFORMATION --")
        print(f"Function: {self.information.get('function').__name__}")
        print(f"Lower bound: {self.information.get('low')}")
        print(f"Upper bound: {self.information.get('high')}")
        print(f"Dimension: {self.information.get('dimention')}")
        print(f"Alpha: {self.information.get('alpha')}")
        print("------------------")