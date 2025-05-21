import random
from Algorithms.functions import distance

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

        # Truncar al tamaño mínimo par común
        pair_count = min(len(population), len(replace))
        pair_count -= pair_count % 2  # asegurar número par

        for i in range(0, pair_count, 2):
            # Obtener pares de padres e hijos
            p1, p2 = population[i], population[i + 1]
            o1, o2 = replace[i], replace[i + 1]

            # Determinar emparejamiento por similitud
            if distance(p1, o1) + distance(p2, o2) <= distance(p1, o2) + distance(p2, o1):
                winner1 = o1 if objective(o1) > objective(p1) else p1
                winner2 = o2 if objective(o2) > objective(p2) else p2
            else:
                winner1 = o2 if objective(o2) > objective(p1) else p1
                winner2 = o1 if objective(o1) > objective(p2) else p2

            new_population.extend([winner1, winner2])

        return new_population
    
    @staticmethod
    def restrictedTournament(population: list, replace: list, objective, replace_rate: int = 5):
        survivors = population.copy()

        for child in replace:
            # Seleccionar una ventana aleatoria de la población actual
            window = random.sample(survivors, min(replace_rate, len(survivors)))

            # Buscar el individuo más cercano en la ventana
            closest = min(window, key=lambda p: distance(p, child))

            # Reemplazar si el hijo tiene mejor aptitud
            if objective(child) > objective(closest):
                survivors[survivors.index(closest)] = child

        return survivors
