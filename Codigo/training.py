import time
import numpy as np
import json
from HillClimbing import HillClimbing
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from cec2017.cec2017.simple import *

# Función objetivo
def objectiveFunction(aditional_information, state):
    return -aditional_information([state])[0]


# Función de vecindad
def neighboursFunction(state, index: int):
    noise = np.random.normal()
    neighbour1 = state[:]
    neighbour2 = state[:]
    
    neighbour1[index] -= noise
    neighbour2[index] += noise
    
    return [neighbour1, neighbour2]

# Función para ejecutar cada optimización de forma paralela
def run_hill_climbing(function, dimension, epochs, iterations):
    results = []

    for i in range(iterations):
        # Nueva inicialización en cada iteración
        state = np.random.uniform(low=-100, high=100, size=dimension).tolist()

        # Inicializar Hill Climbing
        hc = HillClimbing(np.array(state), function, objectiveFunction, neighboursFunction)

        # Registrar el tiempo de inicio de la iteración
        start_time = time.time()

        # Guardar valores iniciales
        initial_objective = objectiveFunction(function, hc.state)
        hc.HillClimbing(hc.RandomMutationhillClimbing, epochs, is_print=0)

        # Calcular el tiempo de ejecución
        execution_time = time.time() - start_time

        # Guardar valores finales
        final_state = hc.state.tolist()
        final_objective = objectiveFunction(function, hc.state)

        # Almacenar el resultado, incluyendo el tiempo de ejecución
        result = {
            "function": function.__name__,
            "iteration": i + 1,
            "initial_objective": initial_objective,
            "final_objective": final_objective,
            "execution_time": execution_time  # Tiempo de ejecución en segundos
        }

        results.append(result)

    return results

def parallel_hill_climbing(dimension, epochs, iterations, num_workers, output_file):
    """
    Ejecuta la optimización Hill Climbing en paralelo para múltiples funciones.

    Parámetros:
    - dimension: int → Dimensión del problema
    - epochs: int → Número de iteraciones por función
    - iterations: int → Número de repeticiones por función
    - num_workers: int → Núcleos paralelos a utilizar
    - output_file: str → Nombre del archivo de salida JSON
    """

    # Funciones a optimizar
    all_functions = {f1, f2, f3, f4, f5,f6, f7, f8, f9, f10}

    # Usar `partial` para empaquetar argumentos adicionales
    run_partial = partial(run_hill_climbing, dimension=dimension, epochs=epochs, iterations=iterations)

    # Ejecutar en paralelo
    all_results = []

    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = [executor.submit(run_partial, f) for f in all_functions]

        for future in futures:
            all_results.extend(future.result())

    # Exportar resultados a JSON
    with open(output_file, "w") as f:
        json.dump(all_results, f, indent=4)

    # Imprimir resumen
    print(f"\nResultados exportados a '{output_file}'")
    # for res in all_results:
    #     print(f"Función: {res['function']}, Iteración: {res['iteration']}, "
    #           f"Inicial: {res['initial_objective']}, Final: {res['final_objective']}")
