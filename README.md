# 🎬 MovieMatch AI - Movie Recommendation System

Uma aplicação web desenvolvida em **Python** que utiliza técnicas de **Machine Learning** e **Processamento de Linguagem Natural (NLP)** para recomendar filmes semelhantes com base em suas características.

O sistema utiliza o método **Content-Based Filtering**, analisando informações como sinopse, gêneros, elenco, diretor e palavras-chave para encontrar filmes similares.

Após o treinamento, o modelo é salvo em arquivos **Pickle (.pkl)**, permitindo que a aplicação carregue instantaneamente sem necessidade de processar novamente o dataset.

---

## 🚀 Funcionalidades

- 🎬 Recomendação de filmes por similaridade.
- 🖼️ Exibição dos pôsteres utilizando a API do TMDB.
- ⭐ Exibição da avaliação do filme.
- 📅 Exibição da data de lançamento.
- 🎭 Exibição dos gêneros.
- 📝 Exibição da sinopse.
- 🔎 Pesquisa de filmes através de uma interface intuitiva.
- 🌐 Interface web desenvolvida com Streamlit.
- ⚡ Carregamento rápido utilizando arquivos Pickle.
- ☁️ Deploy da aplicação para acesso online.

---

## 🧠 Como funciona

## 🧠 Como funciona

O modelo foi desenvolvido utilizando o **TMDB 5000 Movie Dataset**.

Durante a fase de treinamento são realizadas as seguintes etapas:

- Junção das bases de filmes e créditos.
- Limpeza e tratamento dos dados.
- Extração de:
  - Sinopse
  - Gêneros
  - Palavras-chave
  - Elenco
  - Diretor
- Criação de uma coluna contendo todas as características do filme.
- Vetorização utilizando **CountVectorizer**.
- Cálculo da similaridade utilizando **Cosine Similarity**.
- Serialização do modelo em arquivos **.pkl** para utilização na aplicação.

A aplicação web utiliza apenas os arquivos gerados (`movie_list.pkl` e `similarity.pkl`), dispensando o processamento do dataset a cada inicialização.

---

## 🛠️ Tecnologias Utilizadas

### Linguagem

- Python 3

### Bibliotecas

- Pandas
- Scikit-learn
- Streamlit
- Requests
- Pickle
- AST

### Machine Learning

- Content-Based Filtering
- CountVectorizer
- Cosine Similarity

### APIs

- TMDB API

### Dataset

- TMDB 5000 Movie Dataset (Kaggle)

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/movie-recommendation.git
```

### 2. Entre na pasta

```bash
cd movie-recommendation
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure sua chave da API do TMDB

Adicione sua chave da API no arquivo responsável pelas requisições.

### 5. Execute

```bash
streamlit run app.py
```
---

## 📸 Funcionalidades da Interface

A aplicação permite:

- Pesquisar um filme.
- Visualizar recomendações semelhantes.
- Exibir pôsteres.
- Visualizar nota do TMDB.
- Visualizar gêneros.
- Visualizar data de lançamento.
- Ler a sinopse de cada filme recomendado.

---

## 🚀 Melhorias Futuras

- Utilizar **TF-IDF** para aprimorar a vetorização dos textos.
- Implementar **Stemming** utilizando NLTK.
- Adicionar busca inteligente (*Fuzzy Search*).
- Exibir o percentual de similaridade entre os filmes.
- Sistema de favoritos.
- Histórico de pesquisas.
- Salvar o modelo utilizando **Pickle** para reduzir o tempo de carregamento.
- Sistema híbrido de recomendação (Content-Based + Collaborative Filtering).
- Containerização da aplicação com Docker.
- Pesquisa por aproximação de nomes de filmes.
- Recomendação personalizada baseada em avaliações dos usuários.
- Colocar filmes de acordo com seu gosto musical (ouço ABBA, recomenda Mamma Mia)
- Mudar biblioteca de filmes (mais recentes e maior)