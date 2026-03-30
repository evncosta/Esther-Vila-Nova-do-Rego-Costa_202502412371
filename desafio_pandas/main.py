import pandas as pd
import numpy as np

# ── 1. CARREGAR O DATASET ──────────────────────────────
# Lendo o arquivo com o separador correto indicado no enunciado
df = pd.read_csv("livros.csv", sep=";")
print("--- INFORMAÇÕES DO DATASET ---")
print(f"Shape: {df.shape}")  # Esperado: (11967, 5)

# ── 2. EXPLORAÇÃO INICIAL ─────────────────────────────
print("\n--- PRIMEIRAS LINHAS ---")
print(df.head())
print("\n--- INFO ---")
print(df.info())
print("\n--- ESTATÍSTICAS DESCRITIVAS ---")
print(df.describe())
print("\n--- DADOS NULOS ---")
print(df.isnull().sum())

# ── 3. LIMPEZA ────────────────────────────────────────
# Preencher nulos de 'ano' com a mediana
mediana_ano = df["ano"].median()
df["ano"] = df["ano"].fillna(mediana_ano).astype(int)

# Remover livros com 0 páginas
df_limpo = df[df["paginas"] > 0].copy()

# ── 4. TRANSFORMAÇÃO ──────────────────────────────────
def faixa_paginas(n):
    if n < 150: return "Curto"
    elif n <= 350: return "Médio"
    else: return "Longo"

# Aplicando a função para criar a coluna 'faixa_paginas'
df_limpo["faixa_paginas"] = df_limpo["paginas"].apply(faixa_paginas)

# Criando a coluna 'decada' usando divisão inteira
df_limpo["decada"] = (df_limpo["ano"] // 10) * 10

# ── 5. ANÁLISE (EXEMPLOS COMUNS) ──────────────────────
print("\n--- ANÁLISE DOS DADOS ---")

# 5.1. Quantidade de livros por faixa de tamanho (Curto, Médio, Longo)
print("\n1. Quantidade de livros por faixa de páginas:")
contagem_tamanho = df_limpo["faixa_paginas"].value_counts()
print(contagem_tamanho)

# 5.2. Quantidade de livros lançados por década
print("\n2. Quantidade de livros por década (ordem cronológica):")
contagem_decada = df_limpo["decada"].value_counts().sort_index()
print(contagem_decada)

# 5.3. Média de páginas dos livros por década
print("\n3. Média de páginas por década:")
media_paginas_decada = df_limpo.groupby("decada")["paginas"].mean().round(2)
print(media_paginas_decada)

# ── 6. EXPORTAR ───────────────────────────────────────
# Opcional: Se der erro de módulo no to_excel, instale o openpyxl (pip install openpyxl)
df_limpo.to_excel("livros_analisados.xlsx", index=False)
print("\n✅ Arquivo exportado com sucesso!")
