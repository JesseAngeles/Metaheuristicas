import random

class MutationFunctions:
    @staticmethod
    def singlePoint(population:list, problem, alpha: float = 0.2):
        mutations: list  = []
        for individual in population:
            if random.random() <= alpha:
                mutations.append(problem.getRandomNeighbour(individual))
            else:
                mutations.append(individual)
        
        return mutations