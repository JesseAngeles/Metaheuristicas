import random

class MutationFunctions:

    @staticmethod
    def singlePoint(population:list, problem, mutation_rate: float = 0.2):
        mutations: list  = []
        for individual in population:
            if random.random() <= mutation_rate:
                mutations.append(problem.getRandomNeighbour(individual))
            else:
                mutations.append(individual)
        
        return mutations