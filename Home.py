import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(
    page_title="Portal de Aplicativos - Rede Biz",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS para estilo premium
st.markdown("""
<style>
    /* Fundo e fontes */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Cabeçalho */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: #1a1a1a;
        font-size: 3.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .main-header p {
        color: #4a4a4a;
        font-size: 1.2rem;
        font-weight: 400;
    }
    .main-header .subtitle {
        color: #4b6cb7;
        font-weight: 600;
        font-size: 1.5rem;
        margin-top: -10px;
    }
    
    /* Cards dos Apps */
    .app-card {
        background-color: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        height: 100%;
        border: 1px solid rgba(255,255,255,0.5);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .app-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    }
    
    .app-icon {
        font-size: 4rem;
        margin-bottom: 1rem;
    }
    
    .app-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.5rem;
        min-height: 3.6rem; /* Altura fixa para alinhamento */
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .app-desc {
        color: #7f8c8d;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
        line-height: 1.5;
        flex-grow: 1;
    }
    
    /* Botão */
    .stButton button {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 50px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(75, 108, 183, 0.4);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        font-size: 0.8rem;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Cabeçalho Principal
st.markdown("""
<div class="main-header">
    <h1>🚀 Portal de Aplicativos</h1>
    <div class="subtitle">Rede Biz</div>
    <p>Central de ferramentas e dashboards analíticos</p>
</div>
""", unsafe_allow_html=True)

# Container dos Apps
col1, col2, col3, col4 = st.columns(4)

# App 1: Venn Analysis
with col1:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">📊</div>
            <div class="app-title">Análise de Venda Cruzada</div>
            <div class="app-desc">
                Ferramenta para análise de vendas cruzadas entre produtos, com Diagramas de Venn e tabelas detalhadas.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Acessar App", "https://vennbiz.streamlit.app/", use_container_width=True)

# App 2: Conversor PDF
with col2:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">📄</div>
            <div class="app-title">Conversor de Pedidos</div>
            <div class="app-desc">
                Converta pedidos de PDF para Excel de forma rápida e automatizada.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Acessar App", "https://converter-pdf-excel-biz.streamlit.app/", use_container_width=True)

# App 3: Gerador de Rotas
with col3:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">🗺️</div>
            <div class="app-title">Gerador de Rotas</div>
            <div class="app-desc">
                Otimização automática de rotas para logística e entregas.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar App", key="btn_rotas", use_container_width=True):
        st.switch_page("pages/Gerador_Rotas.py")

# App 4: Biz Net
with col4:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">🌐</div>
            <div class="app-title">Biz Net</div>
            <div class="app-desc">
                Ferramenta para transmissão de pedidos com importação via Excel.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Acessar App", key="btn_biznet", use_container_width=True):
        st.switch_page("pages/Biz_Net.py")

# Espaçamento entre linhas
st.markdown("<br>", unsafe_allow_html=True)

# Segunda linha de apps
col5, col6, col7, col8 = st.columns(4)

# App 5: Clientes sem Compra
with col5:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">👥</div>
            <div class="app-title">Clientes sem Compra Biz</div>
            <div class="app-desc">
                Identificação e análise da base de clientes sem compras em períodos específicos.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Acessar App", "https://clientessemcomprasigma.streamlit.app/", use_container_width=True)

# App 6: Consulta CNPJ
with col6:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">🏢</div>
            <div class="app-title">Consulta CNPJ</div>
            <div class="app-desc">
                Consulta situação cadastral e endereço de CNPJs na base da Receita.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Acessar App", "https://cnpjsmgconsulta.streamlit.app/", use_container_width=True)

# App 7: Simulador Nivea
with col7:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">💰</div>
            <div class="app-title">Simulador Nivea</div>
            <div class="app-desc">
                Crie um simulador para cálculo de investimentos nas Top Redes.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.link_button("Acessar App", "https://simuladornivea.streamlit.app/", use_container_width=True)

# Rodapé
st.markdown("""
<div class="footer">
    <p>Desenvolvido por Rerisson Moura Diniz</p>
</div>
""", unsafe_allow_html=True)
