import random

class ReplaceFunctions:
    @staticmethod
    def randomChange(population: list, replace:list):
        population_size = len(population)
        replace_size = len(replace)
        
        survivors = random.sample(population, population_size - replace_size)
        survivors += replace
        
        return survivors