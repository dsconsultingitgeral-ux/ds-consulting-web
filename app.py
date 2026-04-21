import streamlit as st
import pandas as pd
from groq import Groq

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Digital Solutions & Consulting IT",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Configuração da API GROQ (FORMA SEGURA)
# Primeiro tentamos ler dos Secrets do Streamlit, se não existir (local), usamos a tua key direta
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    api_key = "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"

client = Groq(api_key=api_key)

# Estilização Customizada
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #1f77b4; color: white; }
    .service-card { background-color: white; padding: 20px; border-radius: 10px; border-left: 5px solid #1f77b4; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# 2. GESTÃO DE NAVEGAÇÃO
if 'menu_option' not in st.session_state:
    st.session_state.menu_option = "🏠 Início"

# 3. BARRA LATERAL (MENU)
with st.sidebar:
    # Mostra o logo
    st.image("IMG_6163.jpeg", use_container_width=True)
    st.title("DS Consulting IT")
    st.markdown("---")
    
    # Sincroniza o radio com o estado global
    menu_list = ["🏠 Início", "🎯 Estratégia", "💰 Catálogo de Serviços", "🧪 Laboratório DS", "🤖 Agente IA 24/7"]
    current_index = menu_list.index(st.session_state.menu_option)
    
    menu = st.radio("Navegação", menu_list, index=current_index, key="nav_radio")
    st.session_state.menu_option = menu

    st.markdown("---")
    st.markdown("📩 **ds.consulting.it@outlook.com**")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/company/digital-solutions-consulting-it/)")

# --- PÁGINA 1: INÍCIO ---
if st.session_state.menu_option == "🏠 Início":
    st.title("A tecnologia a trabalhar para si. 🚀")
    st.subheader("Transformamos o caos operacional em eficiência digital para PMEs.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### Porquê a DS Consulting IT?
        Muitas empresas perdem horas em tarefas repetitivas. 
        Utilizamos **Google, Microsoft e IA** para devolver-lhe o seu tempo.
        """)
        # BOTÃO QUE AGORA FUNCIONA E MUDA A PÁGINA
        if st.button("Ver a Nossa Estratégia"):
            st.session_state.menu_option = "🎯 Estratégia"
            st.rerun()
    
    with col2:
        st.info("💡 **Diferencial:** Arquitetura de custo zero e máxima eficiência.")

# --- PÁGINA 2: ESTRATÉGIA ---
elif st.session_state.menu_option == "🎯 Estratégia":
    st.title("🎯 Nossa Estratégia e Método")
    st.markdown("### Arquitetura de Custo Zero & Eficiência Máxima")
    
    st.divider()
    st.subheader("🚀 Roteiro em 4 Passos")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown("#### 1. Diagnóstico\nIdentificamos gargalos.")
    with c2: st.markdown("#### 2. Setup Base\nOrganizamos o Office/Google.")
    with c3: st.markdown("#### 3. Automação\nCriamos robôs e IA.")
    with c4: st.markdown("#### 4. Suporte\nEvolução contínua.")

# --- PÁGINA 3: CATÁLOGO ---
elif st.session_state.menu_option == "💰 Catálogo de Serviços":
    st.title("💰 Soluções e Investimento")
    servicos = [
        {"Serviço": "Website + Agente IA", "Preço": "Desde 350€", "Nota": "Atendimento 24/7."},
        {"Serviço": "Reorganização Office 365", "Preço": "Desde 300€", "Nota": "Setup profissional."},
        {"Serviço": "O Robô (Automação)", "Preço": "Desde 350€", "Nota": "Python/Power Automate."},
        {"Serviço": "Agente IA Solo", "Preço": "Desde 200€", "Nota": "Integração rápida."},
        {"Serviço": "Suporte Mensal", "Preço": "Desde 50€/mês", "Nota": "Paz de espírito."}
    ]
    for s in servicos:
        st.markdown(f'<div class="service-card"><h4 style="margin:0;">{s["Serviço"]} — <span style="color:#1f77b4;">{s["Preço"]}</span></h4><p style="margin:5px 0 0 0; color:#666;">{s["Nota"]}</p></div>', unsafe_allow_html=True)

# --- PÁGINA 4: LABORATÓRIO ---
elif st.session_state.menu_option == "🧪 Laboratório DS":
    st.title("🧪 Laboratório de Demonstração")
    st.write("Envie um e-mail para **ds.consulting.it.geral@gmail.com** com as tags:")
    col1, col2, col3 = st.columns(3)
    with col1: st.success("### [ai dados]")
    with col2: st.success("### [AI Reports]")
    with col3: st.success("### [ai business]")

# --- PÁGINA 5: AGENTE IA (LLAMA 3) ---
elif st.session_state.menu_option == "🤖 Agente IA 24/7":
    st.title("🤖 Consultor Estratégico DS")
    
    system_prompt = """
    És o Consultor de IA da 'Digital Solutions & Consulting IT'. 
    Teu objetivo: Mostrar como a automação e IA salvam tempo e dinheiro.
    Valores: Eficiência, custo zero em licenciamento, foco em PMEs.
    Serviços: Website+IA (350€), Robôs Automação (350€), Setup Office (300€).
    Responde sempre em Português de Portugal, de forma curta e profissional.
    """

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": system_prompt}]

    for msg in [m for m in st.session_state.messages if m["role"] != "system"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Como posso ajudar a sua empresa?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.markdown(prompt)
        
        with st.chat_message("assistant"):
            chat_completion = client.chat.completions.create(
                messages=st.session_state.messages,
                model="llama3-8b-8192",
            )
            response = chat_completion.choices[0].message.content
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown("---")
st.caption("© 2026 Digital Solutions & Consulting IT")
