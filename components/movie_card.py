import streamlit as st
from components.movie_details import movie_details


def movie_card(details, similarity):
    """
    Exibe um card moderno com as informações do filme.
    """
    if not details:
        details = {
            "id": 0,
            "title": "Filme Indisponível",
            "poster": None,
            "rating": 0.0,
            "year": "N/A",
            "genres": "Não informado",
            "runtime": 0,
            "overview": "Não foi possível carregar os detalhes deste filme.",
            "tmdb_url": "https://www.themoviedb.org"
        }

    with st.container():
        # Injeta uma div âncora para que o CSS `:has()` estilize o container do Streamlit
        st.markdown('<div class="movie-card-anchor"></div>', unsafe_allow_html=True)

        genres = details.get("genres") or "Não informado"
        runtime = details.get("runtime")
        runtime_text = f"{runtime} min" if runtime else "Não informado"

        # Poster
        if details.get("poster"):
            st.image(
                details["poster"],
                use_container_width=True
            )
        else:
            # Espaço reservado visualmente agradável se não houver poster
            st.markdown(
                """
                <div style="height: 270px; background: #1E293B; border-radius: 18px; 
                            display: flex; align-items: center; justify-content: center;
                            font-size: 40px; border: 1px dashed rgba(255,255,255,0.1); margin-bottom: 10px;">
                    🎬
                </div>
                """,
                unsafe_allow_html=True
            )

        # Nota e ano
        c1, c2 = st.columns(2)

        rating_val = details.get("rating", 0.0)
        rating_text = f"{rating_val:.1f}" if rating_val else "N/A"

        with c1:
            st.markdown(
                f"""
                <div class="rating-badge">
                    ⭐ {rating_text}
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div class="year-badge">
                    📅 {details.get("year") or "N/A"}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div class="movie-title">
                {details.get("title", "Sem título")}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="compatibility">

                <div class="compatibility-title">
                    Compatibilidade
                </div>

                <div class="progress">

                    <div
                        class="progress-fill"
                        style="width:{similarity}%;">
                    </div>

                </div>

                <div class="compatibility-value">
                    {similarity:.1f}%
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        if similarity >= 90:
            reason = "🔥 Excelente correspondência"
        elif similarity >= 80:
            reason = "⭐ Muito semelhante"
        elif similarity >= 70:
            reason = "🎯 Boa recomendação"
        else:
            reason = "🎬 Vale a pena conhecer"

        st.caption(reason)
        st.caption(f"🎭 {genres}")
        st.caption(f"⏱️ {runtime_text}")

        overview = details.get("overview") or ""
        if len(overview) > 120:
            overview = overview[:120] + "..."
        st.write(overview)

        # Botão para abrir o dialog com os detalhes completos do filme
        if st.button("🔍 Ver Detalhes", key=f"btn_{details.get('id', 0)}", use_container_width=True):
            movie_details(details)

        st.link_button(
            "🎬 TMDB",
            details.get("tmdb_url", "https://www.themoviedb.org"),
            use_container_width=True
        )