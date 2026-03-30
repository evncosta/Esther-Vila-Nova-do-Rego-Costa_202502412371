# 📚 Análise de Catálogo de Livros (Desafio Pandas)

Este projeto contém a resolução de um desafio prático de manipulação e análise de dados usando Python e a biblioteca **Pandas**. O objetivo foi explorar, limpar e extrair insights de um dataset simulado de uma livraria online com quase 12.000 registros.

## 🛠️ Tecnologias Utilizadas
* Python 3.x
* Pandas (para manipulação e análise de dados)
* Jupyter Notebook (ambiente de execução)
* Openpyxl (para exportação dos resultados em `.xlsx`)

## 📋 Sobre o Dataset
O arquivo original `livros.csv` possui 11.967 linhas e 5 colunas separadas por ponto-e-vírgula (`;`):
* `titulo`: Título completo do livro (texto)
* `autor`: Nome do autor (texto)
* `isbn`: Código ISBN do livro (numérico/texto)
* `paginas`: Número de páginas (inteiro)
* `ano`: Ano de publicação (numérico)

## 🚀 Etapas do Projeto
O notebook foi estruturado e documentado em três níveis de complexidade:

### 🟢 Nível 1 — Exploração Inicial
* Carregamento do arquivo `.csv` lidando com o separador correto.
* Inspeção da estrutura dos dados (`info`, `describe`).
* Mapeamento de valores nulos por coluna.
* Verificação de dados inconsistentes (ex: livros cadastrados com 0 páginas).

### 🔵 Nível 2 — Transformação e Limpeza
* Criação da coluna `faixa_paginas` para categorizar os livros em "Curto" (<150), "Médio" (150-350) ou "Longo" (>350).
* Remoção de registros inválidos (páginas zeradas).
* Tratamento de valores nulos na coluna `ano` utilizando a mediana para não distorcer a base.
* Criação de uma coluna calculada `decada`.

### 🟡 Nível 3 — Análise Avançada (Bônus)
* Cálculo da média de páginas por década utilizando `groupby`.
* Identificação do Top 10 autores com mais livros no catálogo.
* Análise da distribuição de tamanho dos livros publicados após 2010.
* Exportação do DataFrame limpo e processado para um arquivo Excel final (`livros_analisados.xlsx`).

## 💻 Como Executar Localmente

1. Certifique-se de ter o Python instalado na sua máquina.
2. Instale as bibliotecas necessárias rodando o comando abaixo no seu terminal:
   ```bash
   pip install pandas openpyxl notebook
   ```
3. Garanta que o arquivo `livros.csv` esteja salvo exatamente na mesma pasta do seu arquivo `.ipynb`.
4. Abra o Jupyter Notebook (ou a extensão do Jupyter no VS Code), execute as células em ordem e o arquivo final em Excel será gerado automaticamente.
