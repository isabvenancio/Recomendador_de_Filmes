import ast
import pickle
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"


def extract_names(text):
    """Extrai os nomes de uma lista de dicionários."""

    try:
        return [item["name"] for item in ast.literal_eval(text)]
    except (ValueError, SyntaxError, TypeError):
        return []


def extract_top_cast(text, limit=3):
    """Retorna apenas os 3 principais atores."""

    try:
        cast = ast.literal_eval(text)
        return [actor["name"] for actor in cast[:limit]]
    except (ValueError, SyntaxError, TypeError):
        return []


def extract_director(text):
    """Retorna apenas o diretor."""

    try:
        crew = ast.literal_eval(text)

        for person in crew:
            if person["job"] == "Director":
                return [person["name"]]

    except (ValueError, SyntaxError, TypeError):
        pass

    return []


def collapse(items):
    """Remove espaços dos nomes."""

    return [item.replace(" ", "") for item in items]


print("Carregando datasets...")

movies = pd.read_csv(DATA_DIR / "tmdb_5000_movies.csv")
credits = pd.read_csv(DATA_DIR / "tmdb_5000_credits.csv")

movies = movies.merge(credits, on="title")

movies = movies[
    [
        "movie_id",
        "title",
        "overview",
        "genres",
        "keywords",
        "cast",
        "crew",
    ]
]

movies.dropna(inplace=True)

movies["overview"] = movies["overview"].apply(lambda x: x.split())

movies["genres"] = movies["genres"].apply(extract_names)
movies["keywords"] = movies["keywords"].apply(extract_names)
movies["cast"] = movies["cast"].apply(extract_top_cast)
movies["crew"] = movies["crew"].apply(extract_director)

movies["genres"] = movies["genres"].apply(collapse)
movies["keywords"] = movies["keywords"].apply(collapse)
movies["cast"] = movies["cast"].apply(collapse)
movies["crew"] = movies["crew"].apply(collapse)

movies["tags"] = (
    movies["overview"]
    + movies["genres"]
    + movies["keywords"]
    + movies["cast"]
    + movies["crew"]
)

movies = movies[["movie_id", "title", "tags"]].copy()

movies["tags"] = movies["tags"].apply(lambda x: " ".join(x).lower())

pickle.dump(movies, open(BASE_DIR / "movies.pkl", "wb"))

print(f"Arquivo movies.pkl criado com sucesso!")
print(f"Quantidade de filmes: {len(movies)}")