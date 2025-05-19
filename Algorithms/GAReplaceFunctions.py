import random

class ReplaceFunctions:
    @staticmethod
    def random(population: list, replace:list, objective):
        population_size = len(population)
        replace_size = len(replace)
        
        survivors = random.sample(population, population_size - replace_size)
        survivors += replace
        
        return survivors
        
    @staticmethod
    def elitism(population: list, replace: list, objective):
        population_size = len(population)
        replace_size = len(replace)

        # Ordenar población por fitness
        sorted_population = sorted(population, key=objective, reverse=True)

        # Conservar los mejores
        survivors = sorted_population[:population_size - replace_size]
        survivors += replace

        return survivors

    @staticmethod
    def deterministCrowding(population: list, replace: list, objective):
        new_population = []

        for i in range(0, len(replace), 2):
            # Emparejar hijos con sus padres más cercanos
            parent1 = population[i]
            parent2 = population[i+1]
            child1 = replace[i]
            child2 = replace[i+1]

            # # Comparar distancias
            # if distance(child1, parent1) + distance(child2, parent2) < distance(child1, parent2) + distance(child2, parent1):
            #     pairings = [(parent1, child1), (parent2, child2)]
            # else:
            #     pairings = [(parent1, child2), (parent2, child1)]

            # for parent, child in pairings:
            #     if objective(child) >= objective(parent):
            #         new_population.append(child)
            #     else:
            #         new_population.append(parent)

        return population

    @staticmethod
    def restrictedTournament(population: list, replace: list, objective):
        survivors = population.copy()

        # for child in replace:
        #     # Buscar el más cercano
        #     closest = min(survivors, key=lambda p: distance(p, child))
        #     if objective(child) > objective(closest):
        #         survivors.remove(closest)
        #         survivors.append(child)

        return population
