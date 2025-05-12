import random

class CrossoverFunctions:
    @staticmethod
    def singlePoint(population:list):
        generation:list = []    
        population_size = len(population)
        for i in range(0, population_size, 2):
            point:int = random.randint(0, population_size - 1)
            generation.append(population[i][:point] + population[i][point:])
            generation.append(population[i][point:] + population[i][:point])

        return generation