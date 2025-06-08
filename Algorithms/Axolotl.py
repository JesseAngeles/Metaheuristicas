import random
import numpy as np

from Algorithms.Metaheuristic import Metaheuristic

class Axolotl(Metaheuristic):
    def __init__(self, problem, population_size = 32, damage = 0.5, regeneration = 0.1, tournament_size = 3, alpha = 0.5):
        super().__init__(problem)
        self.population_size = population_size
        self.male_size = int(self.population_size / 2)
        self.damage = damage
        self.regeneration = regeneration
        self.tournament_size = tournament_size
        self.alpha = alpha
        
        self.resetProblem()

    # Abstract methods
    def resetProblem(self):
        super().resetProblem()
        population = [self.problem.generateInitialSolution() for _ in range(self.population_size)]
        self.males = population[:self.male_size]
        self.females = population[self.male_size:]

    def optimize(self, epochs: int = 1):
        for _ in range(epochs):  
            # Transition males and females
            self.transition(self.males)
            self.transition(self.females)
            
            # Injury and restorations
            self.injuryAndRestoration(self.males)
            self.injuryAndRestoration(self.females)
            
            # Reproduction
            self.reproduction()

            
    def transition(self, population):
        best = self.bestIndividual(population)
        values = [ self.problem.objective(individual) for individual in population ]
        total = sum(values)

        for i, individual in enumerate(population):
            objective = values[i]
            probability = objective / total if total else 0
            r = random.random() / len(population)
            
            if probability < r:
                for j in range(len(individual)):
                    individual[j] = individual[j] + (best[j] - individual[j]) * self.alpha
            else:
                population[i] = self.problem.getRandomNeighbour(individual)
            
            population[i] = self.problem.normalizeSolution(individual)
 
    def injuryAndRestoration(self, population):
        for i, individual in enumerate(population):
            if random.random() < self.damage:
                for j in range(len(individual)):
                    if random.random() < self.regeneration:
                        individual = self.problem.getNextNeighbour(individual, j)
                population[i] = individual 

    def reproduction(self):
        new_males = []
        new_females = []
        for female in self.females:
            males = random.sample(self.males, self.tournament_size)
            best_male = self.bestIndividual(males)
            [ new_female, new_male ] = self.uniform(best_male, female)
            new_males.append(new_male)
            new_females.append(new_female)
        
        self.males = new_males
        self.females = new_females
    
    def uniform(self, male, female):
        child1 = []
        child2 = []
        
        for i in range(len(male)):
            if random.random() < 0.5:
                child1.append(male[i])
                child2.append(female[i])
            else:
                child1.append(female[i])
                child2.append(male[i])
        
        population = [ male, female, child1, child2 ]
        population.sort(key=self.problem.objective, reverse= True)         
        return population[0:2]
    
    def bestIndividual(self, population):
        return max(population, key=lambda ind: self.problem.objective(ind))

    def best(self):
        population = self.males + self.females
        values = [self.problem.objective(ind) for ind in population]
        best_idx = np.argmax(values)  # o np.argmax si es un problema de maximización
        return values[best_idx]

    def compare(self, sol1, sol2):
        for i in range(len(sol1)):
            if sol1[i] != sol2[i]:
                return False
        return True
    
    def printPopulation(self):
        for i in self.males:
            print(i, round(self.problem.objective(i),2))
        print(" ")
        for i in self.females:
            print(i, round(self.problem.objective(i),2))
        print(" ")