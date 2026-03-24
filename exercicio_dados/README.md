# Análise de Vendas de Livraria - Exercício de Dados Usando Pandas

Um projeto abrangente de análise de dados explorando dados de vendas de uma livraria fictícia usando Python, pandas e matplotlib. Este notebook Jupyter demonstra um fluxo de trabalho completo de análise de dados, desde a criação do conjunto de dados até a visualização e extração de insights.

## 📊 Visão Geral do Projeto

Este projeto analisa dados fictícios de vendas de uma livraria para extrair insights de negócio, incluindo:
- Desempenho de vendas por categoria e região
- Vendedores com melhor performance
- Tendências de receita ao longo do tempo
- Análise de transações de alto valor
- Limpeza e pré-processamento de dados

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **pandas** - Manipulação e análise de dados
- **matplotlib** - Visualização de dados
- **NumPy** - Operações numéricas

## 📁 Estrutura do Conjunto de Dados

O conjunto de dados contém **50 registros de vendas** com as seguintes colunas:

| Coluna | Descrição |
|--------|-------------|
| `id_venda` | ID da transação |
| `data` | Data da venda |
| `produto` | Título do livro |
| `categoria` | Categoria do livro |
| `quantidade` | Quantidade vendida |
| `preco_unit` | Preço unitário (R$) |
| `vendedor` | Nome do vendedor |
| `regiao` | Região da venda |
| `total_venda` | Valor total da venda (calculado) |

### Categorias de Livros
- Literatura
- Infantil
- Ciências
- Tecnologia
- Fantasia
- Autoajuda
- Filosofia

### Regiões de Venda
- Sudeste
- Sul
- Nordeste
- Norte
- Centro-Oeste

### Vendedores
- Ana Lima
- Carlos Mendes
- Bruno Costa
- Fernanda Rocha

## 📈 Principais Análises Realizadas

### 1. **Análise Exploratória de Dados (EDA)**
- Informações do conjunto de dados
- Validação de tipos de dados
- Detecção de valores ausentes
- Estatísticas descritivas

### 2. **Métricas de Desempenho de Vendas**
- Receita total: **R$ 7.538,40**
- Receita por categoria
- Ranking de vendedores
- Produtos mais vendidos (por quantidade)
- Ticket médio por região

### 3. **Visualizações**
O notebook gera um dashboard com três gráficos:
- **Gráfico de barras**: Receita por categoria
- **Gráfico de barras**: Ranking de vendedores
- **Gráfico de pizza**: Distribuição de receita por região

### 4. **Análises Avançadas**
- **Evolução mensal da receita**: Acompanhamento das vendas de janeiro a junho
- **Gráfico de linha**: Visualização da tendência de vendas ao longo do tempo
- **Análise de ticket médio**: Identificação dos vendedores com melhor performance
- **Análise de transações de alto valor**: Filtragem e análise de vendas > R$ 200
- **Limpeza de dados**: Tratamento de valores ausentes com cenários do mundo real

## 🎯 Principais Descobertas

- **Categoria com maior faturamento**: Tecnologia com R$ 2.788,80 em receita
- **Vendedor com maior faturamento**: Bruno Costa com R$ 3.392,90 em vendas totais
- **Produto mais vendido**: Atomic Habits com 25 unidades comercializadas
- **Região com maior ticket médio**: Nordeste (R$ 178,94)
- **Vendedor com melhor ticket médio**: Bruno Costa (R$ 161,57 por venda)
- **Transações de alto valor**: Dominadas pela categoria Tecnologia

## 📁 Arquivos Gerados

O notebook gera:
- `vendas_livraria.csv` - Conjunto de dados bruto
- `dashboard_livraria.png` - Dashboard visual (150 DPI)

## 🚀 Como Executar

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   ```

2. **Instale as dependências necessárias**
   ```bash
   pip install pandas matplotlib numpy
   ```

3. **Execute o Jupyter notebook**
   ```bash
   jupyter notebook analise_livraria.ipynb
   ```

## 📝 Estrutura do Notebook

O notebook está organizado nas seguintes seções:

1. **Exercício Base**
   - Importação de bibliotecas
   - Criação do conjunto de dados
   - Exploração inicial
   - Análise básica de vendas
   - Visualizações

2. **Desafios Extras**
   - Cálculo de faturamento mensal
   - Visualização de tendência de vendas
   - Ticket médio por vendedor
   - Filtragem de transações de alto valor
   - Limpeza de dados com valores ausentes

## 💡 Aprendizados Demonstrados

Este projeto demonstra:
- Criação de conjuntos de dados sintéticos para análise
- Realização de operações de agrupamento e agregações
- Criação de visualizações profissionais
- Tratamento de problemas de qualidade de dados do mundo real
- Extração de insights acionáveis para negócios

## 📄 Licença

Este projeto foi criado para fins educacionais. Sinta-se à vontade para usar e modificar para aprender técnicas de análise de dados.

---

**Nota**: Todos os dados neste projeto são fictícios e gerados para fins de demonstração.
