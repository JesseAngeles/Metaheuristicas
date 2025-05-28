import pandas as pd

# Cargar el archivo CSV con los resultados
df = pd.read_csv("./results/ga_cec2017_dataset_parallel.csv")
for col in ["BestScore", "WorstScore", "MeanScore", "StdDev"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    
# Lista de problemas a evaluar
problemas = list(range(1, 11))

# Analizar cada problema individualmente
for problema in problemas:
    df_problema = df[df["FunctionIndex"] == problema]
    
    if df_problema.empty:
        print(f"No hay datos para {problema}")
        continue

    # Encontrar la fila con el mejor 'BestScore'
    mejor_fila = df_problema.loc[df_problema["BestScore"].idxmax()]

    print(f"\n Mejor configuración para {problema}:")
    print(f"  - Stationary: {mejor_fila['Stationary']}")
    print(f"  - Selection: {mejor_fila['Selection']}")
    print(f"  - Crossover: {mejor_fila['Crossover']}")
    print(f"  - Mutation: {mejor_fila['Mutation']}")
    print(f"  - Replacement: {mejor_fila['Replacement']}")
    print(f"  - BestScore: {mejor_fila['BestScore']:.4f}")
    print(f"  - WorstScore: {mejor_fila['WorstScore']:.4f}")
    print(f"  - MeanScore: {mejor_fila['MeanScore']:.4f}")
    print(f"  - StdDev: {mejor_fila['StdDev']:.4f}")
