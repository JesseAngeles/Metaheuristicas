import random

class TravelSalesmanProblem:
    def __init__(self):
        self.information = {}

    def generate_information(self, cities):
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
 
    def energy(self, solution, information):
        distance = 0
        num_cities:int = len(solution)
        
        for i in range(num_cities):
            current_city = solution[i]
            next_city = solution[(i + 1) % num_cities]  
            distance += information['distances'][current_city][next_city]
            
        return -distance

    def generate_initial_solution(self, information):
        solution =  list(range(information['cities']))
        random.shuffle(solution)
        return solution        

    def random_neighbour(self, solution):
        neighbour = solution[:]
        i = j = random.randint(0, len(solution) - 1)
        while j == i:
            j = random.randint(0, len(solution) - 1)
        neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
        
        return neighbour
