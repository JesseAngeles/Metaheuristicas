from HillClimbing import HillClimbing

epochs:int = 100
state:list[int] = [0,1,2,3,4]
aditional_information:list = []

def objectiveFunction(aditional_information, state):
    total_sum:float = 0
    
    for val in state:
        total_sum += val**2
   
    return -total_sum

def neighboursFunction(state:list[any])->list[list[any]]:
    neighbours = []
    for i in range(len(state)):
        neighbour1 = state[:]
        neighbour2 = state[:]
        neighbour1[i] = neighbour1[i] - 1
        if neighbour1[i] < -10:
           neighbour1[i] = 10 
        
        neighbour2[i] = neighbour2[i] + 1
        if neighbour2[i] > 10:
           neighbour2[i] = -10 
        
        neighbours.append(neighbour1)
        neighbours.append(neighbour2)
    
    return neighbours

sf = HillClimbing(state, aditional_information, objectiveFunction, neighboursFunction)

sf.Print(sf.state)   
sf.HillClimbing(sf.RandomMutationhillClimbing, epochs, True)
sf.Print(sf.state) 