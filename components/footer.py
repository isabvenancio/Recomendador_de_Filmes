import streamlit as st
import textwrap


def footer():

    st.markdown(
        textwrap.dedent(
            """
            <div class="footer">

                <hr>

                <h3>🎬 MovieMatch AI</h3>

                <p>
                    Sistema de recomendação de filmes desenvolvido com
                    Machine Learning utilizando Python, Scikit-Learn,
                    Streamlit e a API do TMDB.
                </p>

                <div class="footer-tech">

                    <span>🐍 Python</span>

                    <span>📊 Scikit-Learn</span>

                    <span>🎬 TMDB API</span>

                    <span>⚡ Streamlit</span>

                </div>

                <div class="footer-links">

                    <a href="https://github.com/isabvenancio" target="_blank">
                        GitHub
                    </a>

                    <a href="https://linkedin.com/in/isabella-barela-venâncio" target="_blank">
                        LinkedIn
                    </a>

                </div>

                <p class="footer-copy">

                    © 2026 Isabella Barela

                </p>

            </div>
            """
        ),
        unsafe_allow_html=True
    )