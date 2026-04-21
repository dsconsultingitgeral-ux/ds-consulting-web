import streamlit as st
import pandas as pd
from groq import Groq

# 1. CONFIGURAÇÃO DA PÁGINA (Identidade Visual)
st.set_page_config(
    page_title="DS Consulting IT | Soluções Digitais Estratégicas",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuração Segura da API GROQ
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    api_key = "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"

client = Groq(api_key=api_key)

# Estilização CSS Avançada
st.markdown("""
    <style>
    .main { background-color: #fcfcfc; }
    .stTitle { font-size: 45px !important; color: #1a365d; font-weight: 800; }
    .section-header { color: #2c5282; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; margin-top: 30px; font-weight: 700; }
    .service-card { 
        background-color: white; 
        padding: 25px; 
        border-radius: 12px; 
        border-left: 6px solid #3182ce; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.05); 
        margin-bottom: 25px;
    }
    .mission-box {
        background-color: #ebf8ff;
        padding: 20px;
        border-radius: 10px;
        color: #2a4365;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. GESTÃO DE ESTADO
if 'menu_option' not in st.session_state:
    st.session_state.menu_option = "🏠 Início e Missão"

# 3. BARRA LATERAL (MENU PROFISSIONAL)
with st.sidebar:
    try:
        st.image("IMG_6163.jpeg", use_container_width=True)
    except:
        st.title("DS Consulting IT")
    
    st.markdown("---")
    menu_list = ["🏠 Início e Missão", "🎯 Estratégia Detalhada", "💰 Catálogo de Serviços", "🧪 Laboratório DS", "🤖 Agente de Consultoria"]
    
    # Navegação robusta
    current_index = menu_list.index(st.session_state.menu_option)
    menu = st.radio("Selecione a Área:", menu_list, index=current_index)
    st.session_state.menu_option = menu

    st.markdown("---")
    st.info("💡 **Contacto Direto:**\n\nds.consulting.it@outlook.com")
    st.markdown("[🔗 Perfil Institucional LinkedIn](https://www.linkedin.com/company/digital-solutions-consulting-it/)")

# --- PÁGINA 1: INÍCIO E MISSÃO ---
if st.session_state.menu_option == "🏠 Início e Missão":
    st.title("Lideramos a sua Transição para a Eficiência Digital")
    
    st.markdown('<p style="font-size:20px;">A DS Consulting IT não é apenas uma empresa de tecnologia; somos o seu parceiro estratégico na eliminação de desperdício operacional.</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown('<h2 class="section-header">Nossa Missão</h2>', unsafe_allow_html=True)
        st.markdown("""
        No cenário atual, as PMEs enfrentam o desafio de competir com gigantes tecnológicos. A nossa missão é **democratizar o acesso à automação de alto nível**. 
        Acreditamos que nenhuma empresa deve perder tempo com tarefas manuais que um algoritmo pode resolver em segundos. 
        
        **O nosso compromisso é simples:** Entregar soluções que se pagam a si mesmas através da poupança de tempo e redução de erros humanos.
        """)
        
        st.markdown('<h2 class="section-header">Visão de Futuro</h2>', unsafe_allow_html=True)
        st.write("Ser a consultora de referência em Portugal para empresas que procuram modernização sem custos exorbitantes de licenciamento, utilizando o poder do Open Source e das infraestruturas Cloud já existentes.")
    
    with col2:
        st.markdown('<div class="mission-box">"A nossa métrica de sucesso não é o número de sistemas instalados, mas sim as horas de liberdade que devolvemos aos nossos clientes."</div>', unsafe_allow_html=True)
        st.write("")
        st.success("✅ +40% de Eficiência Operacional\n\n✅ Integração Nativa Office/Google\n\n✅ Redução de Custos de Licenciamento")

# --- PÁGINA 2: ESTRATÉGIA ---
elif st.session_state.menu_option == "🎯 Estratégia Detalhada":
    st.title("🎯 Estratégia: O Método DS de 4 Pilares")
    st.write("A nossa abordagem é metódica e desenhada para garantir que a tecnologia se adapta ao seu negócio, e não o contrário.")
    
    st.markdown('<h2 class="section-header">1. Diagnóstico e Auditoria de Processos</h2>', unsafe_allow_html=True)
    st.write("Analisamos o fluxo de trabalho atual da sua equipa. Identificamos onde estão os 'gargalos' — aquelas tarefas repetitivas, manuais e propensas a erros que consomem o tempo produtivo.")
    
    st.markdown('<h2 class="section-header">2. Setup de Ecossistema de Base</h2>', unsafe_allow_html=True)
    st.write("Antes de automatizar, é preciso organizar. Configuramos ou otimizamos a sua infraestrutura Cloud (OneDrive, Google Workspace ou SharePoint) para garantir que os dados fluem de forma segura e organizada.")
    
    st.markdown('<h2 class="section-header">3. Implementação de Automação e IA</h2>', unsafe_allow_html=True)
    st.write("Aqui é onde a magia acontece. Desenvolvemos 'Agentes' e 'Robôs' (em Python ou Power Automate) que executam tarefas complexas, desde a leitura de faturas até ao atendimento automático de clientes 24/7.")
    
    st.markdown('<h2 class="section-header">4. Suporte e Melhoria Contínua</h2>', unsafe_allow_html=True)
    st.write("A tecnologia evolui. O nosso suporte garante que as automações continuam a funcionar perfeitamente e são atualizadas conforme o seu negócio cresce.")

# --- PÁGINA 3: CATÁLOGO ---
elif st.session_state.menu_option == "💰 Catálogo de Serviços":
    st.title("💰 Soluções e Investimento Estratégico")
    st.write("Investir em tecnologia é investir em escala. Conheça as nossas soluções base:")
    
    servicos = [
        {"S": "Website Corporativo + Agente IA Integrado", "P": "Desde 350€", "D": "Um site moderno que não apenas apresenta a empresa, mas atende clientes e tira dúvidas em tempo real, capturando leads enquanto você dorme."},
        {"S": "Reorganização Estrutural Office 365 / Google", "P": "Desde 300€", "D": "Configuração completa de permissões, segurança e fluxos de ficheiros. Acabe com o caos de ficheiros duplicados e anexos de email."},
        {"S": "Desenvolvimento de Robôs de Automação", "P": "Desde 350€", "D": "Scripts customizados que ligam diferentes softwares, processam dados em massa e geram relatórios automáticos sem intervenção humana."},
        {"S": "Consultoria e Workshops de IA", "P": "Desde 200€", "D": "Formação prática para a sua equipa aprender a usar ferramentas de IA generativa para duplicar a sua produtividade diária."},
        {"S": "Suporte Operacional Mensal", "P": "Desde 50€/mês", "D": "Acesso prioritário para ajustes, correções e consultoria contínua para manter a sua empresa na vanguarda."}
    ]
    
    for s in servicos:
        st.markdown(f'''
        <div class="service-card">
            <h3 style="margin-top:0; color:#1a365d;">{s['S']}</h3>
            <p><strong>Investimento:</strong> <span style="color:#2b6cb0; font-size:1.2em;">{s['P']}</span></p>
            <p style="color:#4a5568;">{s['D']}</p>
        </div>
        ''', unsafe_allow_html=True)

# --- PÁGINA 4: LABORATÓRIO ---
elif st.session_state.menu_option == "🧪 Laboratório DS":
    st.title("🧪 Laboratório de Inovação")
    st.write("Quer testar o poder das nossas automações? Envie um e-mail para **ds.consulting.it.geral@gmail.com** com uma das seguintes etiquetas no assunto:")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.info("### [ai dados]\nEnvie uma tabela Excel e o nosso robô devolverá uma análise estatística completa em segundos.")
    with c2:
        st.success("### [AI Reports]\nEnvie notas soltas e receba um relatório profissional estruturado em formato PDF.")
    with c3:
        st.warning("### [ai business]\nDescreva um problema do seu negócio e receba uma sugestão de arquitetura tecnológica.")

# --- PÁGINA 5: AGENTE IA (CORRIGIDO) ---
elif st.session_state.menu_option == "🤖 Agente de Consultoria":
    st.title("🤖 Consultor Estratégico Digital")
    st.write("Este agente foi treinado com o conhecimento profundo da DS Consulting IT. Pergunte sobre serviços, preços ou como podemos ajudar a sua empresa.")

    system_content = """És o Consultor Sénior da DS Consulting IT.
    Teu tom é altamente profissional, empático e focado em soluções.
    Missão: Mostrar que a automação liberta as pessoas para tarefas criativas.
    Preços: Website+IA (350€), Robôs (350€), Setup Office (300€), Suporte (50€).
    Estratégia: 4 passos (Diagnóstico, Setup, Automação, Suporte).
    Responde sempre em Português de Portugal. Se não souberes algo, pede para enviarem email para ds.consulting.it@outlook.com."""

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibe histórico (sem o system prompt)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Em que posso ajudar o seu negócio hoje?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            try:
                # Construção correta das mensagens para a Groq
                full_context = [{"role": "system", "content": system_content}] + st.session_state.messages
                
                chat_completion = client.chat.completions.create(
                    messages=full_context,
                    model="llama3-8b-8192",
                    temperature=0.7
                )
                response = chat_completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"Erro de conexão. Por favor, verifique a sua chave API nos Secrets.")

st.markdown("---")
st.caption("© 2026 Digital Solutions & Consulting IT - Todos os direitos reservados.")
