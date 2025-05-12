from Algorithms.Metaheuristic import Metaheuristic 

class HillClimbing(Metaheuristic):
    def __init__(self, problem, max_random:int = 30):
        super().__init__(problem)
        self.max_random: int = max_random

    # Abstract methods
    def resetProblem(self):
        return super().resetProblem()
    
    def optimize(self, epochs: int = 1):
        if not self.is_best:
            for _ in range(epochs):
                next_solution = self.method(self.solution)
                if self.isSameSolution(next_solution, self.solution):
                    self.is_best = True
                    break
                self.solution = next_solution
                
    # Class methods
    def randomMutation(self, current_solution: any) -> list:
        for _ in range(self.max_random):
            new_solution = self.problem.getRandomNeighbour(current_solution)
            if self.isBetterSolution(new_solution, current_solution):
                current_solution = new_solution
                break

        return current_solution
    
"""
    def SimpleHillClimbing(self, current_state)->list[any]:
        for i in range(len(current_state)):
            neighbours = self.neighbour_function(current_state, i)
            for neighbour in neighbours:
                if self.objective_function(self.aditional_information, neighbour) > self.objective_function(self.aditional_information, current_state):
                    current_state = neighbour
                    break    
        return current_state
        
    def SteepestAscentHillClimbing(self, current_state)->list[any]:
        current_max = current_state
        max = self.objective_function(self.aditional_information, current_state)
        
        for i in range(len(current_state)):
            neighbours = self.neighbour_function(current_state, i)
            for neighbour in neighbours:
                if self.objective_function(self.aditional_information, neighbour) > max:
                    max = self.objective_function(self.aditional_information, neighbour)
                    current_max = neighbour
        return current_max
        
    def NextAscentHillClimbing(self, current_state)->list[any]:
        current_min = current_state
        min = float('inf')
        
        for i in range(len(current_state)):
            neighbours = self.neighbour_function(current_state, i)
            for neighbour in neighbours:
                neighbour_objective_function = self.objective_function(self.aditional_information, neighbour)
                if (neighbour_objective_function > self.objective_function(self.aditional_information, current_state) and neighbour_objective_function < min):
                    min = neighbour_objective_function
                    current_min = neighbour
        return current_min
"""