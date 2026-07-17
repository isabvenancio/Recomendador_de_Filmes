import pickle
from pathlib import Path

import requests
import streamlit as st

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = Path(__file__).parent

API_KEY = st.secrets["TMDB_API_KEY"]


@st.cache_resource
def load_data():
    """
    Carrega os dados processados e gera a matriz de similaridade.
    Esta função é executada apenas uma vez enquanto o app estiver ativo.
    """

    with open(BASE_DIR / "movies.pkl", "rb") as file:
        movies = pickle.load(file)

    vectorizer = CountVectorizer(
        max_features=5000,
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(movies["tags"])

    similarity = cosine_similarity(vectors)

    return movies, similarity


def recommend(movie, movies, similarity):
    """
    Retorna os 5 filmes mais semelhantes ao selecionado.
    """

    if movie not in movies["title"].values:
        return []

    index = movies[movies["title"] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    for movie_index, _ in movie_list:
        recommendations.append(
            movies.iloc[movie_index]["title"]
        )

    return recommendations

@st.cache_data(show_spinner=False)
def get_movie_poster(title):
    """
    Busca o pôster do filme utilizando a API do TMDB.
    """

    url = (
        "https://api.themoviedb.org/3/search/movie"
        f"?api_key={API_KEY}"
        f"&query={title}"
        "&language=pt-BR"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not data.get("results"):
            return None

        poster = data["results"][0].get("poster_path")

        if not poster:
            return None

        return f"https://image.tmdb.org/t/p/w500{poster}"

    except requests.RequestException:
        return None