"""
Angeles Lopez Erick Jesse
Metaheuristicas
"""

def evaluateTravelSalesman(space:list[int],distances:list[list[int]]):
    distance:int = 0
    num_cities:int = len(space)

    for i in range(num_cities):
        current_city = space[i]
        next_city = space[(i + 1) % num_cities]  
        distance += distances[current_city][next_city]

    return distance


def hillClimbing(epochas:int, space:list[int], distances:list[list[int]]):
    value = evaluateTravelSalesman(space=space, distances=distances)

    # Iterar sobre las epocas
    for epocha in range(epochas):
        
        # Iterar sobre la vecindad
        for i in range(len(space) - 1):
            # Hacer el swap de dos elementos
            for j in range(i + 1, len(space)):
                new_space = space[:]
                new_space[i], new_space[j] = new_space[j], new_space[i]
                
                new_value = evaluateTravelSalesman(space=new_space, distances=distances)
                
                if new_value < value:
                    print(space)
                    space[:] = new_space
                    value = new_value
                    break

epochas:int = 1000
cities:int = 5
distances = [
    [0, 10, 15, 20, 25],  
    [10, 0, 35, 30, 40],  
    [15, 35, 0, 45, 50],  
    [20, 30, 45, 0, 55],  
    [25, 40, 50, 55, 0] 
]
space:list = [0,1,2,3,4]

print(f"space: {space} = {evaluateTravelSalesman(space=space, distances=distances)}")

hillClimbing(epochas=epochas, space=space, distances=distances)

print(f"space: {space} = {evaluateTravelSalesman(space=space, distances=distances)}")

