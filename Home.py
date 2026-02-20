import streamlit as st

# Registro das páginas do app usando a nova API st.navigation
pg = st.navigation(
    [
        st.Page("pages/portal.py", title="Portal", default=True, icon="�"),
        st.Page("pages/Biz_Net.py", title="Biz Net", icon="🌐"),
        st.Page("pages/Gerador_Rotas.py", title="Gerador de Rotas", icon="🗺️"),
    ],
    position="hidden"  # Oculta a barra lateral de navegação automática
)

pg.run()
