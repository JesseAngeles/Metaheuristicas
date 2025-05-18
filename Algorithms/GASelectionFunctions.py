import random

class SelectionFunctions:
    @staticmethod
    def universalRandom(population, objective):
        population_size = len(population)
        parents=[]
        objectives = [objective(individual) for individual in population]
        total = sum(objectives)
        space = total / population_size
        start = random.uniform(0, space)
        pointers = [start + i * space for i in range(population_size)]
        
        fitness_sum = 0
        i = 0
        for pointer in pointers:
            while fitness_sum < pointer:
                fitness_sum += objectives[i]
                i += 1
            parents.append(population[i - 1])
        
        print(parents)
        print("\n\n")
    
        return parents
    
    @staticmethod
    def tournament(population, objective, alpha=0.2):
        population_size = len(population)
        parents = []
        for _ in range(population_size):
            candidates = random.sample(population, int(population_size * alpha))
            scores = [objective(ind) for ind in candidates]
            best = candidates[scores.index(max(scores))]
            parents.append(best)
        return parents