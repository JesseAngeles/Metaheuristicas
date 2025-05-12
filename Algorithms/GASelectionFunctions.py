import random

class SelectionFunctions:
    @staticmethod
    def tournament(population, objective_fn, alpha=0.2):
        population_size = len(population)
        parents = []
        for _ in range(population_size):
            candidates = random.sample(population, int(population_size * alpha))
            scores = [objective_fn(ind) for ind in candidates]
            best = candidates[scores.index(max(scores))]
            parents.append(best)
        return parents