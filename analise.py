import pandas as pd

# Projeto Analise de Entrega - Kauê Lopes
df = pd.read_csv('delivery_analise.csv')

print(f"Total pedidos: {len(df)}")
print(f"Tempo medio geral: {df['tempo_entrega_min'].mean():.1f} min")

print("\nTempo medio por bairro:")
print(df.groupby('bairro')['tempo_entrega_min'].mean().sort_values(ascending=False).round(1))
