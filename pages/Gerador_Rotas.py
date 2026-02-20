import streamlit as st
import os

# Configuração da página
st.set_page_config(
    page_title="Gerador de Rotas - Download e Acesso",
    page_icon="🗺️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS para manter o estilo premium
st.markdown("""
<style>
    /* Fundo e fontes */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Container Principal */
    .main-container {
        max_width: 800px;
        margin: 0 auto;
        padding: 2rem;
        background-color: white;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .header-icon {
        font-size: 5rem;
        margin-bottom: 1rem;
    }
    
    h1 {
        color: #1a1a1a;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-bottom: 3rem;
    }
    
    /* Steps */
    .step-card {
        background-color: #f8f9fa;
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        text-align: left;
        border-left: 5px solid #4b6cb7;
        transition: transform 0.2s;
    }
    
    .step-card:hover {
        transform: translateX(5px);
    }
    
    .step-title {
        font-weight: 700;
        color: #2c3e50;
        font-size: 1.1rem;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .step-desc {
        color: #666;
        font-size: 0.95rem;
    }
    
    /* Botões */
    .stButton button {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(75, 108, 183, 0.3);
    }
    
    .secondary-btn button {
        background: transparent !important;
        border: 2px solid #4b6cb7 !important;
        color: #4b6cb7 !important;
        background-image: none !important;
    }
    
    .secondary-btn button:hover {
        background: #4b6cb7 !important;
        color: white !important;
    }

</style>
""", unsafe_allow_html=True)

# Layout Principal
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown("""
        <div class="main-container">
            <div class="header-icon">🗺️</div>
            <h1>Gerador de Rotas</h1>
            <p class="subtitle">Otimização de Logística e Entregas</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Siga os passos abaixo:")
    
    # Passo 1: Download
    st.markdown("""
    <div class="step-card">
        <div class="step-title">
            <span>1️⃣</span> Baixar Modelo de Roteiro
        </div>
        <div class="step-desc">
            Faça o download da planilha modelo para preencher com os dados dos clientes e endereços.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Caminho do arquivo
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    file_path = os.path.join(project_root, "modelo_importacao_roteiro.xlsx")
    
    try:
        with open(file_path, "rb") as file:
            st.download_button(
                label="📥 Baixar Planilha Modelo",
                data=file,
                file_name="modelo_importacao_roteiro.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
    except FileNotFoundError:
        st.error(f"Arquivo modelo não encontrado em: {file_path}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Passo 2: Acessar Site
    st.markdown("""
    <div class="step-card">
        <div class="step-title">
            <span>2️⃣</span> Acessar Gerador de Rotas
        </div>
        <div class="step-desc">
            Acesse a ferramenta de mapas para importar seu arquivo e gerar as rotas.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button(
        "🚀 Ir para Gerador de Rotas", 
        "https://mapsbiz02-z2nfvymzddnmabtzdskkmm.streamlit.app/",
        use_container_width=True
    )

    st.markdown("<br><hr>", unsafe_allow_html=True)

    # Botão Voltar
    if st.button("⬅️ Voltar para Home"):
        st.switch_page("pages/portal.py")
