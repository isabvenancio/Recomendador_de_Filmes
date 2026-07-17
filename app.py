import streamlit as st
from recommendation import load_data, recommend, get_movie_details

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

                details = get_movie_details(movie["id"])

                if details:
                    st.image(
                        details,
                        use_container_width=True
                    )
                else:
                    st.warning("Pôster não encontrado")

                st.markdown(
                    f"**{movie}**"
                )

    else:
        st.error("Nenhuma recomendação encontrada.")

st.image(details["poster"])

st.markdown(f"### {details['title']}")

st.caption(f"⭐ {details['rating']:.1f}")

st.caption(f"📅 {details['year']}")

st.caption(f"🎭 {details['genres']}")

st.caption(f"⏱️ {details['runtime']} min")

st.write(details["overview"][:180] + "...")

st.link_button(
    "🎬 Ver no TMDB",
    details["tmdb_url"]
)