def linealDisplacement(population, objective, epsilon = 0.1):
    objectives = [ objective(individual) for individual in population ]

    min_objective = min(objectives)
    objectives = [ objective - min_objective + epsilon for objective in objectives]

    return objectives

def distance(solution_1, solution_2):
    distance = 0
    for i in range(len(solution_1)):
        distance += abs(solution_1[i] - solution_2[i])
    return distance
