import random
from SimulatedAnnealing import SimulatedAnnealing

solution:list[bool]

information = {
    "items": [
        (12, 4), (2, 2), (1, 2), (1, 1), (4, 10),
        (1, 1), (2, 3), (1, 2), (3, 6), (7, 13)
    ],
    "capacity": 10
}

def energy(solution, information):
    total_weight = total_value = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            total_weight += information['items'][i][0]
            total_value += information['items'][i][1]
    
    if total_weight > information['capacity']:
        return information['capacity'] - total_weight
    return total_value
    

def generate_initial_solution():
    while True:
        solution = [random.randint(0,1) for _ in information['items']]
        if energy(solution, information) > 0:
            return solution


def generate_neighbour(solution):
    neighbour = solution[:]
    index = random.randint(0, len(solution) - 1)
    neighbour[index] = not neighbour[index]
    return neighbour


sa = SimulatedAnnealing(information, energy, generate_initial_solution, generate_neighbour)
a = sa.simulatedAnnealing(1000, 1, 0.95,100)
print(a)
