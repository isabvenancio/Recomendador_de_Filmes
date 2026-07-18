import streamlit as st
from recommendation import load_data, recommend, get_movie_details
from components.styles import load_css
from components.navbar import navbar
from components.hero import hero
from components.movie_selector import movie_selector
from components.movie_card import movie_card
from components.footer import footer

st.set_page_config(
    page_title="MovieMatch AI",
    page_icon="🎬",
    layout="wide"
)

load_css()
navbar()
hero()

movies, similarity = load_data()

selected_movie, recommend_button = movie_selector(
    movies["title"].values
)

if recommend_button:

    with st.spinner("Buscando recomendações..."):

        recommendations = recommend(
            selected_movie,
            movies,
            similarity
        )

    if recommendations:

        st.subheader("🍿 Recomendações")

        cols = st.columns(5)

        for idx, (col, movie) in enumerate(zip(cols, recommendations)):

            with col:

                details = get_movie_details(movie["id"])
                
                if not details:
                    # Fallback local com base nos dados que já possuímos
                    details = {
                        "id": movie["id"],
                        "title": movie["title"],
                        "poster": None,
                        "rating": 0.0,
                        "votes": 0,
                        "year": "N/A",
                        "genres": "Não informado",
                        "runtime": None,
                        "language": "N/A",
                        "popularity": 0.0,
                        "overview": "Detalhes indisponíveis no momento (sem conexão com TMDB).",
                        "homepage": None,
                        "tmdb_url": f"https://www.themoviedb.org/movie/{movie['id']}"
                    }

                movie_card(
                    details,
                    movie["similarity"],
                    card_index=idx
                )

    else:
        st.error("Nenhuma recomendação encontrada.")

footer()