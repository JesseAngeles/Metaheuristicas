"""
Angeles Lopez Erick Jesse
Metaheuristicas
"""

import copy

def evaluateKnapsach(max_weight, space:list):
    weight:int = 0
    value:int = 0
    
    for cell in space:
        if cell[0]:
            weight += cell[1][0]
            value += cell[1][1]
        
    if weight > max_weight:
        return -1
    else:
        return value

def hillClimbing(epochas:int, space:list, max_weight:int):
    value = evaluateKnapsach(max_weight=max_weight, space=space) 
        
    # Iterar sobre las epocas
    for epocha in range(epochas):
        # Iterar sobre la vecinidad
        for i in range(len(space)):
            new_space = copy.deepcopy(space)  
            
            # Modificar solo la celda correspondiente
            new_space[i][0] = 0 if new_space[i][0] == 1 else 1              
            new_value = evaluateKnapsach(max_weight=max_weight, space=new_space)

            # Evaluación
            if new_value > value:
                print(space)
                space[:] = new_space  
                value = new_value

    return space

epochas:int = 10
space:list = [[0,[3,2]],[0,[3,4]],[0,[5,6]]]
max_weight:int = 10

      
print(f"space: {space} = {evaluateKnapsach(max_weight=max_weight,space=space)}")
            
hillClimbing(epochas=epochas, space=space, max_weight=max_weight)

print(f"space: {space} = {evaluateKnapsach(max_weight=max_weight,space=space)}")