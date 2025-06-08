import pandas as pd

# Cargar el archivo CSV con los resultados
df = pd.read_csv("./results/mao_cec_dataset.csv")
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
    print(f"  - Damage: {mejor_fila['Damage']}")
    print(f"  - Regeneration: {mejor_fila['Regeneration']}")
    print(f"  - Tournament: {mejor_fila['Tournament']}")
    print(f"  - Alpha: {mejor_fila['Alpha']}")
    print(f"  - BestScore: {mejor_fila['BestScore']:.4f}")
    print(f"  - WorstScore: {mejor_fila['WorstScore']:.4f}")
    print(f"  - MeanScore: {mejor_fila['MeanScore']:.4f}")
    print(f"  - StdDev: {mejor_fila['StdDev']:.4f}")
