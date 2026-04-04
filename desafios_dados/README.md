# Análise de Vendas - Livraria 2024 📚📊

Este projeto é um exercício prático de análise de dados utilizando **Python**, focado no uso das bibliotecas **Pandas**, **Matplotlib** e **NumPy**. O objetivo é simular as operações de uma livraria fictícia no primeiro semestre de 2024, desde a criação de um dataset sintético até a geração de relatórios, visualizações e tratamento de dados corrompidos.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas:** Manipulação, exploração e limpeza de dados.
* **NumPy:** Geração de dados aleatórios estruturados.
* **Matplotlib:** Criação de gráficos e dashboards.

## ⚙️ Funcionalidades e Estrutura do Código

O projeto está dividido em etapas lógicas (células), simulando um fluxo de trabalho real de um Analista de Dados:

1.  **Criação do Dataset:** Geração de 50 registros de vendas aleatórios, contendo informações como produto, categoria, vendedor, região, quantidade e preço unitário. Os dados são exportados automaticamente para `vendas_livraria.csv`.
2.  **Exploração Inicial:** Inspeção básica do dataset (número de linhas/colunas, tipos de dados, contagem de nulos e estatísticas descritivas).
3.  **Análise de Vendas (KPIs):**
    * Cálculo do faturamento total.
    * Faturamento agrupado por categoria.
    * Ranking de vendedores por volume financeiro.
    * Top 3 produtos mais vendidos (em quantidade).
    * Ticket médio por região.
4.  **Dashboard Visual:** Geração de um painel contendo gráficos de barras horizontais, barras verticais e um gráfico de pizza, exportado automaticamente como `dashboard_livraria.png`.
5.  **Desafios Extras (Avançado):**
    * **Séries Temporais:** Cálculo da evolução do faturamento mês a mês e plotagem de um gráfico de linha (`tendencia_vendas.png`).
    * **Análise de Eficiência:** Descoberta do vendedor com o maior ticket médio por venda.
    * **Filtros Condicionais:** Identificação das categorias que dominam as vendas de alto valor (acima de R$ 200).
    * **Limpeza de Dados:** Inserção intencional de valores nulos (`NaN`) para demonstrar técnicas de identificação (`.isnull()`) e tratamento (`.dropna()`, `.fillna()`).

## 🚀 Como Executar

1.  Certifique-se de ter o Python instalado, juntamente com as bibliotecas necessárias:
    ```bash
    pip install pandas matplotlib numpy
    ```
2.  Copie os blocos de código para um ambiente como **Jupyter Notebook**, **Google Colab** ou um arquivo script `.py`.
3.  Execute as células sequencialmente.
4.  Verifique o diretório do projeto: os arquivos `vendas_livraria.csv`, `dashboard_livraria.png` e `tendencia_vendas.png` serão gerados automaticamente.

## 📂 Arquivos Gerados

* `vendas_livraria.csv`: O dataset bruto com os dados das vendas.
* `dashboard_livraria.png`: Painel contendo os três gráficos principais da análise.
* `tendencia_vendas.png`: Gráfico de linha mostrando a evolução mensal do faturamento.

---
*Projeto desenvolvido como exercício prático de manipulação e visualização de dados com Python.*