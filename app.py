import streamlit as st
from recommendation import load_data, recommend, get_movie_details

st.set_page_config(
    page_title="Recomendador de Filmes",
    page_icon="🎬",
    layout="wide"
)

movies, similarity = load_data()

st.title("🎬 Sistema de Recomendação de Filmes")

st.write(
    "Escolha um filme e descubra outros títulos semelhantes utilizando Machine Learning."
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

                if details is None:
                    st.warning("Informações indisponíveis.")
                    continue

                if details["poster"]:
                    st.image(
                        details["poster"],
                        use_container_width=True
                    )

                st.markdown(f"### {details['title']}")

                st.caption(f"⭐ {details['rating']}")

                st.caption(f"📅 {details['year']}")

                st.caption(f"🎭 {details['genres']}")

                st.caption(f"⏱️ {details['runtime']} min")

                overview = details["overview"]

                if overview:

                    if len(overview) > 150:
                        overview = overview[:150] + "..."

                    st.write(overview)

                st.link_button(
                    "🎬 Ver no TMDB",
                    details["tmdb_url"],
                    use_container_width=True
                )

    else:
        st.error("Nenhuma recomendação encontrada.")