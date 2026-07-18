import streamlit as st
import textwrap


def movie_selector(movie_titles):
    """
    Card responsável pela seleção do filme.
    """

    st.markdown(
        textwrap.dedent(
            """
            <div class="selector-card">

                <div class="selector-icon">
                    🎬
                </div>

                <h2 class="selector-title">
                    Qual filme você gostou?
                </h2>

                <p class="selector-subtitle">
                    Escolha um filme da lista abaixo e nosso algoritmo encontrará
                    cinco recomendações semelhantes utilizando Machine Learning.
                </p>

            </div>
            """
        ),
        unsafe_allow_html=True
    )

    movie = st.selectbox(
        "",
        movie_titles,
        label_visibility="collapsed"
    )

    recommend = st.button(
        "🎥 Encontrar Recomendações",
        use_container_width=True
    )

    return movie, recommend