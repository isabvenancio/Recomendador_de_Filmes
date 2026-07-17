import streamlit as st
from recommendation import load_data, recommend, get_movie_poster

movies, similarity = load_data()

st.set_page_config(
    page_title="Recomendador de Filmes",
    page_icon="🎬",
    layout="wide"
)


st.title("🎬 Sistema de Recomendação de Filmes")

st.write(
    "Escolha um filme e receba recomendações baseadas em similaridade."
)


movie = st.selectbox(
    "Selecione um filme:",
    movies["title"].values
)


if st.button("🔎 Recomendar"):

    recommendations = recommend(movie, movies, similarity)

    st.subheader("Filmes recomendados:")

    cols = st.columns(5)

    for index, film in enumerate(recommendations):

        with cols[index]:
            st.subheader(film)

            poster = get_movie_poster(film)

            if poster:
                st.image(poster)
            else:
                st.write("Sem imagem")
