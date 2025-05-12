import random

from Problems.Problem import Problem

class TravelSalesManProblem(Problem):
    def __init__(self, cities: int):
        super().__init__()
        self.generateInformation(cities)

    def generateInformation(self, cities: int):
        distances = [[0]*cities for _ in range(cities)]

        for i in range(cities):
            for j in range(i, cities):  
                if i == j:
                    valor = 0  
                else:
                    valor = random.randint(1, 100)
                distances[i][j] = valor
                distances[j][i] = valor 

        self.information = {
            "cities" : cities,
            "distances" : distances
        }

    def objective(self, solution):
        distance = 0
        num_cities:int = len(solution)
        
        for i in range(num_cities):
            current_city = solution[i]
            next_city = solution[(i + 1) % num_cities]  
            distance += self.information['distances'][current_city][next_city]
            
        return -distance

    def generateInitialSolution(self):
        solution =  list(range(self.information['cities']))
        random.shuffle(solution)
        return solution   
        
    def getRandomNeighbour(self, solution):
        neighbour = solution[:]
        i = j = random.randint(0, len(solution) - 1)
        while j == i:
            j = random.randint(0, len(solution) - 1)
        neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
        
        return neighbour

    def getNextNeighbour(self, solution, *args, **kwargs):
        return super().getNextNeighbour(solution, *args, **kwargs)
    
    def getNeighbours(self, solution):
        return super().getNeighbours(solution)
    
    def printInformation(self):
        print("-- INFORMATION --")
        print(f"Total cities: {self.information.get('cities')}")
        print("Distance matrix:")
        distances = self.information.get("distances", [])
        
        # Header
        print("    ", end="")
        for i in range(len(distances)):
            print(f"{i:>4}", end="")
        print()
        
        # Rows
        for i, row in enumerate(distances):
            print(f"{i:>3}:", end="")
            for dist in row:
                print(f"{dist:>4}", end="")
            print()
        print("------------------")