import random

from Problems.Problem import Problem

class KnapsackProblem(Problem):
    def __init__(self, items: int, capacity: int):
        super().__init__()
        self.generateInformation(items, capacity)

    def generateInformation(self, items: int, capacity: int):
        self.information = {
            "items": items,
            "values": [(random.randint(1, 10), random.randint(1, 10)) for _ in range(items)],
            "capacity": capacity
        }

    def objective(self, solution):
        total_weight = total_value = 0
        for i, selected in enumerate(solution):
            if selected:
                total_weight += self.information["values"][i][0]
                total_value += self.information["values"][i][1]
        if total_weight > self.information["capacity"]:
            return self.information["capacity"] - total_weight  # Penalización
        return total_value

    def generateInitialSolution(self):
        return [random.randint(0, 1) for _ in self.information['values']]
        
    def normalizeSolution(self, solution):
        return [ 0 if dimention < 0.5 else 1 for dimention in solution ]
        

    def getRandomNeighbour(self, solution):
        neighbour = solution[:]
        index = random.randint(0, len(solution) - 1)
        neighbour[index] = 1 - int(neighbour[index])
        return neighbour

    def getNextNeighbour(self, solution, index):
        sol = solution[:]
        sol[index] = 1 - sol[index]
        return sol

    def getNeighbours(self, solution):
        return super().getNeighbours(solution)

    def printInformation(self):
        print("--INFORMATION---")
        print(f"Total items: {self.information.get('items')}")
        print(f"Capacity: {self.information.get('capacity')}")
        print("W\tV")
        for _, (peso, valor) in enumerate(self.information.get("values", [])):
            print(f"{peso}\t{valor}")
        print("----------------")