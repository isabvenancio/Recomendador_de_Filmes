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
footer()

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

        for col, movie in zip(cols, recommendations):

            with col:

                details = get_movie_details(movie["id"])

                movie_card(
                    details,
                    movie["similarity"]
                )

    else:
        st.error("Nenhuma recomendação encontrada.")