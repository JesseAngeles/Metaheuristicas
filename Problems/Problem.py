from abc import ABC, abstractmethod
from typing import Any

class Problem(ABC):
    def __init__(self,):
        self.information:Any = {}

    @abstractmethod
    def generateInformation(self, *args, **kwargs) -> None:
        pass
    
    @abstractmethod
    def objective(self, solution: Any) -> float:
        pass

    @abstractmethod
    def generateInitialSolution(self) -> Any:
        pass

    @abstractmethod
    def normalizeSolution(self, solution: Any) -> Any:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def getRandomNeighbour(self, solution:Any) -> Any:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def getNextNeighbour(self, solution:Any, *args, **kwargs) -> Any:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def getNeighbours(self, solution: Any) -> list:
        raise NotImplementedError("Subclasses should implement this!")

    @abstractmethod
    def printInformation(self) -> None:
        raise NotImplementedError("Subclasses should implement this!")