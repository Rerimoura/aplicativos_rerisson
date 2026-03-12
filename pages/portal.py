import streamlit as st

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
        padding: 0.6rem 0;
        margin-bottom: 0.8rem;
    }
    .main-header h1 {
        color: #1a1a1a;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .main-header p {
        color: #4a4a4a;
        font-size: 0.95rem;
        font-weight: 400;
    }
    .main-header .subtitle {
        color: #4b6cb7;
        font-weight: 600;
        font-size: 1.1rem;
        margin-top: -6px;
    }
    
    /* Cards dos Apps */
    .app-card {
        background-color: white;
        border-radius: 12px;
        padding: 0.8rem 1rem;
        box-shadow: 0 6px 18px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
        height: 100%;
        border: 1px solid rgba(255,255,255,0.5);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .app-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 12px 24px rgba(0,0,0,0.15);
    }
    
    .app-icon {
        font-size: 2rem;
        margin-bottom: 0.3rem;
    }
    
    .app-title {
        font-size: 1rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.2rem;
        min-height: 2.2rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .app-desc {
        color: #7f8c8d;
        font-size: 0.78rem;
        margin-bottom: 0.6rem;
        line-height: 1.4;
        flex-grow: 1;
    }
    
    /* Botão */
    .stButton button {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%);
        color: white;
        border: none;
        padding: 0.35rem 1rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.8rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(75, 108, 183, 0.4);
    }
    
    /* st.link_button e st.page_link — mesma aparência: azul escuro + branco */
    [data-testid="stLinkButton"] a,
    [data-testid="stLinkButton"] a:visited,
    [data-testid="stPageLink"] a,
    [data-testid="stPageLink"] a:visited {
        background: linear-gradient(90deg, #4b6cb7 0%, #182848 100%) !important;
        color: white !important;
        border: none !important;
        padding: 0.35rem 1rem;
        border-radius: 50px;
        font-weight: 600;
        font-size: 0.8rem;
        text-decoration: none !important;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 100%;
        transition: all 0.3s ease;
        box-sizing: border-box;
    }
    [data-testid="stLinkButton"] a *,
    [data-testid="stPageLink"] a * {
        color: white !important;
    }
    [data-testid="stLinkButton"] a:hover,
    [data-testid="stPageLink"] a:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(75, 108, 183, 0.4);
        color: white !important;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 0.8rem;
        color: #666;
        font-size: 0.75rem;
        margin-top: 0.5rem;
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

# Container dos Apps — linha 1
col1, col2, col3 = st.columns(3)

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
    st.page_link("pages/Gerador_Rotas.py", label="Acessar App", use_container_width=True)

# Espaçamento entre linhas
st.markdown("<br style='line-height:0.3'>", unsafe_allow_html=True)

# Segunda linha de apps
col4, col5, col6 = st.columns(3)

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
    st.page_link("pages/Biz_Net.py", label="Acessar App", use_container_width=True)

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

# Espaçamento entre linhas
st.markdown("<br style='line-height:0.3'>", unsafe_allow_html=True)

# Terceira linha de apps
col7, col8, col9 = st.columns(3)

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

# App 8: Simulador Poliequipes
with col8:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">📈</div>
            <div class="app-title">Simulador Poliequipes</div>
            <div class="app-desc">
                Simulação de investimentos para as equipes Polibras.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Acessar App", "https://simuladorpolibras.streamlit.app/", use_container_width=True)

# App 9: Simulador Compra Agora
with col9:
    st.markdown("""
    <div class="app-card">
        <div>
            <div class="app-icon">🛒</div>
            <div class="app-title">Simulador Compra Agora</div>
            <div class="app-desc">
                Simulador para análise e planejamento de compras imediatas.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Acessar App", "https://simuladorcompraagora.streamlit.app/", use_container_width=True)

# Rodapé
st.markdown("""
<div class="footer">
    <p>Desenvolvido por Rerisson Moura Diniz</p>
</div>
""", unsafe_allow_html=True)
