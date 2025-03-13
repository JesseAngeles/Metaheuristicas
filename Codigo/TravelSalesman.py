from typing import Any
import random
from HillClimbing import HillClimbing

def evaluateTravelSalesman(space:list[int],information:list[list[int]]):
    distance:int = 0
    num_cities:int = len(space)

    for i in range(num_cities):
        current_city = space[i]
        next_city = space[(i + 1) % num_cities]  
        distance += information[current_city][next_city]

    return distance

def valueTravelSalesman(space:list[Any],information:list[Any], position:int, value:int, option: int = 0):
    best_options:list = []
    
    if option == 3:
        new_space = space[:]
        pos = random.randrange(0, len(space))
        new_space[position], new_space[pos] = new_space[pos], new_space[position]
        new_value:int = evaluateTravelSalesman(new_space, information)

        if new_value < value: 
            space[:] = new_space[:]
            return new_value


    for i in range(position + 1, len(space)):
        new_space = space[:]

        new_space[position], new_space[i] = new_space[i], new_space[position]

        new_value:int = evaluateTravelSalesman(new_space, information)

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
    epochs: int = 10
    space: list[int] = [0, 1, 2, 3, 4]
    information:list[list[int]] = [
    [0, 10, 15, 20, 25],  
    [10, 0, 35, 30, 40],  
    [15, 35, 0, 45, 50],  
    [20, 30, 45, 0, 55],  
    [25, 40, 50, 55, 0] 
]
    
    TravelSalesman = HillClimbing(space, information, evaluateTravelSalesman, valueTravelSalesman, True)

    TravelSalesman.print()
    TravelSalesman.RMHC(epochs)
    TravelSalesman.print()
