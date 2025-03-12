"""
    Angeles Lopez Erick Jesse
    Metaheuristicas
    Ascenso de colinas
"""

import csv

def evaluateKnapsach(max_weight, state:list):
    weight:int = 0
    value:int = 0
    
    for item in state:
        if item[0]:
            weight += item[1][0]
            value += item[1][1]
        
    if weight > max_weight:
        return 0
    else:
        return value
    
def bitSwitch(bit:int):
    if bit:
        return 0
    return 1
        

def HillClimbing1(space:list, states:list, max_weight:int, epochas:int):
    for epocha in range(epochas):
        print(f"epocha: {epocha}")
    
        objective = evaluateKnapsach(10, space)
        # Iterate the neighbourhod
        for i, cell in space:
            # Iterate states
            for state in states:
                new_cell = bitSwitch(cell[0])
                new_space = space
                new_space[i] = new_cell
                
                new_objective = evaluateKnapsach(10,new_space)
                print(f"old: {objective} \nnew: {new_objective}")
                
    
with open('./prompt/knapsach1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

        first_row = next(spamreader) 
        total_items = int(first_row[0])
        max_weight = int(first_row[1])
        items = []
        
        for row in spamreader:
            items.append([int(row[0]), int(row[1])])  
            
        # Init state
        init_space:list = []
        for item in items:
            init_space.append([1,item])

        states = {0,1}

print(init_space, states, max_weight)

HillClimbing1(init_space, states, max_weight, 10)
