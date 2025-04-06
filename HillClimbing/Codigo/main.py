from training import parallel_hill_climbing

parallel_hill_climbing(
    dimension=100,                        # Dimensión del problema
    epochs=1000000,                      # Número de épocas
    iterations=20,                        # Iteraciones por función
    num_workers=28,                      # Núcleos paralelos
    output_file="hill_climbing_results.json",  # Archivo de salida
)
