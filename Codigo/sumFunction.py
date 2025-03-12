"""
Angeles Lopez Erick Jesse
Metaheuristicas
"""

import random

def evaluatesumFunction(space:list[float]):
    total_sum:float = 0
    
    for cell in space:
        total_sum += cell**2
                    
    return total_sum


def hillClimbing(epochas:int, space:list[float]):
    value:float = evaluatesumFunction(space=space)

    # Iterar sobre las epocas
    for epocha in range(epochas):
        
        # Iterar sobre la vecindad
        for i in range(len(space)):
            
            # Itear sobre estados
            for j in range(20):
                new_space = space[:]
                new_space[i] = new_space[i] + j if new_space[i] + j <= 10 else new_space[i] + j - 20
                
                new_value:float = evaluatesumFunction(space=new_space)
                if new_value < value:
                    print(space)
                    space[:] = new_space
                    value = new_value
                    break;

epochas:int = 1
space:list[float] = [0,1,2,3,4]

print(f"space: {space} = {evaluatesumFunction(space=space)}")

hillClimbing(epochas=epochas, space=space)

print(f"space: {space} = {evaluatesumFunction(space=space)}")

