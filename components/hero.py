import streamlit as st
import textwrap


def hero():

    st.markdown(
        textwrap.dedent(
            """
            <section class="hero">

                <div class="hero-badge">
                    🤖 Powered by Machine Learning
                </div>

                <h1 class="hero-title">
                    Descubra seu próximo filme favorito.
                </h1>

                <p class="hero-description">
                    Escolha um filme que você gosta e nosso algoritmo utiliza
                    Inteligência Artificial, Machine Learning e Similaridade de
                    Cosseno para encontrar recomendações personalizadas.
                </p>

            </section>
            """
        ),
        unsafe_allow_html=True
    )