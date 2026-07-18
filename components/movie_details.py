import streamlit as st


def movie_details(details):

    if details is None:
        return

    with st.expander("🎬 Mais detalhes"):

        col1, col2 = st.columns([1, 2])

        with col1:

            if details["poster"]:
                st.image(
                    details["poster"],
                    use_container_width=True
                )

        with col2:

            st.markdown(f"## {details['title']}")

            st.markdown(f"⭐ **Nota:** {details['rating']}")

            st.markdown(f"👥 **Votos:** {details['votes']:,}")

            st.markdown(f"📅 **Ano:** {details['year']}")

            st.markdown(f"🎭 **Gêneros:** {details['genres']}")

            st.markdown(f"⏱️ **Duração:** {details['runtime']} min")

            st.markdown(f"🌎 **Idioma:** {details['language'].upper()}")

            st.markdown(
                f"🔥 **Popularidade:** {details['popularity']}"
            )

        st.divider()

        st.markdown("### Sinopse")

        st.write(details["overview"])

        if details["homepage"]:

            st.link_button(
                "🌐 Site Oficial",
                details["homepage"],
                use_container_width=True
            )

        st.link_button(
            "🎬 Abrir no TMDB",
            details["tmdb_url"],
            use_container_width=True
        )