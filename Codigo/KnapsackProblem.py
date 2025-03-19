from HillClimbing import HillClimbing

epochs:int = 100
state:list[bool] = [False, False, False]
aditional_information = [[3, 2], [3, 4], [5, 6], 10]

def objectiveFunction(aditional_information, state):
    max_weight = aditional_information[-1]
    weight: int = 0
    value: int = 0

    for i in range(len(state)):
        if state[i]:
            weight += aditional_information[i][0]
            value += aditional_information[i][1]

    if weight > max_weight:
        return max_weight - weight

    return value

def neighboursFunction(state:list[any])->list[list[any]]:
    neighbours = []
    for i in range(len(state)):
        neighbour = state[:]
        neighbour[i] = not neighbour[i]
        neighbours.append(neighbour)
    
    return neighbours

ks = HillClimbing(state, aditional_information, objectiveFunction, neighboursFunction)

ks.Print(ks.state)
ks.HillClimbing(ks.RandomMutationhillClimbing ,epochs, True)
ks.Print(ks.state)