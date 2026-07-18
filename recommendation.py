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

    for movie_index, score in movie_list:

        movie = movies.iloc[movie_index]

        recommendations.append(
            {
                "id": int(movie["movie_id"]),
                "title": movie["title"],
                "similarity": round(score * 100, 1)
            }
        )

    return recommendations

@st.cache_data(show_spinner=False)
def get_movie_details(movie_id):
    url = (
        f"https://api.themoviedb.org/3/search/movie"
        f"?api_key={API_KEY}"
        "&language=pt-BR"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        return {
            "title": data.get("title"),

            "original_title": data.get("original_title"),

            "poster": (
                f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
                if data.get("poster_path")
                else None
            ),

            "overview": data.get("overview"),

            "rating": round(data.get("vote_average", 0), 1),

            "votes": data.get("vote_count"),

            "year": (
                data.get("release_date", "")[:4]
                if data.get("release_date")
                else ""
            ),

            "genres": ", ".join(
                g["name"]
                for g in data.get("genres", [])
            ),

            "runtime": data.get("runtime"),

            "language": data.get("original_language"),

            "popularity": round(
                data.get("popularity", 0),
                1
            ),

            "homepage": data.get("homepage"),

            "tmdb_url": f"https://www.themoviedb.org/movie/{movie_id}"
        }

    except requests.RequestException:
        return None