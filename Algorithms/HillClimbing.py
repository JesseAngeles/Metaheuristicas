import random

class HillClimbing:
    def __init__(self, state, aditional_information, objective_function, neighbour_function, max_random = 30):
        self.state = state
        self.aditional_information = aditional_information
        self.objective_function = objective_function
        self.neighbour_function = neighbour_function
        self.max_random = max_random

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
        
    def RandomMutationhillClimbing(self, current_state)->list[any]:       
        for _ in range(self.max_random):
            random_pos = random.randrange(len(current_state))
            new_state = self.neighbour_function(current_state, random_pos,True)

            if self.objective_function(self.aditional_information, new_state) > self.objective_function(self.aditional_information, current_state):
                current_state = new_state
                break
        return current_state
        
    def HillClimbing(self, method, epochs:int, is_print: int):
        current_state = self.state
        for i in range(epochs):
            next_state = method(current_state)

            if is_print == 1:
                self.Print(next_state)
            elif is_print == 2:
                self.PrintObjective(next_state)

            if self.objective_function(self.aditional_information, next_state) == self.objective_function(self.aditional_information, current_state):
                if is_print:
                    print(f"No improve in {i}")
                break
            current_state = next_state
        
        self.state = current_state
    
    def PrintObjective(self, state):
        print(f"objective: {self.objective_function(self.aditional_information, state)}")


    def Print(self, state):
        print(f"state: {state}: {self.objective_function(self.aditional_information, state)}")