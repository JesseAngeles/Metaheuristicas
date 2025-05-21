import math
import random
from Algorithms.functions import distance, linealDisplacement

class SelectionFunctions:

    @staticmethod
    def universalRandom(population, objective):
        population_size = len(population)
        parents=[]
   
        objectives = linealDisplacement(population, objective)
        total = sum(objectives)
        space = total / population_size
        start = random.uniform(0, space)
        pointers = [start + i * space for i in range(population_size)]
        
        fitness_sum = 0
        i = 0
        for pointer in pointers:
            while i < len(objectives) and fitness_sum < pointer:
                fitness_sum += objectives[i]
                i += 1
            parents.append(population[i - 1 if i > 0 else 0])

        return parents

    @staticmethod
    def tournament(population, objective, selection_rate=0.2):
        population_size = len(population)
        parents = []

        for _ in range(population_size):
            k = max(2, math.ceil(population_size * selection_rate))
            candidates = random.sample(population, min(k, population_size))
            scores = [objective(ind) for ind in candidates]
            best = candidates[scores.index(max(scores))]
            parents.append(best)

        return parents    
    
    @staticmethod
    def proportional(population, objective):
        population_size = len(population)
        parents = []
        
        objectives = linealDisplacement(population, objective)
        
        total = sum(objectives)
        probabilities = [ objective/total for objective in objectives ]
        
        proportions = [ probabilities[0] ]
        for i in range(1, len(probabilities)):
            proportions.append(probabilities[i] + proportions[i - 1])

        for _ in range(population_size):
            pos = random.random()
            for i in range(len(proportions)):
                if (pos <= proportions[i]):
                    parents.append(population[i])
                    break

        return parents
 
    @staticmethod
    def negativeAssortativeMating(population, objective):
        population_size = len(population)
        parents = []

        for _ in range(int(population_size/2)):
            individual = random.choice(population)
            distances = [ distance(individual, test) for test in population ]

            parents.append(individual)
            parents.append(population[distances.index(max(distances))])

        return parents