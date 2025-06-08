import pandas as pd

# Cargar el archivo CSV con los resultados
df = pd.read_csv("results/mao_dataset_sfp.csv")

# Lista de problemas a evaluar
problemas = ["SumFunction", "sfp", "TSP"]

# Analizar cada problema individualmente
for problema in problemas:
    df_problema = df[df["Problem"] == problema]
    
    if df_problema.empty:
        print(f"No hay datos para {problema}")
        continue

    # Encontrar la fila con el mejor 'BestScore'
    mejor_fila = df_problema.loc[df_problema["StdDev"].idxmin()]

    print(f"\n Mejor configuración para {problema}:")
    print(f"  - Damage: {mejor_fila['Damage']}")
    print(f"  - Regeneration: {mejor_fila['Regeneration']}")
    print(f"  - Tournament_size: {mejor_fila['Tournament_size']}")
    print(f"  - alpha: {mejor_fila['alpha']}")
    print(f"  - BestScore: {mejor_fila['BestScore']:.4f}")
    print(f"  - WorstScore: {mejor_fila['WorstScore']:.4f}")
    print(f"  - MeanScore: {mejor_fila['MeanScore']:.4f}")
    print(f"  - StdDev: {mejor_fila['StdDev']:.4f}")
