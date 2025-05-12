from abc import ABC, abstractmethod
from typing import Any

from Problems.Problem import Problem

class Metaheuristic(ABC):
    def __init__(self, problem: Problem):
        self.problem = problem

    # Abstract methods
    @abstractmethod
    def resetProblem(self):
        self.solution = self.problem.generateInitialSolution()
        self.is_best = False

    @abstractmethod
    def optimize(self, *args, **kwargs):
        pass

    def evaluate(self, state: Any) -> float:
        return self.problem.objective(state)

    def isBetterSolution(self, solution_1: Any, solution_2: Any)-> bool:
        return (self.problem.objective(solution_1) > 
            self.problem.objective(solution_2)) 

    def isSameSolution(self, solution_1: Any, solution_2: Any) -> bool:
        return (self.problem.objective(solution_1) ==
                self.problem.objective(solution_2)) 

    # Prints
    def printSolution(self) -> None:
        print(f'Solution: {self.solution}: {self.evaluate(self.solution)}')

    # Getters y Setter
    def getSolution(self) -> Any:
        return self.solution

    def setSolution(self, solution: Any):
        self.solution = solution
