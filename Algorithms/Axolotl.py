import random

from Algorithms.Metaheuristic import Metaheuristic

class Axolotl(Metaheuristic):
    def __init__(self, problem, population_size = 10, damage = 0.5, regeneration = 0.1, tournament_size = 3, alpha = 0.5):
        super().__init__(problem)
        self.population_size = population_size
        self.damage = damage
        self.regeneration = regeneration
        self.torunament_size = tournament_size
        self.alpha = alpha
        
        self.resetProblem()

    # Abstract methods
    def resetProblem(self):
        super().resetProblem()
        self.population = [self.problem.generateInitialSolution() for _ in range(self.population_size)]

    def optimize(self, epochs: int = 1):
        for _ in range(epochs):
            random.shuffle(self.population)
            male = self.population[:int(self.population_size / 2)]
            female = self.population[int(self.population_size / 2):]

            best_male = self.bestIndividual(male)

            male = [ self.updateSolution(best_male, larva) for larva in male ]
            # for larva in self.population:
            #     print(larva)
            # print("")

            for larva in male:
                if random.random() < self.damage:
                    for dimention in range(len(larva)):
                        if random.random() < self.regeneration:
                            larva = self.problem.getNextNeighbour(larva, dimention)
            

            new_population = self.uniformCross(male, female)
            self.population = self.elitism(self.population, new_population, self.problem.objective)
            # for larva in self.population:
            #     print(larva)
            # print("")

    def bestIndividual(self, population):
        return max(population, key=lambda ind: self.problem.objective(ind))

    def updateSolution(self, solution_1: list, solution_2: list):
        solution: list = []
        for i in range(len(solution_1)):
            solution.append(solution_2[i] + self.alpha * (solution_1[i] - solution_2[i]))
        return self.problem.normalizeSolution(solution)
    
    def uniformCross(self, male, female):
        generation = []

        for i in range(len(male)):
            child1 = []
            child2 =[]
            
            for j in range(len(male[i])):
                if random.random() < 0.5:
                    child1.append(male[i][j])
                    child2.append(female[i][j])
                else:
                    child1.append(female[i][j])
                    child2.append(male[i][j])
            
            generation.append(child1)
            generation.append(child2)
            
        return generation
    
    def elitism(self, population: list, new_population: list, objective):
        combined = population + new_population
        combined.sort(key=objective)
        return combined[:len(population)]
