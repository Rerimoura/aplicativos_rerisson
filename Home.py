import streamlit as st

# Registro das páginas do app usando a nova API st.navigation
pg = st.navigation(
    [
        st.Page("pages/portal.py", title="Portal", default=True),
        st.Page("pages/Biz_Net.py", title="Biz Net"),
        st.Page("pages/Gerador_Rotas.py", title="Gerador de Rotas"),
    ],
    position="hidden"  # Oculta a barra lateral de navegação automática
)

pg.run()
