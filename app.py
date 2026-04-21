import streamlit as st
import pandas as pd

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Digital Solutions & Consulting IT",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Customizada (CSS) para um ar mais profissional
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #1f77b4;
        color: white;
    }
    .service-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. BARRA LATERAL (MENU)
with st.sidebar:
    st.image("IMG_6163.jpeg", width=200)
    st.title("DS Consulting IT")
    st.markdown("---")
    menu = st.radio(
        "Navegação",
        ["🏠 Início", "🎯 Estratégia", "💰 Catálogo de Serviços", "🧪 Laboratório DS", "🤖 Agente IA 24/7"]
    )
    st.markdown("---")
    st.markdown("📩 **ds.consulting.it@outlook.com**")
    st.markdown("[🔗 LinkedIn Oficial](https://www.linkedin.com/company/digital-solutions-consulting-it/)")

# --- PÁGINA 1: INÍCIO ---
if menu == "🏠 Início":
    st.title("A tecnologia a trabalhar para si. 🚀")
    st.subheader("Transformamos o caos operacional em eficiência digital para PMEs.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Porquê a DS Consulting IT?
        Muitas empresas perdem horas em tarefas repetitivas que poderiam ser automatizadas. 
        Nós não instalamos apenas software; **devolvemos-lhe o tempo.**
        
        Utilizamos tecnologias de ponta (**Google, Microsoft e Open Source**) para criar soluções 
        sob medida que se adaptam ao seu orçamento.
        """)
        if st.button("Ver a Nossa Estratégia"):
            st.balloons()
    
    with col2:
        st.info("💡 **Diferencial:** Focamos em ferramentas gratuitas e licenciamento económico para maximizar o seu ROI.")

# --- PÁGINA 2: ESTRATÉGIA ---
elif menu == "🎯 Estratégia":
    st.title("🎯 Nossa Estratégia e Método")
    st.markdown("### Arquitetura de Custo Zero & Eficiência Máxima")
    
    st.write("""
    A nossa estratégia baseia-se em aproveitar o que de melhor os gigantes tecnológicos oferecem, 
    ajustando a infraestrutura ao tamanho real do seu negócio.
    """)
    
    st.divider()
    st.subheader("🚀 Roteiro de Transformação em 4 Passos")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("#### 1. Diagnóstico\nLevantamento de processos e identificação de gargalos.")
    with c2:
        st.markdown("#### 2. Setup Base\nOrganização do ecossistema digital (Office 365/Google).")
    with c3:
        st.markdown("#### 3. Automação & IA\nCriação de robôs e agentes de IA personalizados.")
    with c4:
        st.markdown("#### 4. Suporte\nManutenção contínua e evolução tecnológica.")

# --- PÁGINA 3: CATÁLOGO ---
elif menu == "💰 Catálogo de Serviços":
    st.title("💰 Soluções e Investimento")
    st.write("Projetos modulares desenhados para micro e pequenas empresas.")
    
    # Serviços em formato de tabela e cards
    servicos = [
        {"Serviço": "Website Profissional + Agente IA", "Preço": "Desde 350€", "Nota": "Inclui atendimento automático 24/7."},
        {"Serviço": "Reorganização Office 365 Online", "Preço": "Desde 300€", "Nota": "Setup de Excel, OneDrive, Teams e Outlook."},
        {"Serviço": "O Robô (Automação Customizada)", "Preço": "Desde 350€", "Nota": "Python / Power Automate / SQL."},
        {"Serviço": "Relatórios e Análise Preditiva", "Preço": "Desde 250€", "Nota": "PDFs inteligentes com visão de futuro."},
        {"Serviço": "Workshop de IA para Equipas", "Preço": "Desde 200€", "Nota": "Formação prática de produtividade."},
        {"Serviço": "Agente de IA Solo", "Preço": "Desde 200€", "Nota": "Integração em sistemas existentes."},
        {"Serviço": "Suporte e Apoio Mensal", "Preço": "Desde 50€/mês", "Nota": "Paz de espírito e sistemas sempre online."}
    ]
    
    for s in servicos:
        st.markdown(f"""
        <div class="service-card">
            <h4 style="margin:0;">{s['Serviço']} — <span style="color:#1f77b4;">{s['Preço']}</span></h4>
            <p style="margin:5px 0 0 0; color:#666;">{s['Nota']}</p>
        </div>
        """, unsafe_allow_html=True)

# --- PÁGINA 4: LABORATÓRIO (TESTES) ---
elif menu == "🧪 Laboratório DS":
    st.title("🧪 Laboratório de Demonstração")
    st.write("Envie um e-mail para **ds.consulting.it.geral@gmail.com** com as tags abaixo:")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.success("### [ai dados]")
        st.write("Anexe um Excel e receba-o com análise estatística completa.")
    with col2:
        st.success("### [AI Reports]")
        st.write("Envie os seus dados e receba um relatório PDF preditivo.")
    with col3:
        st.success("### [ai business]")
        st.write("Descreva uma tarefa e receba um plano de alavancagem com IA.")

# --- PÁGINA 5: AGENTE IA ---
elif menu == "🤖 Agente IA 24/7":
    st.title("🤖 Consultor Estratégico DS")
    st.write("Fale em tempo real com o nosso agente sobre o seu negócio.")
    
    # Integração simples de Chat (Mantenha aqui a sua lógica de API se tiver)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Como posso ajudar a sua empresa hoje?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            # Aqui ligaria à sua lógica de IA. Exemplo de resposta:
            response = "Sou o assistente da DS Consulting. Posso ajudar a explicar o nosso roteiro de 4 passos ou os serviços a partir de 200€."
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# RODAPÉ
st.markdown("---")
st.caption("© 2026 Digital Solutions & Consulting IT | Inovação através da Eficiência.")
