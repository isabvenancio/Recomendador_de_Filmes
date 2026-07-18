import streamlit as st

def hero():
    st.markdown(
        """<section class="hero">
<div class="hero-badge">🤖 Powered by Machine Learning</div>
<div class="hero-title">Descubra seu próximo filme favorito.</div>
<p class="hero-description">Escolha um filme que você gosta e nosso algoritmo utiliza Inteligência Artificial, Machine Learning e Similaridade de Cosseno para encontrar recomendações personalizadas.</p>
</section>""",
        unsafe_allow_html=True
    )