import streamlit as st
from components.movie_details import movie_details


def movie_card(details, similarity):
    """
    Exibe um card moderno com as informações do filme.
    """
    
    genres = details.get("genres") or "Não informado"
    runtime = details.get("runtime")

    runtime_text = f"{runtime} min" if runtime else "Não informado"

    # Poster
    if details["poster"]:
        st.image(
            details["poster"],
            use_container_width=True
        )

    # Nota e ano
    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            f"""
            <div class="rating-badge">
                ⭐ {details["rating"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            f"""
            <div class="year-badge">
                📅 {details["year"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="movie-title">
            {details["title"]}
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

    overview = details["overview"] or ""

    if len(overview) > 160:
        overview = overview[:160] + "..."

    st.write(overview)

    st.link_button(
    "🎬 Ver no TMDB",
    details["tmdb_url"],
    use_container_width=True
    )

    movie_details(details)