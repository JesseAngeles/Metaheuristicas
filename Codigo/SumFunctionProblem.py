from HillClimbing import HillClimbing

epochs:int = 100
state:list[int] = [0,1,2,3,4]
aditional_information:list = []

def objectiveFunction(aditional_information, state):
    total_sum:float = 0
    
    for val in state:
        total_sum += val**2
   
    return -total_sum

def neighboursFunction(state:list[any], index:int)->list[list[any]]:
    neighbour1 = state[:]
    neighbour2 = state[:]
    
    neighbour1[index] -= 1
    neighbour2[index] += 1
    
    if neighbour1[index] < -10:
        neighbour1[index] = 10 
        
    if neighbour2[index] > 10:
        neighbour2[index] = -10 

    return [neighbour1,neighbour2]

sf = HillClimbing(state, aditional_information, objectiveFunction, neighboursFunction)

sf.Print(sf.state)   
sf.HillClimbing(sf.RandomMutationhillClimbing, epochs, True)
sf.Print(sf.state) 