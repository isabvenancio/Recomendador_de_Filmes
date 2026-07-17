# 🎬 Sistema de Recomendação de Filme

Este projeto implementa um sistema de recomendação de filmes baseado em conteúdo (*Content-Based Filtering*), utilizando informações como sinopse, gênero, elenco e palavras-chave para sugerir filmes semelhantes.

O sistema foi desenvolvido em **Python** utilizando **Jupyter Notebook** e técnicas de Processamento de Linguagem Natural (NLP).

---

## 📌 Funcionalidades

- Leitura da base de dados do TMDB.
- União dos arquivos de filmes e créditos.
- Limpeza e tratamento dos dados.
- Extração de informações relevantes (gêneros, elenco, palavras-chave e descrição).
- Criação de uma coluna de características ("tags").
- Vetorização do texto utilizando **CountVectorizer**.
- Cálculo da similaridade entre filmes com **Cosine Similarity**.
- Recomendação dos 5 filmes mais semelhantes ao título informado.

---

## 🛠 Tecnologias Utilizadas

- Python 3
- Jupyter Notebook
- Pandas
- Scikit-learn
- AST (literal_eval)

---

## 📂 Base de Dados

Foi utilizada a base pública do **TMDB 5000 Movie Dataset**, disponível no Kaggle.

Baixe os arquivos e coloque-os na pasta raiz do projeto:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Instale as dependências:

```bash
pip install pandas scikit-learn
```

Ou, caso utilize o Jupyter Notebook:

```python
!pip install pandas scikit-learn
```

---

## ▶️ Como executar

1. Baixe os arquivos do dataset do TMDB.
2. Coloque os arquivos `.csv` na mesma pasta do notebook.
3. Execute todas as células do notebook em ordem.
4. Utilize a função:

```python
recommend("Avatar")
```

Exemplo de saída:

```
Guardians of the Galaxy
John Carter
Star Trek Into Darkness
Aliens
Star Trek Beyond
```

---

## ⚙️ Como funciona

O algoritmo segue as seguintes etapas:

1. Carrega os datasets.
2. Une as informações de filmes e créditos.
3. Seleciona apenas os atributos relevantes.
4. Converte colunas em formato JSON para listas.
5. Cria uma coluna chamada **tags**, reunindo todas as características do filme.
6. Transforma as tags em vetores numéricos utilizando **CountVectorizer**.
7. Calcula a similaridade entre todos os filmes usando **Cosine Similarity**.
8. Retorna os filmes mais semelhantes ao escolhido pelo usuário.

---

## 🚀 Melhorias Futuras

- Pesquisa por aproximação de nomes de filmes.
- Recomendação personalizada baseada em avaliações dos usuários.
- Colocar filmes de acordo com seu gosto musical (ouço ABBA, recomenda Mamma Mia)
- Mudar biblioteca de filmes (mais recentes e maior)