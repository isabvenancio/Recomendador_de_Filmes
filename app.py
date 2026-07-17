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
    "Escolha um filme e descubra outros títulos semelhantes."
)


selected_movie = st.selectbox(
    "Selecione um filme:",
    movies["title"].values
)


if st.button("🎥 Recomendar"):

    with st.spinner("Buscando recomendações..."):

        recommendations = recommend(
            selected_movie,
            movies,
            similarity
        )

    if recommendations:

        cols = st.columns(5)

        for col, movie in zip(cols, recommendations):

            with col:

                poster = get_movie_poster(movie)

                if poster:
                    st.image(
                        poster,
                        use_container_width=True
                    )
                else:
                    st.warning("Pôster não encontrado")

                st.markdown(
                    f"**{movie}**"
                )

    else:
        st.error("Nenhuma recomendação encontrada.")