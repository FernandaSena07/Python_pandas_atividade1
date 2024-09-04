import pandas as pd

# Substitua pelo caminho do seu arquivo CSV
file_path = './CSV/tmdb_5000_movies.csv'

# Ler o arquivo CSV
df = pd.read_csv(file_path)

# Mostrar as primeiras linhas do dataset
print("Primeiras linhas do dataset:")
print(df.head())

# Verificar as colunas disponíveis
print("\nColunas disponíveis no dataset:")
print(df.columns)

# Demonstrar dados das colunas 'title' e 'overview'
print("\nDados das colunas 'title' e 'overview':")
print(df[['title', 'overview']].head())

# Exemplo de disposição de filmes e suas descrições
print("\nExemplo de filmes e suas descrições:")
for _, row in df[['title', 'overview']].dropna().head(3).iterrows():
    print(f"{row['title']} | {row['overview']}")
