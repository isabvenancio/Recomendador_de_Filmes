import streamlit as st

def navbar():
    st.markdown(
        """<div class="navbar">
<div class="navbar-logo">🎬 MovieMatch AI</div>
<div class="navbar-links">
<a href="#inicio">Home</a>
<a href="#sobre">Sobre</a>
<a href="https://github.com/isabvenancio" target="_blank">GitHub</a>
<a href="https://linkedin.com/in/isabella-barela-venâncio" target="_blank">LinkedIn</a>
</div>
</div>""",
        unsafe_allow_html=True
    )