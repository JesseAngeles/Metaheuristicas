import random

class CrossoverFunctions:
    @staticmethod
    def onePoint(population:list):
        generation:list = []    
        population_size = len(population)
        for i in range(0, population_size, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            
            point:int = random.randint(1, population_size - 1)

            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]
            generation.extend([child1, child2])

        return generation
    
    @staticmethod
    def twoPoint(population:list):
        population_size = len(population)
        generation:list = []

        for i in range(0, population_size - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            length = len(parent1)

            point1 = random.randint(1, length - 2)
            point2 = random.randint(point1 + 1, length - 1)

            child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
            child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
            generation.extend([child1, child2])

        return generation

    @staticmethod
    def uniform(population: list, crossover_rate: float = 0.5):
        generation = []
        population_size = len(population)

        for i in range(0, population_size - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            length = len(parent1)

            child1 = []
            child2 = []

            for j in range(length):
                if random.random() < crossover_rate:
                    child1.append(parent1[j])
                    child2.append(parent2[j])
                else:
                    child1.append(parent2[j])
                    child2.append(parent1[j])

            generation.extend([child1, child2])

        return generation

    @staticmethod
    def arithmetic(population: list, crossover_rate: float = None):
        generation = []
        population_size = len(population)

        for i in range(0, population_size - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]

            a = crossover_rate if crossover_rate is not None else random.random()

            child1 = [a * x + (1 - a) * y for x, y in zip(parent1, parent2)]
            child2 = [(1 - a) * x + a * y for x, y in zip(parent1, parent2)]

            generation.extend([child1, child2])

        return generation


    @staticmethod
    def blend(population: list, crossover_rate: float = 0.5):
        generation = []
        population_size = len(population)

        for i in range(0, population_size - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]

            child1 = []
            child2 = []

            for x, y in zip(parent1, parent2):
                d = abs(x - y)
                low = min(x, y) - crossover_rate * d
                high = max(x, y) + crossover_rate * d

                gene1 = random.uniform(low, high)
                gene2 = random.uniform(low, high)

                child1.append(gene1)
                child2.append(gene2)

            generation.extend([child1, child2])

        return generation

    @staticmethod
    def simulatedBinary(population: list, crossover_rate: float = 2):
        generation = []
        population_size = len(population)

        for i in range(0, population_size - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]

            child1 = []
            child2 = []

            for x1, x2 in zip(parent1, parent2):
                if random.random() < 0.5:
                    if abs(x1 - x2) > 1e-14:
                        x_min = min(x1, x2)
                        x_max = max(x1, x2)

                        u = random.random()
                        if u <= 0.5:
                            beta = (2 * u) ** (1 / (crossover_rate + 1))
                        else:
                            beta = (1 / (2 * (1 - u))) ** (1 / (crossover_rate + 1))

                        c1 = 0.5 * ((1 + beta) * x1 + (1 - beta) * x2)
                        c2 = 0.5 * ((1 - beta) * x1 + (1 + beta) * x2)
                    else:
                        c1, c2 = x1, x2
                else:
                    c1, c2 = x1, x2

                child1.append(c1)
                child2.append(c2)

            generation.extend([child1, child2])

        return generation

    @staticmethod
    def uniformOrderBased(population: list):
        generation = []
        population_size = len(population)

        for i in range(0, population_size - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            size = len(parent1)

            mask = [random.randint(0, 1) for _ in range(size)]

            def create_child(p1, p2):
                child = [None] * size
                for j in range(size):
                    if mask[j] == 1:
                        child[j] = p1[j]
                fill = [gene for gene in p2 if gene not in child]
                k = 0
                for j in range(size):
                    if child[j] is None:
                        child[j] = fill[k]
                        k += 1
                return child

            child1 = create_child(parent1, parent2)
            child2 = create_child(parent2, parent1)
            generation.extend([child1, child2])

        return generation

    @staticmethod
    def orderBased(population: list):
        generation = []
        population_size = len(population)

        for i in range(0, population_size - 1, 2):
            parent1 = population[i]
            parent2 = population[i + 1]
            size = len(parent1)

            positions = random.sample(range(size), random.randint(1, size - 1))

            def create_child(p1, p2):
                child = [None] * size
                
                for idx in positions:
                    child[idx] = p1[idx]
                    
                fill = [gene for gene in p2 if gene not in child]
                k = 0
                for j in range(size):
                    if child[j] is None:
                        child[j] = fill[k]
                        k += 1
                return child

            child1 = create_child(parent1, parent2)
            child2 = create_child(parent2, parent1)
            generation.extend([child1, child2])

        return generation
