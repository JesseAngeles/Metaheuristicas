import time
import csv
from Problems.Cec20171 import Cec2017
from Problems.cec2017.cec2017.simple import *
from Algorithms.SimulatedAnnealing1 import SimulatedAnnealing

functions = { f1, f2, f3, f4, f5, f6, f7, f8, f9, f10 }

dataset = []

for function in functions:
    cec_problem = Cec2017()
    dimension = 5
    cec_problem.generate_information(function, -100, 100, 100, dimension)

    sa = SimulatedAnnealing(cec_problem.information, 
                            cec_problem.energy, 
                            cec_problem.generate_initial_solution, 
                            cec_problem.random_neighbour)

    for i in range(100):
        sa.reset()

        start_time = time.time()
        while sa.temperature > sa.min_temperature:
            sa.stepSimpleSimulatedAnnealing()
        elapsed_time = time.time() - start_time

        record = {
            "function": function.__name__,
            "energy": sa.energy,
            "time_seconds": elapsed_time,
            "dimension": dimension
        }

        dataset.append(record)

        print(f"[{i+1}/100] Energy: {sa.energy:.4f}, Time: {elapsed_time:.4f}s, Function {function.__name__}")

# Guardar en un archivo CSV
with open("simulated_annealing_results.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["function", "energy", "time_seconds", "dimension"])
    writer.writeheader()
    writer.writerows(dataset)

print("\nResultados guardados en 'simulated_annealing_results.csv'")