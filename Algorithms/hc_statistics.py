import json
import numpy as np
from collections import defaultdict

# Nombre del archivo JSON
file_name = "hill_climbing_results.json"

# Leer el archivo JSON
with open(file_name, "r") as f:
    data = json.load(f)

# Agrupar resultados por función
results_by_function = defaultdict(list)

# Agregar valores por función
for entry in data:
    function_name = entry["function"]
    results_by_function[function_name].append(entry["final_objective"])

# Calcular estadísticas
stats = {}

for function, values in results_by_function.items():
    values = np.array(values)

    # Escala logarítmica
    safe_values = np.where(values != 0, values, 1)  # Evitar log(0)
    log_values = np.log(np.abs(safe_values)) * np.sign(values)

    stats[function] = {
        "peor": float(np.min(values)),
        "mejor": float(np.max(values)),
        "promedio": float(np.mean(values)),
        "mediana": float(np.median(values)),
        "desviacion_estandar": float(np.std(log_values)) 
    }

# Exportar estadísticas a JSON
output_file = "hill_climbing_stats.json"
with open(output_file, "w") as f:
    json.dump(stats, f, indent=4)

print(f"\nEstadísticas exportadas a '{output_file}'")
