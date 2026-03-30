# 📚 Análise de Catálogo de Livros

Este projeto contém a resolução de desafios de análise de dados utilizando Python e a biblioteca Pandas. O objetivo foi explorar, limpar e extrair insights de um dataset contendo informações de quase 12.000 registros de uma livraria online.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas** (Manipulação, limpeza e análise de dados)
* **NumPy** (Operações numéricas auxiliares)
* **OpenPyXL** (Exportação dos resultados para Excel)
* **Jupyter Notebook** (Ambiente de execução)

---

## ⚙️ Como Executar

1. Clone o repositório ou baixe os arquivos do projeto.
2. Certifique-se de que as bibliotecas necessárias estão instaladas no seu ambiente. Caso não estejam, rode o comando abaixo no terminal:
   ```bash
   pip install pandas numpy openpyxl
   ```
3. Garanta que o arquivo de dados original (`livros.csv`) esteja salvo no mesmo diretório do notebook.
4. Abra o arquivo `.ipynb` em sua IDE preferida (VS Code, JupyterLab, Google Colab, etc.) e execute as células sequencialmente.

---

## 📊 Estrutura da Análise

O código foi construído e documentado em três etapas principais de complexidade:

### 🟢 Nível 1: Exploração Inicial
* Carregamento do dataset lidando com separadores de texto específicos (`sep=";"`).
* Inspeção da estrutura, identificação de tipos de dados incorretos e contagem de valores nulos.
* Mapeamento de anomalias, como livros registrados com 0 páginas.
* Contagem de publicações distintas agrupadas por ano.

### 🔵 Nível 2: Transformação e Limpeza
* Classificação dos livros criando uma nova coluna categórica (`faixa_paginas`: Curto, Médio ou Longo).
* Higienização do dataset com a remoção de registros inválidos (páginas zeradas).
* Imputação de dados ausentes na coluna de ano utilizando o cálculo da mediana.
* Engenharia de features criando uma coluna de agrupamento por `decada`.

### 🟡 Nível 3: Análise Avançada
* Agrupamento de dados (`groupby`) para descobrir a média de páginas por década.
* Levantamento dos 10 autores com mais obras no catálogo.
* Análise da distribuição do tamanho dos livros publicados exclusivamente após 2010.
* Exportação do DataFrame final limpo para o arquivo `livros_analisados.xlsx`.

---

## 📋 Dicionário de Dados Original

| Coluna | Tipo Esperado | Descrição |
| :--- | :--- | :--- |
| **titulo** | Texto | Título completo do livro |
| **autor** | Texto | Nome do autor |
| **isbn** | String/Numérico | Código ISBN de registro do livro |
| **paginas** | Inteiro | Número de páginas da edição |
| **ano** | Inteiro | Ano de publicação original |
