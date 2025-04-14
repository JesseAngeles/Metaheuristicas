import csv
import statistics
from collections import defaultdict

filename = "simulated_annealing_results.csv"

energy_data = defaultdict(list)
time_data = defaultdict(list)

# Leer el archivo CSV original
with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        func = row["function"]
        energy = float(row["energy"])
        time_sec = float(row["time_seconds"])
        energy_data[func].append(energy)
        time_data[func].append(time_sec)

# Función para calcular estadísticas
def compute_stats(data_dict):
    stats = {}
    for func, values in data_dict.items():
        stats[func] = {
            "min": min(values),
            "max": max(values),
            "mean": statistics.mean(values),
            "median": statistics.median(values),
            "std": statistics.stdev(values) if len(values) > 1 else 0.0
        }
    return stats

# Formatear número en notación científica si es muy grande o muy pequeño
def fmt(x):
    if abs(x) >= 1e5 or abs(x) <= 1e-3:
        return f"{x:.4e}"  # notación científica
    else:
        return f"{x:.4f}"

# Guardar estadísticas en CSV
def save_stats_csv(stats, filename):
    with open(filename, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["function", "min", "max", "mean", "median", "std"])
        for func, s in stats.items():
            writer.writerow([func, fmt(s["min"]), fmt(s["max"]), fmt(s["mean"]), fmt(s["median"]), fmt(s["std"])])

# Calcular y guardar
energy_stats = compute_stats(energy_data)
time_stats = compute_stats(time_data)

save_stats_csv(energy_stats, "energy_stats.csv")
save_stats_csv(time_stats, "time_stats.csv")

print("✅ Estadísticas guardadas en 'energy_stats.csv' y 'time_stats.csv'")
