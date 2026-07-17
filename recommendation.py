import pandas as pd
import ast
import requests
import streamlit as st

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def convert(text):
    lista = []

    for i in ast.literal_eval(text):
        lista.append(i['name'])

    return lista

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)


def convert3(text):
    lista = []
    contador = 0

    for i in ast.literal_eval(text):
        if contador != 3:
            lista.append(i['name'])
            contador += 1
        else:
            break

    return lista

    movies['cast'] = movies['cast'].apply(convert3)


def fetch_director(text):
    lista = []

    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            lista.append(i['name'])
            break

    return lista

    movies['crew'] = movies['crew'].apply(fetch_director)


def collapse(lista):
    return [i.replace(" ", "") for i in lista]

    movies['genres'] = movies['genres'].apply(collapse)
    movies['keywords'] = movies['keywords'].apply(collapse)
    movies['cast'] = movies['cast'].apply(collapse)
    movies['crew'] = movies['crew'].apply(collapse)


def load_data():

    movies = pd.read_csv("data/tmdb_5000_movies.csv")
    credits = pd.read_csv("data/tmdb_5000_credits.csv")

    movies = movies.merge(credits, on="title")

    movies = movies[ ['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

    movies.dropna(inplace=True)

    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert3)
    movies['crew'] = movies['crew'].apply(fetch_director)

    movies['overview'] = movies['overview'].apply(lambda x: x.split())

    movies['genres'] = movies['genres'].apply(collapse)
    movies['keywords'] = movies['keywords'].apply(collapse)
    movies['cast'] = movies['cast'].apply(collapse)
    movies['crew'] = movies['crew'].apply(collapse)

    movies['tags'] = ( movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew'])

    new_df = movies[['movie_id', 'title', 'tags']]

    new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
    new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

    cv = CountVectorizer(max_features=5000, stop_words='english')

    vectors = cv.fit_transform(new_df['tags']).toarray()

    similarity = cosine_similarity(vectors)

    return new_df, similarity


def recommend(movie, movies, similarity):

    if movie not in movies['title'].values:
        return []

    index = movies[movies['title'] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append( movies.iloc[i[0]].title)

    return recommendations



API_KEY = st.secrets["TMDB_API_KEY"]


def get_movie_poster(title):

    url = (
        "https://api.themoviedb.org/3/search/movie"
        f"?api_key={API_KEY}"
        f"&query={title}"
        "&language=pt-BR"
    )


    response = requests.get(url)

    data = response.json()


    if data["results"]:

        poster = data["results"][0]["poster_path"]

        if poster:
            return (
                "https://image.tmdb.org/t/p/w500"
                + poster
            )


    return None