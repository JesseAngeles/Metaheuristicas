from typing import Any
import random
from HillClimbing import HillClimbing

def evaluateSumFunction(space:list[float], information:None):
    total_sum:float = 0
    
    for cell in space:
        total_sum += cell**2
                    
    return total_sum

def valueSumfunction(space:list[Any],information:list[Any], position:int, value:int, option:int = 0):
    best_options:list = []

    if option == 3:
        new_space = space[:]
        pos = random.randrange(-10, 10)
        new_space[position], new_space[pos] = new_space[pos], new_space[position]
        new_value:int = evaluateSumFunction(new_space, information)

        if new_value < value:    
            space[:] = new_space[:]
            return new_value

    for j in range(20):
        new_space = space[:]
        new_space[position] = new_space[position] + j if new_space[position] + j <= 10 else new_space[position] + j - 20

        new_value:float = evaluateSumFunction(new_space,information)
        if new_value < value:
            if not option:
                space[:] = new_space[:]
                return new_value
    
            if option == 1 or option == 2:
                best_options.append([new_value, new_space])

    if option == 0:  # Si no se guarda nada
        return value

    elif option == 1:  
        if best_options:
            _, best_option = min(enumerate(best_options), key=lambda x: x[1][0])
            if best_option[0] < value:
                space[:] = best_option[1]
                return best_option[0]
    
    elif option == 2: 
        if best_options:
            _, best_option = max(enumerate(best_options), key=lambda x: x[1][0])
            if best_option[0] < value:
                space[:] = best_option[1]
                return best_option[0]

    return value

# Pruebas
if __name__ == "__main__":
    epochs: int = 2
    space: list[int] = [0, 1, 2, 3, 4]
    information:list = []
    
    SumFunction = HillClimbing(space, information, evaluateSumFunction, valueSumfunction, True)

    SumFunction.print()
    SumFunction.SAHC(epochs)
    SumFunction.print()
