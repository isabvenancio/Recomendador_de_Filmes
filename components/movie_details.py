import streamlit as st


@st.dialog("Detalhes do Filme", width="large")
def movie_details(details):

    if details is None:
        st.warning("Detalhes do filme não disponíveis.")
        return

    col1, col2 = st.columns([1, 2])

    with col1:

        if details.get("poster"):
            st.image(
                details["poster"],
                use_container_width=True
            )
        else:
            st.info("Pôster indisponível")

    with col2:

        st.markdown(f"## {details.get('title', 'Sem título')}")

        rating = details.get('rating', 0.0)
        st.markdown(f"⭐ **Nota:** {rating if rating else 'N/A'}")

        votes = details.get("votes")
        votes_text = f"{votes:,}" if votes is not None else "Não informado"
        st.markdown(f"👥 **Votos:** {votes_text}")

        st.markdown(f"📅 **Ano:** {details.get('year', 'Não informado')}")

        st.markdown(f"🎭 **Gêneros:** {details.get('genres') or 'Não informado'}")

        runtime = details.get("runtime")
        runtime_text = f"{runtime} min" if runtime else "Não informado"
        st.markdown(f"⏱️ **Duração:** {runtime_text}")

        lang = details.get("language")
        lang_text = lang.upper() if lang else "Não informado"
        st.markdown(f"🌎 **Idioma:** {lang_text}")

        st.markdown(
            f"🔥 **Popularidade:** {details.get('popularity', 0.0)}"
        )

    st.divider()

    st.markdown("### Sinopse")

    st.write(details.get("overview") or "Sinopse não disponível.")

    if details.get("homepage"):

        st.link_button(
            "🌐 Site Oficial",
            details["homepage"],
            use_container_width=True
        )

    st.link_button(
        "🎬 Abrir no TMDB",
        details.get("tmdb_url", "https://www.themoviedb.org"),
        use_container_width=True
    )