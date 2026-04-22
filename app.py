import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (Identidade Visual de Luxo)
st.set_page_config(
    page_title="Digital Solutions & Consulting IT | Transformação Digital de Elite",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização CSS para um visual de "5 Milhões de Dólares"
st.markdown("""
    <style>
    /* Importar fonte moderna */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .main { background-color: #f8fafc; }
    
    /* Títulos e Headers */
    .stTitle { 
        font-size: 52px !important; 
        color: #1e3a8a; 
        font-weight: 800; 
        letter-spacing: -1px;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 24px;
        color: #475569;
        margin-bottom: 40px;
    }
    
    /* Cartões de Serviço e Secções */
    .section-header { 
        color: #1e40af; 
        border-left: 5px solid #3b82f6; 
        padding-left: 15px; 
        margin-top: 40px; 
        font-weight: 700; 
        font-size: 28px;
    }
    
    .service-card { 
        background-color: white; 
        padding: 30px; 
        border-radius: 20px; 
        box-shadow: 0 10px 25px rgba(0,0,0,0.05); 
        transition: transform 0.3s ease;
        border: 1px solid #e2e8f0;
        height: 100%;
    }
    .service-card:hover {
        transform: translateY(-5px);
        border-color: #3b82f6;
    }
    
    /* Lab Box */
    .lab-box {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 20px;
    }
    
    /* Sidebar */
    .sidebar-text { font-size: 14px; color: #64748b; }
    
    /* Footer */
    .footer { text-align: center; padding: 20px; color: #94a3b8; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

# 2. GESTÃO DE NAVEGAÇÃO
if 'menu_option' not in st.session_state:
    st.session_state.menu_option = "🏠 Início"

# 3. BARRA LATERAL (BRANDING & CONTACTOS)
with st.sidebar:
    try:
        st.image("IMG_6163.jpeg", use_container_width=True)
    except:
        st.markdown(f"### **Digital Solutions & Consulting IT**")
    
    st.markdown("---")
    menu_list = ["🏠 Início", "🎯 Estratégia", "💰 Catálogo", "🧪 Laboratório"]
    
    # Navegação Dinâmica
    current_index = menu_list.index(st.session_state.menu_option)
    menu = st.radio("Navegação Principal:", menu_list, index=current_index)
    st.session_state.menu_option = menu

    st.markdown("---")
    st.markdown("### 💡 **Contacto Direto**")
    st.write("📩 [ds.consulting.it@outlook.com](mailto:ds.consulting.it@outlook.com)")
    st.markdown("[🔗 LinkedIn Institucional](https://www.linkedin.com/company/digital-solutions-consulting-it/)")
    
    st.caption("© 2026 Digital Solutions & Consulting IT")

# --- PÁGINA 1: INÍCIO E MISSÃO ---
if st.session_state.menu_option == "🏠 Início":
    st.markdown('<h1 class="stTitle">A tecnologia a trabalhar para o seu negócio 🚀</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Na <b>Digital Solutions & Consulting IT</b>, transformamos ferramentas comuns em motores de eficiência. Devolvemos-lhe o tempo que hoje perde com processos manuais.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="section-header">Nossa Missão 🛡️</h2>', unsafe_allow_html=True)
        st.markdown("""
        A nossa missão é garantir que a sua empresa não fique para trás na era digital. 
        Acreditamos que a automação e a Inteligência Artificial devem ser acessíveis, permitindo que o seu investimento seja aplicado no desenvolvimento de soluções práticas que geram retorno real, sem a necessidade de licenças de software dispendiosas. 💎
        """)
        
        st.markdown('<h2 class="section-header">Visão de Futuro 🔮</h2>', unsafe_allow_html=True)
        st.markdown("""
        Ser o parceiro estratégico que simplifica a tecnologia. Queremos que os nossos clientes utilizem a IA e a automação como ferramentas naturais do dia a dia, integradas perfeitamente nas suas operações para potenciar o crescimento.
        """)
    
    with col2:
        st.info("📊 **Porquê nós?**\n\n- Foco em Micro e Pequenas Empresas\n- Uso de Ferramentas que já possui\n- Redução de Erros Humanos\n- ROI em Tempo Real")
        st.success("✨ **Especialistas em:**\n- Python & Automação\n- Power Automate\n- Agentes IA Customizados")

# --- PÁGINA 2: ESTRATÉGIA ---
elif st.session_state.menu_option == "🎯 Estratégia":
    st.markdown('<h1 class="stTitle">O Método em 4 Fases ⚡</h1>', unsafe_allow_html=True)
    st.write("Uma abordagem estruturada para garantir resultados sólidos e escaláveis.")

    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("### 1️⃣ Auditoria e Diagnóstico")
        st.write("Não implementamos soluções sem primeiro compreender o seu negócio. Analisamos o seu fluxo de trabalho atual para identificar onde a tecnologia e a IA podem eliminar tarefas repetitivas e otimizar o tempo da sua equipa.")
        
        st.markdown("### 2️⃣ Arquitetura Digital")
        st.write("Organizamos a sua infraestrutura utilizando o que já possui (ex: **OneDrive, SharePoint, Google Drive**) e exploramos outras ferramentas gratuitas para alavancar o seu negócio com segurança e ordem.")

    with col_b:
        st.markdown("### 3️⃣ Desenvolvimento & Implementação")
        st.write("Damos vida ao projeto com scripts, automações e websites. Utilizamos **Python**, **Power Automate Desktop** e IA de vanguarda para criar soluções que vão desde a triagem de emails até à gestão de bases de dados.")
        
        st.markdown("### 4️⃣ Estabilidade e Formação")
        st.write("Trabalhamos consigo para garantir que tudo funciona corretamente. Fornecemos formação e consultoria contínua para que a tecnologia seja o suporte sólido de todas as boas práticas da sua empresa.")

# --- PÁGINA 3: CATÁLOGO ---
elif st.session_state.menu_option == "💰 Catálogo":
    st.markdown('<h1 class="stTitle">Catálogo de Investimento 💰</h1>', unsafe_allow_html=True)
    st.write("Soluções de elite com preços transparentes e foco no retorno.")

    servicos = [
        {"T": "Website Corporativo + Agente IA", "I": "Desde 350€", "D": "Um site moderno que funciona como o seu cartão de visita digital e o desenvolvimento de um agente de IA sobre o seu negócio para interagir com os seus visitantes. 🌐"},
        {"T": "Eficiência Cloud & Office 365", "I": "Desde 300€", "D": "Configuração profissional de permissões e fluxos no Office 365 ou Google Workspace. Acabe com o caos de ficheiros e emails perdidos. ☁️"},
        {"T": "Agentes IA & Scripts de Dados", "I": "Desde 300€", "D": "Soluções personalizadas para análise de relatórios e grandes volumes de dados, transformando informação bruta em decisões estratégicas. 🧠"},
        {"T": "Automação (Python/Power Automate)", "I": "Desde 350€", "D": "Criação de robôs e scripts que executam tarefas manuais, integram sistemas e aceleram a operação do seu negócio. 🤖"},
        {"T": "Consultoria e Workshops IA", "I": "Desde 200€", "D": "Formação prática para a sua equipa aprender a utilizar a IA como ferramenta de produtividade diária. 🎓"},
        {"T": "Suporte Operacional Mensal", "I": "Desde 50€/mês", "D": "Acesso prioritário para ajustes, correções e consultoria contínua para manter a sua empresa na vanguarda tecnológica. 🛠️"}
    ]

    cols = st.columns(2)
    for idx, s in enumerate(servicos):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="service-card">
                <h3 style="color:#1e40af;">{s['T']}</h3>
                <p><b>Investimento:</b> <span style="color:#2563eb; font-size:1.1em;">{s['I']}</span></p>
                <p style="color:#475569;">{s['D']}</p>
            </div><br>
            """, unsafe_allow_html=True)

# --- PÁGINA 4: LABORATÓRIO ---
elif st.session_state.menu_option == "🧪 Laboratório":
    st.markdown('<h1 class="stTitle">Laboratório de Inovação 🧪</h1>', unsafe_allow_html=True)
    st.markdown("### Como Usar os Nossos Agentes Gratuitos 🤖")
    st.write("Disponibilizamos vários Agentes de IA independentes que funcionam como os nossos embaixadores de eficiência.")

    st.markdown(f"""
    <div class="lab-box">
        <h4>✨ Consultor IA 24/7</h4>
        <p>Temos o prazer de apresentar o nosso novo Consultor de Inteligência Artificial – disponível para si agora!</p>
        <a href="https://agente-ia-digital-solutions-consulting-it.streamlit.app/" style="color:white; font-weight:bold; text-decoration:underline;">EXPERIMENTE AQUI (GRÁTIS)</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("#### 📧 Agentes de Processamento por E-mail")
    st.info("Basta enviar um e-mail para **ds.consulting.it.geral@gmail.com**. O nosso motor processa os pedidos em ciclos programados e redireciona a resposta analisada para si.")

    with st.expander("📊 [ai dados] – O seu Excel com Inteligência"):
        st.write("""
        Envie um ficheiro Excel ou CSV. Inclua no assunto a tag **[ai dados]**.
        **O que recebe:** Um relatório PDF profissional com análise estatística, regressões e gráficos dinâmicos para apoiar a sua estratégia.
        """)

    with st.expander("💡 [AI Solutions] – Consultoria Estratégica"):
        st.write("""
        Descreva um problema no corpo do e-mail. Inclua no assunto a tag **[AI Solutions]**.
        **O que recebe:** Um relatório com pontos de melhoria, soluções de baixo custo e formas de impulsionar o seu negócio via IA.
        """)

    with st.expander("📑 [AI Reports] – Assistente de Documentos"):
        st.write("""
        Envie PDF, Word ou Texto com uma dúvida. Inclua no assunto a tag **[AI Reports]**.
        **O que recebe:** Um relatório detalhado com a filtragem inteligente da informação, poupando horas de leitura.
        """)

st.markdown("---")
st.markdown('<div class="footer">Digital Solutions & Consulting IT | Inteligência em Cada Processo | 2026</div>', unsafe_allow_html=True)
