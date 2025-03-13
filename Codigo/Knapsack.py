from typing import Any
from HillClimbing import HillClimbing

def evaluateKnapsack(space: list[bool], information: list) -> int:
    max_weight = information[-1]
    weight: int = 0
    value: int = 0

    for i in range(len(space)):
        if space[i]:
            weight += information[i][0]
            value += information[i][1]

    if weight > max_weight:
        return -1

    return value

def valueKnapsack(space: list[Any], information: list[Any], position: int, value: int, option = 0):
    space[position] = not space[position]
    new_value: float = evaluateKnapsack(space, information)

    if new_value > value:
        return new_value
    return value

# Pruebas
if __name__ == "__main__":
    epochs: int = 2
    space: list[bool] = [False, False, False]
    information: list = [[3, 2], [3, 4], [5, 6], 10]
    
    Knapsack = HillClimbing(space, information, evaluateKnapsack, valueKnapsack, False)

    Knapsack.print()
    Knapsack.RMHC(epochs)
    Knapsack.print()
