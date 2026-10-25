import streamlit as st
from html import escape

# ============================================================
# DIGITAL SOLUTIONS & CONSULTING IT
# Premium, conversion-focused multilingual Streamlit website
# ============================================================

st.set_page_config(
    page_title="Digital Solutions & Consulting IT | Automação e IA",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------- BRAND --------------------------
BRAND = "Digital Solutions & Consulting IT"
CONTACT_EMAIL = "ds.consulting.it@outlook.com"
LINKEDIN_URL = "https://www.linkedin.com/company/digital-solutions-consulting-it/"
AI_DEMO_URL = "https://agente-ia-digital-solutions-consulting-it.streamlit.app/"

# Replace with your real company logo/image path if available.
LOGO_PATH = "IMG_6163.jpeg"

# ----------------------------- CSS ---------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

    :root {
        --navy: #0b1220;
        --navy-2: #111d35;
        --blue: #2563eb;
        --cyan: #67e8f9;
        --ink: #142033;
        --muted: #64748b;
        --line: #e2e8f0;
        --paper: #f7f9fc;
        --white: #ffffff;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', sans-serif;
    }
    .stApp { background: var(--paper); color: var(--ink); }
    [data-testid="stHeader"] { background: rgba(247,249,252,.85); }
    [data-testid="stSidebar"] {
        background: #0b1220;
        border-right: 1px solid rgba(255,255,255,.08);
    }
    [data-testid="stSidebar"] * { color: #e5edf9; }
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: #c2cde0; }
    [data-testid="stSidebar"] hr { border-color: rgba(255,255,255,.15); }
    .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 1240px; }

    h1, h2, h3 { font-family: 'Manrope', sans-serif !important; letter-spacing: -0.035em; }
    h1 { color: var(--navy); }
    h2, h3 { color: var(--ink); }

    .eyebrow {
        color: #2563eb; text-transform: uppercase; letter-spacing: .16em;
        font-size: .75rem; font-weight: 800; margin-bottom: .8rem;
    }
    .hero {
        position: relative; overflow: hidden; border-radius: 28px;
        padding: clamp(2rem, 5vw, 4.5rem);
        background: radial-gradient(circle at 90% 10%, rgba(103,232,249,.20), transparent 28%),
                    radial-gradient(circle at 10% 100%, rgba(37,99,235,.25), transparent 35%),
                    linear-gradient(135deg, #0b1220 0%, #111d35 65%, #172b50 100%);
        color: white; margin-bottom: 1.5rem;
        box-shadow: 0 24px 70px rgba(15,23,42,.16);
    }
    .hero h1 {
        color: #fff !important; font-size: clamp(2.25rem, 5.5vw, 4.4rem) !important;
        line-height: 1.04 !important; font-weight: 800 !important; max-width: 850px;
        margin: 0 0 1.2rem 0;
    }
    .hero p { color: #d8e4f5; font-size: clamp(1.03rem, 1.6vw, 1.25rem); line-height: 1.75; max-width: 740px; }
    .hero .hero-note { color: #a8f3ff; font-size: .9rem; font-weight: 700; letter-spacing: .04em; margin-bottom: 1rem; }
    .pill {
        display: inline-block; border: 1px solid rgba(255,255,255,.23); color: #e8f3ff;
        border-radius: 999px; padding: .45rem .8rem; font-size: .78rem; margin: .25rem .25rem 0 0;
        background: rgba(255,255,255,.06);
    }
    .section-kicker { color: var(--blue); font-weight: 800; text-transform: uppercase; letter-spacing: .14em; font-size: .73rem; }
    .section-title { font-family: 'Manrope', sans-serif; color: var(--navy); font-size: clamp(1.8rem, 3vw, 2.65rem); font-weight: 800; line-height: 1.12; margin: .45rem 0 .75rem; }
    .section-copy { color: var(--muted); font-size: 1.02rem; line-height: 1.75; max-width: 780px; margin-bottom: 1.5rem; }
    .card {
        background: white; border: 1px solid var(--line); border-radius: 20px;
        padding: 1.45rem; height: 100%; box-shadow: 0 8px 26px rgba(15,23,42,.035);
    }
    .card .icon { font-size: 1.7rem; margin-bottom: .8rem; }
    .card h3 { font-size: 1.12rem; margin: 0 0 .55rem 0; color: var(--navy); }
    .card p { color: var(--muted); line-height: 1.65; font-size: .94rem; }
    .card .small-label { color: var(--blue); font-size: .75rem; font-weight: 800; text-transform: uppercase; letter-spacing: .1em; }
    .dark-panel {
        background: linear-gradient(135deg, #101b30, #172c50); border-radius: 24px;
        padding: clamp(1.5rem, 4vw, 2.5rem); color: white;
    }
    .dark-panel h2, .dark-panel h3 { color: white !important; }
    .dark-panel p { color: #d4deee; line-height: 1.75; }
    .metric {
        background: rgba(255,255,255,.07); border: 1px solid rgba(255,255,255,.13);
        border-radius: 15px; padding: 1rem; height: 100%;
    }
    .metric strong { display:block; color: #a8f3ff; font-size: 1.05rem; margin-bottom: .35rem; }
    .metric span { color: #d4deee; font-size: .88rem; }
    .step-number {
        display: inline-flex; width: 2.25rem; height: 2.25rem; border-radius: 12px;
        align-items: center; justify-content: center; background: #dbeafe; color: #1d4ed8;
        font-weight: 800; margin-bottom: .8rem;
    }
    .trust-line { color: #64748b; font-size: .85rem; text-align: center; margin: .8rem 0 1.8rem; }
    .footer {
        margin-top: 3rem; padding: 1.5rem 0 .5rem; border-top: 1px solid var(--line);
        color: #64748b; font-size: .83rem; text-align: center;
    }
    div.stButton > button, div.stLinkButton > a {
        border-radius: 12px !important; font-weight: 700 !important;
        padding: .65rem 1rem !important; border: 1px solid #2563eb !important;
    }
    div.stButton > button[kind="primary"] {
        background: #2563eb !important; color: white !important;
    }
    div.stButton > button:hover, div.stLinkButton > a:hover { transform: translateY(-1px); }
    [data-testid="stMetric"] { background: white; border: 1px solid var(--line); padding: 1rem; border-radius: 16px; }
    .stAlert { border-radius: 14px; }
    @media (max-width: 700px) {
        .block-container { padding-left: 1rem; padding-right: 1rem; }
        .hero { border-radius: 20px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------- TRANSLATIONS ---------------------
TEXT = {
    "English": {
        "nav": "Navigation",
        "home": "Home",
        "services_nav": "Services",
        "method": "How we work",
        "lab": "AI Lab",
        "contact": "Contact",
        "language": "Language",
        "hero_kicker": "AUTOMATION · DATA · PRACTICAL AI",
        "hero_title": "Less manual work. More time to grow.",
        "hero_sub": "We help small and medium-sized businesses simplify repetitive work, connect everyday tools and turn information into useful decisions.",
        "cta": "Discuss a process",
        "secondary_cta": "Explore our approach",
        "pills": ["Process automation", "Data & reporting", "AI solutions"],
        "trust": "Practical solutions shaped around your workflow — not technology for technology’s sake.",
        "problem_kicker": "THE OPPORTUNITY",
        "problem_title": "Your team’s time is too valuable for repetitive tasks.",
        "problem_copy": "Copying data between systems, preparing recurring reports and sorting documents can consume hours every week. We help identify which steps can be simplified, automated or supported by AI.",
        "problem_cards": [
            ("⏱️", "Time lost to manual work", "Reduce repetitive steps so your team can focus on customers and higher-value work."),
            ("🔁", "Disconnected tools", "Improve workflows between spreadsheets, email, cloud storage and business applications."),
            ("📊", "Reports that take too long", "Turn recurring data preparation into a more consistent, repeatable process."),
        ],
        "services_kicker": "WHAT WE DO",
        "services_title": "Focused solutions for real business problems.",
        "services_copy": "We start with the process and the outcome. The technology comes second.",
        "services": [
            ("⚙️", "Workflow automation", "Automate recurring tasks, data entry, file handling and hand-offs between systems using suitable automation tools.", "AUTOMATION"),
            ("📈", "Data processing & reporting", "Clean, combine and analyse Excel or CSV data, and streamline the creation of recurring reports.", "DATA"),
            ("🧠", "Practical AI solutions", "Explore document processing, information extraction and AI assistants for well-defined business tasks.", "AI"),
            ("☁️", "Microsoft 365 & cloud workflows", "Improve the way your team uses tools such as Excel, Outlook, OneDrive, SharePoint and Power Automate.", "WORKSPACE"),
            ("🌐", "Websites & digital tools", "Create a clear digital presence and lightweight tools that support your customer or internal workflows.", "DIGITAL"),
            ("🛠️", "Ongoing support", "Keep delivered solutions useful with adjustments, troubleshooting and practical guidance.", "SUPPORT"),
        ],
        "proof_kicker": "A PRACTICAL START",
        "proof_title": "Start with one process. Prove the value. Then scale.",
        "proof_copy": "You do not need to transform everything at once. We can begin with a short discovery conversation, map the current process and assess whether an improvement is worthwhile.",
        "proof_metrics": [
            ("01 · Understand", "What takes time, causes errors or creates bottlenecks?"),
            ("02 · Assess", "What can be simplified with the tools you already use?"),
            ("03 · Improve", "Agree on a realistic scope, next steps and success measures."),
        ],
        "method_kicker": "HOW WE WORK",
        "method_title": "Clear steps. No unnecessary complexity.",
        "method_copy": "A straightforward process designed to keep the scope understandable and the work focused.",
        "steps": [
            ("Discovery", "We discuss your workflow, constraints and desired outcome."),
            ("Recommendation", "We identify practical options and agree on scope before development."),
            ("Build & test", "We implement and test the solution against real scenarios."),
            ("Handover & support", "We explain how it works and discuss support or future improvements."),
        ],
        "lab_kicker": "TRY A DEMONSTRATION",
        "lab_title": "See how practical AI can help.",
        "lab_copy": "Explore our AI demonstration environment to understand possible workflows. Do not upload confidential, personal or sensitive business data into a public demo.",
        "lab_button": "Open the AI Lab",
        "contact_kicker": "LET’S TALK",
        "contact_title": "What process would you like to improve?",
        "contact_copy": "Tell us briefly what takes too much time in your business. We can discuss whether automation, data processing or AI is a sensible fit.",
        "name": "Your name",
        "company": "Company",
        "email": "Business email",
        "need": "What would you like to improve?",
        "need_placeholder": "For example: preparing a weekly report takes 3 hours...",
        "send": "Prepare email",
        "form_note": "This button opens your email application with a draft. It does not send anything automatically.",
        "email_direct": "Or email us directly:",
        "footer": "Practical technology. Better workflows. More time for your business.",
        "privacy_note": "Please do not include confidential or sensitive information in this form.",
        "budget_note": "Project scope and pricing are discussed after understanding the process and requirements.",
        "success": "Your email draft is ready to open in your email application.",
        "required": "Please provide your name, a valid email address and a short description.",
    },
    "Português": {
        "nav": "Navegação",
        "home": "Início",
        "services_nav": "Serviços",
        "method": "Como trabalhamos",
        "lab": "Laboratório IA",
        "contact": "Contacto",
        "language": "Idioma",
        "hero_kicker": "AUTOMAÇÃO · DADOS · IA PRÁTICA",
        "hero_title": "Menos trabalho manual. Mais tempo para crescer.",
        "hero_sub": "Ajudamos pequenas e médias empresas a simplificar tarefas repetitivas, ligar ferramentas do dia a dia e transformar informação em decisões úteis.",
        "cta": "Falar sobre um processo",
        "secondary_cta": "Conhecer o método",
        "pills": ["Automação de processos", "Dados e relatórios", "Soluções de IA"],
        "trust": "Soluções práticas adaptadas ao seu processo — tecnologia com um propósito concreto.",
        "problem_kicker": "A OPORTUNIDADE",
        "problem_title": "O tempo da sua equipa vale demasiado para tarefas repetitivas.",
        "problem_copy": "Copiar dados entre sistemas, preparar relatórios recorrentes e organizar documentos pode consumir horas todas as semanas. Ajudamos a identificar o que pode ser simplificado, automatizado ou apoiado por IA.",
        "problem_cards": [
            ("⏱️", "Tempo perdido em tarefas manuais", "Reduza etapas repetitivas para a equipa se concentrar nos clientes e no trabalho de maior valor."),
            ("🔁", "Ferramentas pouco ligadas", "Melhore os fluxos entre folhas de cálculo, email, armazenamento na cloud e aplicações empresariais."),
            ("📊", "Relatórios demorados", "Torne a preparação recorrente de dados mais consistente e fácil de repetir."),
        ],
        "services_kicker": "O QUE FAZEMOS",
        "services_title": "Soluções focadas em problemas reais do negócio.",
        "services_copy": "Começamos pelo processo e pelo resultado pretendido. A tecnologia vem depois.",
        "services": [
            ("⚙️", "Automação de processos", "Automatização de tarefas recorrentes, introdução de dados, gestão de ficheiros e passagens de informação entre sistemas.", "AUTOMAÇÃO"),
            ("📈", "Tratamento de dados e relatórios", "Limpeza, combinação e análise de dados Excel ou CSV e simplificação de relatórios recorrentes.", "DADOS"),
            ("🧠", "Soluções práticas de IA", "Análise de documentos, extração de informação e assistentes de IA para tarefas empresariais bem definidas.", "IA"),
            ("☁️", "Microsoft 365 e cloud", "Melhoria dos fluxos de trabalho com Excel, Outlook, OneDrive, SharePoint e Power Automate.", "PRODUTIVIDADE"),
            ("🌐", "Websites e ferramentas digitais", "Presença digital clara e ferramentas simples que apoiam os processos internos ou o contacto com clientes.", "DIGITAL"),
            ("🛠️", "Acompanhamento e suporte", "Ajustes, resolução de problemas e orientação prática para manter as soluções úteis ao longo do tempo.", "SUPORTE"),
        ],
        "proof_kicker": "COMEÇAR DE FORMA PRÁTICA",
        "proof_title": "Começar por um processo. Validar o valor. Depois evoluir.",
        "proof_copy": "Não precisa de transformar tudo de uma vez. Podemos começar com uma conversa, mapear o processo atual e avaliar se uma melhoria faz sentido.",
        "proof_metrics": [
            ("01 · Compreender", "O que consome tempo, provoca erros ou cria bloqueios?"),
            ("02 · Avaliar", "O que pode ser simplificado com as ferramentas que já utiliza?"),
            ("03 · Melhorar", "Definir um âmbito realista, próximos passos e critérios de sucesso."),
        ],
        "method_kicker": "COMO TRABALHAMOS",
        "method_title": "Etapas claras. Sem complexidade desnecessária.",
        "method_copy": "Um processo simples para manter o âmbito compreensível e o trabalho focado.",
        "steps": [
            ("Diagnóstico", "Conversamos sobre o processo, as limitações e o resultado pretendido."),
            ("Recomendação", "Identificamos opções práticas e acordamos o âmbito antes do desenvolvimento."),
            ("Desenvolvimento e testes", "Implementamos e testamos a solução com cenários reais."),
            ("Entrega e suporte", "Explicamos o funcionamento e combinamos o suporte ou melhorias futuras."),
        ],
        "lab_kicker": "EXPERIMENTE UMA DEMONSTRAÇÃO",
        "lab_title": "Veja como a IA pode ajudar na prática.",
        "lab_copy": "Explore o nosso ambiente de demonstração para conhecer possíveis fluxos de trabalho. Não carregue dados confidenciais, pessoais ou sensíveis numa demonstração pública.",
        "lab_button": "Abrir Laboratório IA",
        "contact_kicker": "VAMOS CONVERSAR",
        "contact_title": "Que processo gostaria de melhorar?",
        "contact_copy": "Explique brevemente o que consome demasiado tempo no seu negócio. Podemos avaliar se a automação, o tratamento de dados ou a IA fazem sentido.",
        "name": "O seu nome",
        "company": "Empresa",
        "email": "Email profissional",
        "need": "O que gostaria de melhorar?",
        "need_placeholder": "Por exemplo: preparar um relatório semanal demora 3 horas...",
        "send": "Preparar email",
        "form_note": "Este botão abre a aplicação de email com uma mensagem preparada. Não envia nada automaticamente.",
        "email_direct": "Ou envie-nos um email:",
        "footer": "Tecnologia prática. Melhores processos. Mais tempo para o seu negócio.",
        "privacy_note": "Não inclua informação confidencial ou sensível neste formulário.",
        "budget_note": "O âmbito e o preço são discutidos depois de compreendermos o processo e os requisitos.",
        "success": "O rascunho está pronto para abrir na sua aplicação de email.",
        "required": "Indique o seu nome, um email válido e uma breve descrição.",
    },
    "Français": {
        "nav": "Navigation",
        "home": "Accueil",
        "services_nav": "Services",
        "method": "Notre méthode",
        "lab": "Laboratoire IA",
        "contact": "Contact",
        "language": "Langue",
        "hero_kicker": "AUTOMATISATION · DONNÉES · IA PRATIQUE",
        "hero_title": "Moins de tâches manuelles. Plus de temps pour grandir.",
        "hero_sub": "Nous aidons les petites et moyennes entreprises à simplifier les tâches répétitives, connecter leurs outils et transformer les données en décisions utiles.",
        "cta": "Parler d’un processus",
        "secondary_cta": "Découvrir notre méthode",
        "pills": ["Automatisation", "Données et rapports", "Solutions IA"],
        "trust": "Des solutions pratiques adaptées à vos processus — la technologie au service d’un objectif concret.",
        "problem_kicker": "L’OPPORTUNITÉ",
        "problem_title": "Le temps de votre équipe est trop précieux pour les tâches répétitives.",
        "problem_copy": "La saisie entre systèmes, les rapports récurrents et le classement de documents peuvent prendre des heures chaque semaine. Nous identifions ce qui peut être simplifié, automatisé ou assisté par l’IA.",
        "problem_cards": [
            ("⏱️", "Temps perdu en tâches manuelles", "Réduisez les étapes répétitives pour que l’équipe se concentre sur les activités à plus forte valeur."),
            ("🔁", "Outils peu connectés", "Améliorez les flux entre tableurs, e-mails, stockage cloud et applications métier."),
            ("📊", "Rapports trop longs à préparer", "Rendez la préparation des données plus cohérente et reproductible."),
        ],
        "services_kicker": "NOS SERVICES",
        "services_title": "Des solutions centrées sur les vrais besoins de l’entreprise.",
        "services_copy": "Nous partons du processus et du résultat attendu. La technologie vient ensuite.",
        "services": [
            ("⚙️", "Automatisation des processus", "Automatisation des tâches récurrentes, de la saisie de données et des échanges entre systèmes.", "AUTOMATISATION"),
            ("📈", "Données et rapports", "Nettoyage, combinaison et analyse de données Excel ou CSV et simplification des rapports récurrents.", "DONNÉES"),
            ("🧠", "Solutions IA pratiques", "Traitement de documents, extraction d’informations et assistants IA pour des tâches métier bien définies.", "IA"),
            ("☁️", "Microsoft 365 et cloud", "Amélioration des flux avec Excel, Outlook, OneDrive, SharePoint et Power Automate.", "PRODUCTIVITÉ"),
            ("🌐", "Sites web et outils numériques", "Présence numérique claire et outils simples pour les processus internes ou la relation client.", "NUMÉRIQUE"),
            ("🛠️", "Support continu", "Ajustements, résolution de problèmes et accompagnement pour maintenir les solutions utiles.", "SUPPORT"),
        ],
        "proof_kicker": "UNE APPROCHE PRATIQUE",
        "proof_title": "Commencer par un processus. Valider la valeur. Puis évoluer.",
        "proof_copy": "Il n’est pas nécessaire de tout transformer en même temps. Nous pouvons commencer par un échange et évaluer les améliorations possibles.",
        "proof_metrics": [
            ("01 · Comprendre", "Qu’est-ce qui prend du temps, provoque des erreurs ou crée des blocages ?"),
            ("02 · Évaluer", "Que peut-on simplifier avec les outils déjà disponibles ?"),
            ("03 · Améliorer", "Définir un périmètre réaliste et des critères de réussite."),
        ],
        "method_kicker": "NOTRE MÉTHODE",
        "method_title": "Des étapes claires. Sans complexité inutile.",
        "method_copy": "Une méthode simple pour garder un périmètre compréhensible et un travail ciblé.",
        "steps": [
            ("Diagnostic", "Nous échangeons sur le processus, les contraintes et le résultat attendu."),
            ("Recommandation", "Nous identifions les options et définissons le périmètre."),
            ("Développement et tests", "Nous réalisons et testons la solution sur des cas concrets."),
            ("Livraison et support", "Nous expliquons le fonctionnement et les options de suivi."),
        ],
        "lab_kicker": "ESSAYER UNE DÉMONSTRATION",
        "lab_title": "Découvrez l’IA en pratique.",
        "lab_copy": "Explorez notre environnement de démonstration. N’y envoyez aucune donnée confidentielle, personnelle ou sensible.",
        "lab_button": "Ouvrir le laboratoire IA",
        "contact_kicker": "ÉCHANGEONS",
        "contact_title": "Quel processus souhaitez-vous améliorer ?",
        "contact_copy": "Expliquez brièvement ce qui prend trop de temps dans votre activité. Nous évaluerons si l’automatisation, les données ou l’IA sont adaptées.",
        "name": "Votre nom",
        "company": "Entreprise",
        "email": "E-mail professionnel",
        "need": "Que souhaitez-vous améliorer ?",
        "need_placeholder": "Exemple : préparer un rapport hebdomadaire prend 3 heures...",
        "send": "Préparer l’e-mail",
        "form_note": "Ce bouton ouvre votre application e-mail avec un brouillon. Aucun message n’est envoyé automatiquement.",
        "email_direct": "Ou contactez-nous directement :",
        "footer": "Technologie pratique. Meilleurs processus. Plus de temps pour votre entreprise.",
        "privacy_note": "N’incluez aucune information confidentielle ou sensible.",
        "budget_note": "Le périmètre et le prix sont discutés après analyse du besoin.",
        "success": "Le brouillon est prêt à être ouvert dans votre application e-mail.",
        "required": "Veuillez indiquer votre nom, un e-mail valide et une brève description.",
    },
    "Español": {
        "nav": "Navegación",
        "home": "Inicio",
        "services_nav": "Servicios",
        "method": "Cómo trabajamos",
        "lab": "Laboratorio IA",
        "contact": "Contacto",
        "language": "Idioma",
        "hero_kicker": "AUTOMATIZACIÓN · DATOS · IA PRÁCTICA",
        "hero_title": "Menos trabajo manual. Más tiempo para crecer.",
        "hero_sub": "Ayudamos a pequeñas y medianas empresas a simplificar tareas repetitivas, conectar herramientas y convertir datos en decisiones útiles.",
        "cta": "Hablar de un proceso",
        "secondary_cta": "Conocer el método",
        "pills": ["Automatización", "Datos e informes", "Soluciones de IA"],
        "trust": "Soluciones prácticas adaptadas a tus procesos: tecnología con un objetivo concreto.",
        "problem_kicker": "LA OPORTUNIDAD",
        "problem_title": "El tiempo de tu equipo vale demasiado para tareas repetitivas.",
        "problem_copy": "Copiar datos entre sistemas, preparar informes recurrentes y organizar documentos puede consumir horas cada semana. Identificamos qué se puede simplificar, automatizar o apoyar con IA.",
        "problem_cards": [
            ("⏱️", "Tiempo perdido en tareas manuales", "Reduce pasos repetitivos para centrarte en clientes y tareas de mayor valor."),
            ("🔁", "Herramientas desconectadas", "Mejora los flujos entre hojas de cálculo, correo, nube y aplicaciones empresariales."),
            ("📊", "Informes lentos", "Haz que la preparación de datos sea más coherente y repetible."),
        ],
        "services_kicker": "QUÉ HACEMOS",
        "services_title": "Soluciones centradas en problemas reales del negocio.",
        "services_copy": "Empezamos por el proceso y el resultado. La tecnología viene después.",
        "services": [
            ("⚙️", "Automatización de procesos", "Automatiza tareas recurrentes, entrada de datos y transferencias entre sistemas.", "AUTOMATIZACIÓN"),
            ("📈", "Datos e informes", "Limpieza, combinación y análisis de datos Excel o CSV y simplificación de informes.", "DATOS"),
            ("🧠", "Soluciones prácticas de IA", "Procesamiento de documentos, extracción de información y asistentes de IA para tareas concretas.", "IA"),
            ("☁️", "Microsoft 365 y nube", "Mejora los flujos con Excel, Outlook, OneDrive, SharePoint y Power Automate.", "PRODUCTIVIDAD"),
            ("🌐", "Web y herramientas digitales", "Presencia digital clara y herramientas sencillas para procesos internos o clientes.", "DIGITAL"),
            ("🛠️", "Soporte continuo", "Ajustes, resolución de problemas y orientación práctica para mantener las soluciones útiles.", "SOPORTE"),
        ],
        "proof_kicker": "EMPEZAR DE FORMA PRÁCTICA",
        "proof_title": "Empieza con un proceso. Valida el valor. Después escala.",
        "proof_copy": "No necesitas transformarlo todo a la vez. Podemos empezar con una conversación y evaluar mejoras posibles.",
        "proof_metrics": [
            ("01 · Entender", "¿Qué consume tiempo, provoca errores o crea bloqueos?"),
            ("02 · Evaluar", "¿Qué se puede simplificar con las herramientas actuales?"),
            ("03 · Mejorar", "Definir un alcance realista y criterios de éxito."),
        ],
        "method_kicker": "CÓMO TRABAJAMOS",
        "method_title": "Pasos claros. Sin complejidad innecesaria.",
        "method_copy": "Un proceso sencillo para mantener el alcance claro y el trabajo enfocado.",
        "steps": [
            ("Diagnóstico", "Hablamos del proceso, las limitaciones y el resultado deseado."),
            ("Recomendación", "Identificamos opciones prácticas y acordamos el alcance."),
            ("Desarrollo y pruebas", "Implementamos y probamos la solución con casos reales."),
            ("Entrega y soporte", "Explicamos el funcionamiento y las opciones de seguimiento."),
        ],
        "lab_kicker": "PRUEBA UNA DEMOSTRACIÓN",
        "lab_title": "Descubre la IA en la práctica.",
        "lab_copy": "Explora nuestro entorno de demostración. No subas datos confidenciales, personales o sensibles.",
        "lab_button": "Abrir Laboratorio IA",
        "contact_kicker": "HABLEMOS",
        "contact_title": "¿Qué proceso te gustaría mejorar?",
        "contact_copy": "Cuéntanos brevemente qué consume demasiado tiempo. Evaluaremos si la automatización, los datos o la IA encajan.",
        "name": "Tu nombre",
        "company": "Empresa",
        "email": "Correo profesional",
        "need": "¿Qué te gustaría mejorar?",
        "need_placeholder": "Por ejemplo: preparar un informe semanal tarda 3 horas...",
        "send": "Preparar correo",
        "form_note": "Este botón abre tu aplicación de correo con un borrador. No envía nada automáticamente.",
        "email_direct": "O escríbenos directamente:",
        "footer": "Tecnología práctica. Mejores procesos. Más tiempo para tu negocio.",
        "privacy_note": "No incluyas información confidencial o sensible.",
        "budget_note": "El alcance y el precio se definen después de comprender la necesidad.",
        "success": "El borrador está listo para abrirse en tu aplicación de correo.",
        "required": "Indica tu nombre, un correo válido y una breve descripción.",
    },
    "Italiano": {
        "nav": "Navigazione",
        "home": "Home",
        "services_nav": "Servizi",
        "method": "Come lavoriamo",
        "lab": "Laboratorio IA",
        "contact": "Contatti",
        "language": "Lingua",
        "hero_kicker": "AUTOMAZIONE · DATI · IA PRATICA",
        "hero_title": "Meno lavoro manuale. Più tempo per crescere.",
        "hero_sub": "Aiutiamo le piccole e medie imprese a semplificare le attività ripetitive, collegare gli strumenti e trasformare i dati in decisioni utili.",
        "cta": "Parliamo di un processo",
        "secondary_cta": "Scopri il metodo",
        "pills": ["Automazione", "Dati e report", "Soluzioni IA"],
        "trust": "Soluzioni pratiche adattate ai tuoi processi: tecnologia con uno scopo concreto.",
        "problem_kicker": "L’OPPORTUNITÀ",
        "problem_title": "Il tempo del tuo team è troppo prezioso per le attività ripetitive.",
        "problem_copy": "Copiare dati tra sistemi, preparare report ricorrenti e organizzare documenti può richiedere ore ogni settimana. Individuiamo cosa semplificare, automatizzare o supportare con l’IA.",
        "problem_cards": [
            ("⏱️", "Tempo perso in attività manuali", "Riduci i passaggi ripetitivi per concentrarti sui clienti e sulle attività di maggior valore."),
            ("🔁", "Strumenti non collegati", "Migliora i flussi tra fogli di calcolo, email, cloud e applicazioni aziendali."),
            ("📊", "Report lenti da preparare", "Rendi la preparazione dei dati più coerente e ripetibile."),
        ],
        "services_kicker": "COSA FACCIAMO",
        "services_title": "Soluzioni focalizzate su problemi aziendali reali.",
        "services_copy": "Partiamo dal processo e dal risultato. La tecnologia viene dopo.",
        "services": [
            ("⚙️", "Automazione dei processi", "Automatizza attività ricorrenti, inserimento dati e passaggi tra sistemi.", "AUTOMAZIONE"),
            ("📈", "Dati e report", "Pulizia, combinazione e analisi di dati Excel o CSV e semplificazione dei report.", "DATI"),
            ("🧠", "Soluzioni IA pratiche", "Elaborazione documenti, estrazione di informazioni e assistenti IA per attività definite.", "IA"),
            ("☁️", "Microsoft 365 e cloud", "Migliora i flussi con Excel, Outlook, OneDrive, SharePoint e Power Automate.", "PRODUTTIVITÀ"),
            ("🌐", "Siti web e strumenti digitali", "Presenza digitale chiara e strumenti semplici per i processi interni o i clienti.", "DIGITALE"),
            ("🛠️", "Supporto continuo", "Modifiche, risoluzione problemi e consulenza pratica per mantenere utili le soluzioni.", "SUPPORTO"),
        ],
        "proof_kicker": "UN INIZIO PRATICO",
        "proof_title": "Partire da un processo. Verificare il valore. Poi crescere.",
        "proof_copy": "Non serve trasformare tutto subito. Possiamo iniziare con una conversazione e valutare le opportunità di miglioramento.",
        "proof_metrics": [
            ("01 · Capire", "Cosa richiede tempo, provoca errori o crea ostacoli?"),
            ("02 · Valutare", "Cosa si può semplificare con gli strumenti già disponibili?"),
            ("03 · Migliorare", "Definire un ambito realistico e criteri di successo."),
        ],
        "method_kicker": "COME LAVORIAMO",
        "method_title": "Passaggi chiari. Nessuna complessità inutile.",
        "method_copy": "Un processo semplice per mantenere chiaro l’ambito e concentrato il lavoro.",
        "steps": [
            ("Analisi", "Parliamo del processo, dei vincoli e del risultato desiderato."),
            ("Raccomandazione", "Individuiamo opzioni pratiche e concordiamo l’ambito."),
            ("Sviluppo e test", "Implementiamo e testiamo la soluzione su casi reali."),
            ("Consegna e supporto", "Spieghiamo il funzionamento e le opzioni di assistenza."),
        ],
        "lab_kicker": "PROVA UNA DIMOSTRAZIONE",
        "lab_title": "Scopri l’IA nella pratica.",
        "lab_copy": "Esplora il nostro ambiente dimostrativo. Non caricare dati riservati, personali o sensibili.",
        "lab_button": "Apri Laboratorio IA",
        "contact_kicker": "PARLIAMONE",
        "contact_title": "Quale processo vorresti migliorare?",
        "contact_copy": "Descrivi brevemente cosa richiede troppo tempo. Valuteremo se automazione, dati o IA sono adatti.",
        "name": "Il tuo nome",
        "company": "Azienda",
        "email": "Email professionale",
        "need": "Cosa vorresti migliorare?",
        "need_placeholder": "Ad esempio: preparare un report settimanale richiede 3 ore...",
        "send": "Prepara email",
        "form_note": "Il pulsante apre la tua applicazione email con una bozza. Non invia automaticamente.",
        "email_direct": "Oppure scrivici direttamente:",
        "footer": "Tecnologia pratica. Processi migliori. Più tempo per la tua azienda.",
        "privacy_note": "Non inserire informazioni riservate o sensibili.",
        "budget_note": "Ambito e prezzo vengono discussi dopo aver compreso il processo.",
        "success": "La bozza è pronta per essere aperta nella tua applicazione email.",
        "required": "Inserisci il nome, un indirizzo email valido e una breve descrizione.",
    },
}

# ---------------------------- HELPERS ------------------------
def section_heading(kicker: str, title: str, copy: str):
    st.markdown(
        f'<div class="section-kicker">{escape(kicker)}</div>'
        f'<div class="section-title">{escape(title)}</div>'
        f'<div class="section-copy">{escape(copy)}</div>',
        unsafe_allow_html=True,
    )

def render_card(icon: str, title: str, description: str, label: str = ""):
    safe_label = f'<div class="small-label">{escape(label)}</div>' if label else ""
    st.markdown(
        f"""
        <div class="card">
            <div class="icon">{escape(icon)}</div>
            {safe_label}
            <h3>{escape(title)}</h3>
            <p>{escape(description)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

def valid_email(value: str) -> bool:
    value = value.strip()
    return "@" in value and "." in value.split("@")[-1] and " " not in value

def make_mailto(to: str, subject: str, body: str) -> str:
    from urllib.parse import quote
    return f"mailto:{to}?subject={quote(subject)}&body={quote(body)}"

# --------------------------- SIDEBAR -------------------------
with st.sidebar:
    st.markdown("## 💠 Digital Solutions")
    st.caption("CONSULTING IT")
    st.markdown("---")
    language = st.selectbox(
        "🌐 Language / Idioma / Langue",
        list(TEXT.keys()),
        index=0,
        key="language_choice",
    )
    t = TEXT[language]
    page = st.radio(
        t["nav"],
        [t["home"], t["services_nav"], t["method"], t["lab"], t["contact"]],
        key="navigation",
    )
    st.markdown("---")
    st.markdown("### " + t["contact"])
    st.markdown(f"✉️ [{CONTACT_EMAIL}](mailto:{CONTACT_EMAIL})")
    st.markdown(f"[LinkedIn ↗]({LINKEDIN_URL})")
    st.markdown("---")
    st.caption("Automation · Data · Practical AI")

# ---------------------------- HOME ---------------------------
if page == t["home"]:
    pills = "".join(f'<span class="pill">{escape(item)}</span>' for item in t["pills"])
    st.markdown(
        f"""
        <div class="hero">
            <div class="hero-note">{escape(t["hero_kicker"])}</div>
            <h1>{escape(t["hero_title"])}</h1>
            <p>{escape(t["hero_sub"])}</p>
            {pills}
        </div>
        """,
        unsafe_allow_html=True,
    )
    cta1, cta2, spacer = st.columns([1.4, 1.6, 4])
    with cta1:
        if st.button(t["cta"], type="primary", use_container_width=True):
            st.session_state["navigation"] = t["contact"]
            st.rerun()
    with cta2:
        if st.button(t["secondary_cta"], use_container_width=True):
            st.session_state["navigation"] = t["method"]
            st.rerun()
    st.markdown(f'<div class="trust-line">{escape(t["trust"])}</div>', unsafe_allow_html=True)

    section_heading(t["problem_kicker"], t["problem_title"], t["problem_copy"])
    cols = st.columns(3, gap="medium")
    for col, item in zip(cols, t["problem_cards"]):
        with col:
            render_card(*item)

    st.markdown("<br>", unsafe_allow_html=True)
    section_heading(t["services_kicker"], t["services_title"], t["services_copy"])
    service_cols = st.columns(3, gap="medium")
    for i, item in enumerate(t["services"]):
        with service_cols[i % 3]:
            render_card(*item)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="dark-panel">
            <div class="section-kicker" style="color:#a8f3ff">{escape(t["proof_kicker"])}</div>
            <h2 style="font-size:clamp(1.8rem,3vw,2.6rem); margin:.5rem 0 1rem;">{escape(t["proof_title"])}</h2>
            <p>{escape(t["proof_copy"])}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    metric_cols = st.columns(3, gap="medium")
    for col, (heading, description) in zip(metric_cols, t["proof_metrics"]):
        with col:
            st.markdown(
                f'<div class="card"><h3>{escape(heading)}</h3><p>{escape(description)}</p></div>',
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown(f"### {t['contact_title']}")
        st.write(t["contact_copy"])
    with c2:
        if st.button(t["cta"], type="primary", use_container_width=True, key="home_contact_bottom"):
            st.session_state["navigation"] = t["contact"]
            st.rerun()

# --------------------------- SERVICES ------------------------
elif page == t["services_nav"]:
    section_heading(t["services_kicker"], t["services_title"], t["services_copy"])
    cols = st.columns(3, gap="medium")
    for i, item in enumerate(t["services"]):
        with cols[i % 3]:
            render_card(*item)
    st.markdown("<br>", unsafe_allow_html=True)
    st.info(t["budget_note"])
    if st.button(t["cta"], type="primary"):
        st.session_state["navigation"] = t["contact"]
        st.rerun()

# ---------------------------- METHOD -------------------------
elif page == t["method"]:
    section_heading(t["method_kicker"], t["method_title"], t["method_copy"])
    cols = st.columns(2, gap="large")
    for i, (title, description) in enumerate(t["steps"]):
        with cols[i % 2]:
            st.markdown(
                f"""
                <div class="card">
                    <div class="step-number">{i+1:02d}</div>
                    <h3>{escape(title)}</h3>
                    <p>{escape(description)}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"#### {t['budget_note']}")
    st.write(t["proof_copy"])
    if st.button(t["cta"], type="primary"):
        st.session_state["navigation"] = t["contact"]
        st.rerun()

# ----------------------------- AI LAB ------------------------
elif page == t["lab"]:
    section_heading(t["lab_kicker"], t["lab_title"], t["lab_copy"])
    st.markdown(
        f"""
        <div class="dark-panel">
            <div class="section-kicker" style="color:#a8f3ff">AI DEMONSTRATION</div>
            <h2>{escape(t["lab_title"])}</h2>
            <p>{escape(t["lab_copy"])}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.link_button(t["lab_button"], AI_DEMO_URL, type="primary")
    st.warning(t["privacy_note"])
    st.markdown("#### Email-based demonstrations")
    if language == "Português":
        st.write("Os agentes por email podem ser apresentados como demonstrações, mas confirme que o processamento, os prazos e o envio de respostas estão a funcionar antes de os promover comercialmente.")
        st.write("**[ai dados]** — análise de Excel/CSV · **[AI Solutions]** — sugestões de melhoria · **[AI Reports]** — apoio à análise de documentos.")
    elif language == "Français":
        st.write("Avant de promouvoir les agents par e-mail, vérifiez que le traitement, les délais et les réponses fonctionnent correctement.")
        st.write("**[ai data]** — analyse Excel/CSV · **[AI Solutions]** — pistes d’amélioration · **[AI Reports]** — analyse de documents.")
    elif language == "Español":
        st.write("Antes de promocionar los agentes por correo, comprueba que el procesamiento y las respuestas funcionan correctamente.")
        st.write("**[ai data]** — análisis Excel/CSV · **[AI Solutions]** — mejoras · **[AI Reports]** — análisis de documentos.")
    elif language == "Italiano":
        st.write("Prima di promuovere gli agenti via email, verifica che elaborazione e risposte funzionino correttamente.")
        st.write("**[ai data]** — analisi Excel/CSV · **[AI Solutions]** — miglioramenti · **[AI Reports]** — analisi documenti.")
    else:
        st.write("Before promoting email agents, verify that processing, response delivery and timing work reliably.")
        st.write("**[ai data]** — Excel/CSV analysis · **[AI Solutions]** — improvement ideas · **[AI Reports]** — document analysis.")

# ---------------------------- CONTACT ------------------------
elif page == t["contact"]:
    section_heading(t["contact_kicker"], t["contact_title"], t["contact_copy"])
    left, right = st.columns([1.4, 1], gap="large")
    with left:
        with st.form("contact_form", clear_on_submit=False):
            name = st.text_input(t["name"])
            company = st.text_input(t["company"])
            email = st.text_input(t["email"])
            need = st.text_area(t["need"], placeholder=t["need_placeholder"], height=150)
            submitted = st.form_submit_button(t["send"], type="primary", use_container_width=True)

        st.caption(t["form_note"])
        st.caption(t["privacy_note"])

        if submitted:
            if not name.strip() or not valid_email(email) or not need.strip():
                st.error(t["required"])
            else:
                subject = f"Business enquiry — {company.strip() or name.strip()}"
                body = (
                    f"Name: {name.strip()}\n"
                    f"Company: {company.strip() or 'Not provided'}\n"
                    f"Email: {email.strip()}\n\n"
                    f"Process / challenge:\n{need.strip()}\n"
                )
                mailto = make_mailto(CONTACT_EMAIL, subject, body)
                st.success(t["success"])
                st.link_button("Open email draft ↗", mailto, type="primary")

    with right:
        st.markdown(
            f"""
            <div class="dark-panel">
                <div class="section-kicker" style="color:#a8f3ff">{escape(t["contact_kicker"])}</div>
                <h2>{escape(t["contact_title"])}</h2>
                <p>{escape(t["contact_copy"])}</p>
                <p><strong>{escape(t["email_direct"])}</strong><br>{escape(CONTACT_EMAIL)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.link_button("LinkedIn ↗", LINKEDIN_URL)
        st.link_button(t["lab_button"], AI_DEMO_URL)

# ----------------------------- FOOTER ------------------------
st.markdown(
    f'<div class="footer"><strong>{escape(BRAND)}</strong><br>{escape(t["footer"])}<br>© 2026</div>',
    unsafe_allow_html=True,
)
