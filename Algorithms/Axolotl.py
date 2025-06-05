import random
import copy

from Algorithms.Metaheuristic import Metaheuristic

class Axolotl(Metaheuristic):
    def __init__(self, problem, population_size = 32, male_size = 0.5, damage = 0.5, regeneration = 0.1, tournament_size = 3, alpha = 0.5):
        super().__init__(problem)
        self.population_size = population_size
        self.male_size = int(self.population_size * male_size)
        self.damage = damage
        self.regeneration = regeneration
        self.torunament_size = tournament_size
        self.alpha = alpha
        self.k = 3
        
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
            new_population = self.reproduction()
            
            # Assortment
            self.assortment(new_population)
            
    def transition(self, population):
        best = self.bestIndividual(population)
        values = [ self.problem.objective(individual) for individual in population ]
        total = sum(values)

        for i, individual in enumerate(population):
            objective = values[i]
            probability = objective / total if total else 0
            r = random.random() / len(population)
            
            for j in range(len(individual)):
                if probability < r and not self.compare(best, individual):
                    individual[j] = individual[j] + (best[j] - individual[j]) * self.alpha
                else:
                    population[i] = self.problem.getRandomNeighbour(individual)
                           
            population[i] = self.problem.normalizeSolution(individual)
 
    def injuryAndRestoration(self, population):
        for i, individual in enumerate(population):
            if random.random() < self.damage:
                for dimention in individual:
                    if random.random() < self.regeneration:
                        population[i] = self.problem.getNextNeighbour(individual, i)
    
    def reproduction(self):
        new_males = []
        new_females = []
        for female in self.females:
            males = random.sample(self.males, self.k)
            best_male = self.bestIndividual(males)
            [ new_f, new_m ] = self.uniform(best_male, female)
            new_males.append(new_m)
            new_females.append(new_f)
        
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
        population.sort(key=self.problem.objective)         
        return population[0:2]
    
    def reproduction(self, males, females):
        generation = []
        for i in range(len(males)):
            child1 = []
            child2 = []
            
            for j in range(len(males[i])):
                if random.random() < 0.5:
                    child1.append(males[i][j])
                    child2.append(females[i][j])
                else:
                    child1.append(females[i][j])
                    child2.append(males[i][j])
            
            generation.append(child1)
            generation.append(child2)
        
        return generation    
        
    def assortment(self, new_population: list):
        combined = self.population + new_population
        combined.sort(key=self.problem.objective, reverse=True)
        self.population = combined[:len(self.population)]
    
    
    def bestIndividual(self, population):
        return max(population, key=lambda ind: self.problem.objective(ind))
    
    def printPopulation(self):
        for i in self.population:
            print(i, self.problem.objective(i))
        print(" ")

    def compare(self, sol1, sol2):
        for i in range(len(sol1)):
            if sol1[i] != sol2[i]:
                return False
        return True