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

# 2. DICIONÁRIO DE TRADUÇÕES
translations = {
    "🇬🇧 English": {
        "menu": ["🏠 Home", "🎯 Strategy", "💰 Catalog", "🧪 Laboratory"],
        "nav_title": "Main Navigation:",
        "contact_title": "💡 Direct Contact",
        "home_title": "Technology working for your business 🚀",
        "home_subtitle": "At <b>Digital Solutions & Consulting IT</b>, we turn ordinary tools into efficiency engines. We give you back the time you currently lose on manual processes.",
        "mission_title": "Our Mission 🛡️",
        "mission_text": "Our mission is to ensure your company does not fall behind in the digital age. We believe that automation and Artificial Intelligence should be accessible, allowing your investment to be applied to practical solutions that generate real return, without expensive software licenses. 💎",
        "vision_title": "Future Vision 🔮",
        "vision_text": "To be the strategic partner that simplifies technology. We want our clients to use AI and automation as natural day-to-day tools, seamlessly integrated into operations to boost growth.",
        "why_us": "📊 **Why Us?**\n\n- Focus on Micro and Small Businesses\n- Use tools you already own\n- Reduction of Human Errors\n- Real-Time ROI",
        "specialists": "✨ **Specialists in:**\n- Python & Automation\n- Power Automate\n- Custom AI Agents",
        "strat_title": "The 4-Phase Method ⚡",
        "strat_sub": "A structured approach to ensure solid and scalable results.",
        "p1_title": "1️⃣ Audit & Diagnosis",
        "p1_desc": "We don't implement solutions without first understanding your business. We analyze your current workflow to identify where technology and AI can eliminate repetitive tasks and optimize your team's time.",
        "p2_title": "2️⃣ Digital Architecture",
        "p2_desc": "We organize your infrastructure using what you already own (e.g., **OneDrive, SharePoint, Google Drive**) and explore other free tools to boost your business with security and order.",
        "p3_title": "3️⃣ Development & Implementation",
        "p3_desc": "We bring the project to life with scripts, automations, and websites. We use **Python**, **Power Automate Desktop**, and cutting-edge AI to create solutions ranging from email sorting to database management.",
        "p4_title": "4️⃣ Stability & Training",
        "p4_desc": "We work with you to ensure everything runs smoothly. We provide ongoing training and consulting so technology remains the solid foundation of your company's best practices.",
        "cat_title": "Solutions Catalog",
        "cat_sub": "Elite solutions tailored to your unique requirements.",
        "solution_label": "Custom Proposal",
        "services": [
            {"T": "Corporate Website + AI Agent", "D": "A modern website that acts as your digital business card and the development of an AI agent tailored to your business to interact with your visitors. 🌐"},
            {"T": "Cloud & Office 365 Efficiency", "D": "Professional configuration of permissions and workflows in Office 365 or Google Workspace. End the chaos of lost files and emails. ☁️"},
            {"T": "AI Agents & Data Scripts", "D": "Custom solutions for analyzing reports and large volumes of data, turning raw information into strategic decisions. 🧠"},
            {"T": "Automation (Python/Power Automate)", "D": "Creation of robots and scripts that execute manual tasks, integrate systems, and accelerate your business operations. 🤖"},
            {"T": "AI Consulting & Workshops", "D": "Practical training for your team to learn how to use AI as a daily productivity tool. 🎓"},
            {"T": "Monthly Operational Support", "D": "Priority access for adjustments, fixes, and ongoing consulting to keep your company at the technological forefront. 🛠️"}
        ],
        "lab_title": "Innovation Laboratory 🧪",
        "lab_sub_title": "How to Use Our Free Agents 🤖",
        "lab_desc": "We provide several independent AI Agents that act as our efficiency ambassadors.",
        "lab_box_title": "✨ 24/7 AI Consultant",
        "lab_box_text": "We are pleased to introduce our new Artificial Intelligence Consultant – available for you now!",
        "lab_box_btn": "TRY HERE (FREE)",
        "email_proc_title": "📧 Email Processing Agents",
        "email_proc_info": "Simply send an email to **ds.consulting.it.geral@gmail.com**. Our engine processes requests in scheduled cycles and redirects the analyzed response to you.",
        "exp1_title": "📊 [ai data] – Your Excel with Intelligence",
        "exp1_text": "Send an Excel or CSV file. Include the tag **[ai data]** in the subject.\n**What you receive:** A professional PDF report with statistical analysis, regressions, and dynamic charts to support your strategy.",
        "exp2_title": "💡 [AI Solutions] – Strategic Consulting",
        "exp2_text": "Describe a problem in the body of the email. Include the tag **[AI Solutions]** in the subject.\n**What you receive:** A report with improvement points, low-cost solutions, and ways to boost your business via AI.",
        "exp3_title": "📑 [AI Reports] – Document Assistant",
        "exp3_text": "Send a PDF, Word, or Text document with a question. Include the tag **[AI Reports]** in the subject.\n**What you receive:** A detailed report with intelligent information filtering, saving hours of reading.",
        "footer": "Digital Solutions & Consulting IT | Intelligence in Every Process | 2026"
    },
    "🇵🇹 Português": {
        "menu": ["🏠 Início", "🎯 Estratégia", "💰 Catálogo", "🧪 Laboratório"],
        "nav_title": "Navegação Principal:",
        "contact_title": "💡 Contacto Direto",
        "home_title": "A tecnologia a trabalhar para o seu negócio 🚀",
        "home_subtitle": "Na <b>Digital Solutions & Consulting IT</b>, transformamos ferramentas comuns em motores de eficiência. Devolvemos-lhe o tempo que hoje perde com processos manuais.",
        "mission_title": "Nossa Missão 🛡️",
        "mission_text": "A nossa missão é garantir que a sua empresa não fique para trás na era digital. Acreditamos que a automação e a Inteligência Artificial devem ser acessíveis, permitindo que o seu investimento seja aplicado no desenvolvimento de soluções práticas que geram retorno real, sem a necessidade de licenças de software dispendiosas. 💎",
        "vision_title": "Visão de Futuro 🔮",
        "vision_text": "Ser o parceiro estratégico que simplifica a tecnologia. Queremos que os nossos clientes utilizem a IA e a automação como ferramentas naturais do dia a dia, integradas perfeitamente nas suas operações para potenciar o crescimento.",
        "why_us": "📊 **Porquê nós?**\n\n- Foco em Micro e Pequenas Empresas\n- Uso de Ferramentas que já possui\n- Redução de Erros Humanos\n- ROI em Tempo Real",
        "specialists": "✨ **Especialistas em:**\n- Python & Automação\n- Power Automate\n- Agentes IA Customizados",
        "strat_title": "O Método em 4 Fases ⚡",
        "strat_sub": "Uma abordagem estruturada para garantir resultados sólidos e escaláveis.",
        "p1_title": "1️⃣ Auditoria e Diagnóstico",
        "p1_desc": "Não implementamos soluções sem primeiro compreender o seu negócio. Analisamos o seu fluxo de trabalho atual para identificar onde a tecnologia e a IA podem eliminar tarefas repetitivas e otimizar o tempo da sua equipa.",
        "p2_title": "2️⃣ Arquitetura Digital",
        "p2_desc": "Organizamos a sua infraestrutura utilizando o que já possui (ex: **OneDrive, SharePoint, Google Drive**) e exploramos outras ferramentas gratuitas para alavancar o seu negócio com segurança e ordem.",
        "p3_title": "3️⃣ Desenvolvimento & Implementação",
        "p3_desc": "Damos vida ao projeto com scripts, automações e websites. Utilizamos **Python**, **Power Automate Desktop** e IA de vanguarda para criar soluções que vão desde a triagem de emails até à gestão de bases de dados.",
        "p4_title": "4️⃣ Estabilidade e Formação",
        "p4_desc": "Trabalhamos consigo para garantir que tudo funciona corretamente. Fornecemos formação e consultoria contínua para que a tecnologia seja o suporte sólido de todas as boas práticas da sua empresa.",
        "cat_title": "Catálogo de Soluções",
        "cat_sub": "Soluções de elite com análise personalizada e foco no retorno.",
        "solution_label": "Proposta à Medida",
        "services": [
            {"T": "Website Corporativo + Agente IA", "D": "Um site moderno que funciona como o seu cartão de visita digital e o desenvolvimento de um agente de IA sobre o seu negócio para interagir com os seus visitantes. 🌐"},
            {"T": "Eficiência Cloud & Office 365", "D": "Configuração profissional de permissões e fluxos no Office 365 ou Google Workspace. Acabe com o caos de ficheiros e emails perdidos. ☁️"},
            {"T": "Agentes IA & Scripts de Dados", "D": "Soluções personalizadas para análise de relatórios e grandes volumes de dados, transformando informação bruta em decisões estratégicas. 🧠"},
            {"T": "Automação (Python/Power Automate)", "D": "Criação de robôs e scripts que executam tarefas manuais, integram sistemas e aceleram a operação do seu negócio. 🤖"},
            {"T": "Consultoria e Workshops IA", "D": "Formação prática para a sua equipa aprender a utilizar a IA como ferramenta de produtividade diária. 🎓"},
            {"T": "Suporte Operacional Mensal", "D": "Acesso prioritário para ajustes, correções e consultoria contínua para manter a sua empresa na vanguarda tecnológica. 🛠️"}
        ],
        "lab_title": "Laboratório de Inovação 🧪",
        "lab_sub_title": "Como Usar os Nossos Agentes Gratuitos 🤖",
        "lab_desc": "Disponibilizamos vários Agentes de IA independentes que funcionam como os nossos embaixadores de eficiência.",
        "lab_box_title": "✨ Consultor IA 24/7",
        "lab_box_text": "Temos o prazer de apresentar o nosso novo Consultor de Inteligência Artificial – disponível para si agora!",
        "lab_box_btn": "EXPERIMENTE AQUI (GRÁTIS)",
        "email_proc_title": "📧 Agentes de Processamento por E-mail",
        "email_proc_info": "Basta enviar um e-mail para **ds.consulting.it.geral@gmail.com**. O nosso motor processa os pedidos em ciclos programados e redireciona a resposta analisada para si.",
        "exp1_title": "📊 [ai dados] – O seu Excel com Inteligência",
        "exp1_text": "Envie um ficheiro Excel ou CSV. Inclua no assunto a tag **[ai dados]**.\n**O que recebe:** Um relatório PDF profissional com análise estatística, regressões e gráficos dinâmicos para apoiar a sua estratégia.",
        "exp2_title": "💡 [AI Solutions] – Consultoria Estratégica",
        "exp2_text": "Descreva um problema no corpo do e-mail. Inclua no assunto a tag **[AI Solutions]**.\n**O que recebe:** Um relatório com pontos de melhoria, soluções de baixo custo e formas de impulsionar o seu negócio via IA.",
        "exp3_title": "📑 [AI Reports] – Assistente de Documentos",
        "exp3_text": "Envie PDF, Word ou Texto com uma dúvida. Inclua no assunto a tag **[AI Reports]**.\n**O que recebe:** Um relatório detalhado com a filtragem inteligente da informação, poupando horas de leitura.",
        "footer": "Digital Solutions & Consulting IT | Inteligência em Cada Processo | 2026"
    },
    "🇫🇷 Français": {
        "menu": ["🏠 Accueil", "🎯 Stratégie", "💰 Catalogue", "🧪 Laboratoire"],
        "nav_title": "Navigation Principale:",
        "contact_title": "💡 Contact Direct",
        "home_title": "La technologie au service de votre entreprise 🚀",
        "home_subtitle": "Chez <b>Digital Solutions & Consulting IT</b>, nous transformons les outils ordinaires en moteurs d'efficacité. Nous vous redonnons le temps que vous perdez aujourd'hui dans des processus manuels.",
        "mission_title": "Notre Mission 🛡️",
        "mission_text": "Notre mission est de veiller à ce que votre entreprise ne soit pas laissée pour compte à l'ère numérique. Nous pensons que l'automatisation et l'intelligence artificielle doivent être accessibles, permettant à votre investissement d'être appliqué à des solutions pratiques qui génèrent un retour réel. 💎",
        "vision_title": "Vision d'Avenir 🔮",
        "vision_text": "Être le partenaire stratégique qui simplifie la technologie. Nous voulons que nos clients utilisent l'IA et l'automatisation comme des outils naturels au quotidien.",
        "why_us": "📊 **Pourquoi nous ?**\n\n- Focus TPE & PME\n- Utilisation des outils existants\n- Réduction des erreurs humaines\n- ROI en temps réel",
        "specialists": "✨ **Spécialistes en :**\n- Python & Automatisation\n- Power Automate\n- Agents IA sur mesure",
        "strat_title": "La Méthode en 4 Phases ⚡",
        "strat_sub": "Une approche structurée pour garantir des résultats solides et évolutifs.",
        "p1_title": "1️⃣ Audit & Diagnostic",
        "p1_desc": "Nous n'implémentons pas de solutions sans d'abord comprendre votre entreprise. Nous analysons votre flux de travail actuel pour éliminer les tâches répétitives.",
        "p2_title": "2️⃣ Architecture Numérique",
        "p2_desc": "Nous organisons votre infrastructure en utilisant ce que vous possédez déjà (ex: **OneDrive, SharePoint, Google Drive**).",
        "p3_title": "3️⃣ Développement & Implémentation",
        "p3_desc": "Nous donnons vie au projet avec des scripts, des automatisations et des sites web en utilisant **Python** et **Power Automate Desktop**.",
        "p4_title": "4️⃣ Stabilité & Formation",
        "p4_desc": "Nous travaillons avec vous pour garantir le bon fonctionnement et offrons une formation continue.",
        "cat_title": "Catalogue de Solutions",
        "cat_sub": "Solutions d'élite avec analyse personnalisée.",
        "solution_label": "Sur Mesure",
        "services": [
            {"T": "Site Web d'Entreprise + Agent IA", "D": "Un site moderne servant de carte de visite numérique et un agent IA personnalisé pour vos visiteurs. 🌐"},
            {"T": "Efficacité Cloud & Office 365", "D": "Configuration professionnelle des permissions et flux Office 365 ou Google Workspace. Fin du chaos des fichiers perdus. ☁️"},
            {"T": "Agents IA & Scripts de Données", "D": "Solutions personnalisées pour analyser de grands volumes de données et prendre des décisions stratégiques. 🧠"},
            {"T": "Automatisation (Python/Power Automate)", "D": "Création de robots et scripts exécutant des tâches manuelles et accélérant vos opérations. 🤖"},
            {"T": "Conseil et Ateliers IA", "D": "Formation pratique pour votre équipe afin d'utiliser l'IA comme outil de productivité quotidienne. 🎓"},
            {"T": "Support Opérationnel Mensuel", "D": "Accès prioritaire pour les ajustements et le conseil continu pour rester à la pointe. 🛠️"}
        ],
        "lab_title": "Laboratoire d'Innovation 🧪",
        "lab_sub_title": "Comment utiliser nos agents gratuits 🤖",
        "lab_desc": "Nous proposons plusieurs agents IA indépendants agissant comme ambassadeurs d'efficacité.",
        "lab_box_title": "✨ Consultant IA 24/7",
        "lab_box_text": "Découvrez notre nouveau Consultant en Intelligence Artificielle – disponible dès maintenant !",
        "lab_box_btn": "ESSAYER ICI (GRATUIT)",
        "email_proc_title": "📧 Agents de Traitement par E-mail",
        "email_proc_info": "Envoyez simplement un e-mail à **ds.consulting.it.geral@gmail.com**. Notre moteur traite les demandes et vous renvoie l'analyse.",
        "exp1_title": "📊 [ai data] – Votre Excel Intelligent",
        "exp1_text": "Envoyez un fichier Excel ou CSV avec la balise **[ai data]** dans l'objet.\n**Ce que vous recevez:** Un rapport PDF professionnel avec analyse statistique et graphiques dynamiques.",
        "exp2_title": "💡 [AI Solutions] – Conseil Stratégique",
        "exp2_text": "Décrivez un problème avec la balise **[AI Solutions]** dans l'objet.\n**Ce que vous recevez:** Un rapport avec des pistes d'amélioration et des solutions économiques.",
        "exp3_title": "📑 [AI Reports] – Assistant Documentaire",
        "exp3_text": "Envoyez un PDF, Word ou texte avec une question et la balise **[AI Reports]** dans l'objet.\n**Ce que vous recevez:** Un rapport détaillé avec filtrage intelligent de l'information.",
        "footer": "Digital Solutions & Consulting IT | L'intelligence dans chaque processus | 2026"
    },
    "🇪🇸 Español": {
        "menu": ["🏠 Inicio", "🎯 Estrategia", "💰 Catálogo", "🧪 Laboratorio"],
        "nav_title": "Navegación Principal:",
        "contact_title": "💡 Contacto Directo",
        "home_title": "La tecnología trabajando para tu negocio 🚀",
        "home_subtitle": "En <b>Digital Solutions & Consulting IT</b>, transformamos herramientas comunes en motores de eficiencia. Te devolvemos el tiempo que hoy pierdes con procesos manuales.",
        "mission_title": "Nuestra Misión 🛡️",
        "mission_text": "Nuestra misión es asegurar que tu empresa no se quede atrás en la era digital. Creemos que la automatización y la Inteligencia Artificial deben ser accesibles, permitiendo aplicar tu inversión a soluciones prácticas sin licencias de software costosas. 💎",
        "vision_title": "Visión de Futuro 🔮",
        "vision_text": "Ser el socio estratégico que simplifica la tecnología. Queremos que nuestros clientes utilicen la IA y la automatización como herramientas naturales del día a día.",
        "why_us": "📊 **¿Por qué nosotros?**\n\n- Enfoque en Micro y Pequeñas Empresas\n- Uso de herramientas que ya posees\n- Reducción de errores humanos\n- ROI en tiempo real",
        "specialists": "✨ **Especialistas en:**\n- Python y Automatización\n- Power Automate\n- Agentes de IA Personalizados",
        "strat_title": "El Método en 4 Fases ⚡",
        "strat_sub": "Un enfoque estructurado para garantizar resultados sólidos y escalables.",
        "p1_title": "1️⃣ Auditoría y Diagnóstico",
        "p1_desc": "Analizamos tu flujo de trabajo actual para identificar dónde la tecnología y la IA pueden eliminar tareas repetitivas y optimizar el tiempo de tu equipo.",
        "p2_title": "2️⃣ Arquitectura Digital",
        "p2_desc": "Organizamos tu infraestructura utilizando lo que ya posees (ej: **OneDrive, SharePoint, Google Drive**).",
        "p3_title": "3️⃣ Desarrollo e Implementación",
        "p3_desc": "Damos vida al proyecto con scripts, automatizaciones y sitios web utilizando **Python** y **Power Automate Desktop**.",
        "p4_title": "4️⃣ Estabilidad y Formación",
        "p4_desc": "Trabajamos contigo para asegurar que todo funcione correctamente y ofrecemos formación continua.",
        "cat_title": "Catálogo de Soluciones",
        "cat_sub": "Soluciones de élite con análisis personalizado.",
        "solution_label": "A Medida",
        "services": [
            {"T": "Sitio Web Corporativo + Agente IA", "D": "Un sitio moderno que funciona como tarjeta de visita digital y un agente de IA para interactuar con tus visitantes. 🌐"},
            {"T": "Eficiencia Cloud & Office 365", "D": "Configuración profesional de permisos y flujos en Office 365 o Google Workspace. Termina con el caos de archivos. ☁️"},
            {"T": "Agentes IA & Scripts de Datos", "D": "Soluciones personalizadas para analizar informes y grandes volúmenes de datos en decisiones estratégicas. 🧠"},
            {"T": "Automatización (Python/Power Automate)", "D": "Creación de robots y scripts que ejecutan tareas manuales e integran sistemas. 🤖"},
            {"T": "Consultoría y Talleres de IA", "D": "Formación práctica para que tu equipo aprenda a usar la IA como herramienta de productividad. 🎓"},
            {"T": "Soporte Operacional Mensual", "D": "Acceso prioritario para ajustes, correcciones y consultoría continua. 🛠️"}
        ],
        "lab_title": "Laboratorio de Innovación 🧪",
        "lab_sub_title": "Cómo Usar Nuestros Agentes Gratuitos 🤖",
        "lab_desc": "Ofrecemos varios agentes de IA independientes que actúan como embajadores de eficiencia.",
        "lab_box_title": "✨ Consultor IA 24/7",
        "lab_box_text": "Presentamos nuestro nuevo Consultor de Inteligencia Artificial – ¡disponible para ti ahora!",
        "lab_box_btn": "PRUÉBALO AQUÍ (GRATIS)",
        "email_proc_title": "📧 Agentes de Procesamiento por Correo",
        "email_proc_info": "Envía un correo a **ds.consulting.it.geral@gmail.com**. Nuestro motor procesa las solicitudes y te devuelve la respuesta analizada.",
        "exp1_title": "📊 [ai data] – Tu Excel con Inteligencia",
        "exp1_text": "Envía un archivo Excel o CSV con la etiqueta **[ai data]** en el asunto.\n**Lo que recibes:** Un informe PDF profesional con análisis estadístico y gráficos dinámicos.",
        "exp2_title": "💡 [AI Solutions] – Consultoría Estratégica",
        "exp2_text": "Describe un problema con la etiqueta **[AI Solutions]** en el asunto.\n**Lo que recibes:** Un informe con puntos de mejora y soluciones de bajo coste.",
        "exp3_title": "📑 [AI Reports] – Asistente de Documentos",
        "exp3_text": "Envía PDF, Word o Texto con una duda y la etiqueta **[AI Reports]** en el asunto.\n**Lo que recibes:** Un informe detallado con filtrado inteligente de información.",
        "footer": "Digital Solutions & Consulting IT | Inteligencia en Cada Proceso | 2026"
    },
    "🇮🇹 Italiano": {
        "menu": ["🏠 Inizio", "🎯 Strategia", "💰 Catalogo", "🧪 Laboratorio"],
        "nav_title": "Navigazione Principale:",
        "contact_title": "💡 Contatto Diretto",
        "home_title": "La tecnologia al lavoro per la tua azienda 🚀",
        "home_subtitle": "In <b>Digital Solutions & Consulting IT</b>, trasformiamo gli strumenti comuni in motori di efficienza. Ti restituiamo il tempo che oggi perdi con i processi manuali.",
        "mission_title": "La Nostra Missione 🛡️",
        "mission_text": "La nostra missione è garantire che la tua azienda non rimanga indietro nell'era digitale. Crediamo che l'automazione e l'Intelligenza Artificiale debbano essere accessibili, generando un ritorno reale senza licenze software costose. 💎",
        "vision_title": "Visione Futura 🔮",
        "vision_text": "Essere il partner strategico che semplifica la tecnologia. Vogliamo che i nostri clienti utilizzino l'IA e l'automazione come strumenti naturali quotidiani.",
        "why_us": "📊 **Perché noi?**\n\n- Focus su Micro e Piccole Imprese\n- Uso di strumenti già posseduti\n- Riduzione degli errori umani\n- ROI in tempo reale",
        "specialists": "✨ **Specialisti in:**\n- Python & Automazione\n- Power Automate\n- Agenti IA Personalizzati",
        "strat_title": "Il Metodo in 4 Fasi ⚡",
        "strat_sub": "Un approccio strutturato per garantire risultati solidi e scalabili.",
        "p1_title": "1️⃣ Audit e Diagnosi",
        "p1_desc": "Analizziamo il tuo flusso di lavoro attuale per identificare dove la tecnologia e l'IA possono eliminare le attività ripetitive.",
        "p2_title": "2️⃣ Architettura Digitale",
        "p2_desc": "Organizziamo la tua infrastruttura utilizzando ciò che già possiedi (es: **OneDrive, SharePoint, Google Drive**).",
        "p3_title": "3️⃣ Sviluppo e Implementazione",
        "p3_desc": "Diamo vita al progetto con script, automazioni e siti web utilizzando **Python** e **Power Automate Desktop**.",
        "p4_title": "4️⃣ Stabilità e Formazione",
        "p4_desc": "Lavoriamo con te per garantire il corretto funzionamento e forniamo formazione continua.",
        "cat_title": "Catalogo Soluzioni",
        "cat_sub": "Soluzioni d'élite con analisi personalizzata.",
        "solution_label": "Analisi Personalizzata",
        "services": [
            {"T": "Sito Web Aziendale + Agente IA", "D": "Un sito moderno che funge da biglietto da visita digitale e un agente IA per interagire con i tuoi visitatori. 🌐"},
            {"T": "Efficienza Cloud & Office 365", "D": "Configurazione professionale di permessi e flussi in Office 365 o Google Workspace. Stop al caos dei file persi. ☁️"},
            {"T": "Agenti IA & Script di Dati", "D": "Soluzioni personalizzate per analizzare report e grandi volumi di dati in decisioni strategiche. 🧠"},
            {"T": "Automazione (Python/Power Automate)", "D": "Creazione di robot e script che eseguono attività manuali e accelerano le operazioni aziendali. 🤖"},
            {"T": "Consulenza e Workshop IA", "D": "Formazione pratica per il tuo team per imparare a usare l'IA come strumento di produttività giornaliera. 🎓"},
            {"T": "Supporto Operativo Mensile", "D": "Accesso prioritario per modifiche, correzioni e consulenza continua. 🛠️"}
        ],
        "lab_title": "Laboratorio di Innovazione 🧪",
        "lab_sub_title": "Come Usare i Nostri Agenti Gratuiti 🤖",
        "lab_desc": "Mettiamo a disposizione diversi Agenti IA indipendenti che fungono da ambasciatori di efficienza.",
        "lab_box_title": "✨ Consulente IA 24/7",
        "lab_box_text": "Siamo lieti di presentare il nostro nuovo Consulente di Intelligenza Artificiale – disponibile ora per te!",
        "lab_box_btn": "PROVALO QUI (GRATIS)",
        "email_proc_title": "📧 Agenti di Elaborazione Email",
        "email_proc_info": "Invia un'email a **ds.consulting.it.geral@gmail.com**. Il nostro motore elabora le richieste e reindirizza la risposta analizzata.",
        "exp1_title": "📊 [ai data] – Il tuo Excel con Intelligenza",
        "exp1_text": "Invia un file Excel o CSV con il tag **[ai data]** nell'oggetto.\n**Cosa ricevi:** Un report PDF professionale con analisi statistica e grafici dinamici.",
        "exp2_title": "💡 [AI Solutions] – Consulenza Strategica",
        "exp2_text": "Descrivi un problema nel corpo dell'email con il tag **[AI Solutions]** nell'oggetto.\n**Cosa ricevi:** Un report con punti di miglioramento e soluzioni a basso costo.",
        "exp3_title": "📑 [AI Reports] – Assistente Documenti",
        "exp3_text": "Invia PDF, Word o Testo con un dubbio e il tag **[AI Reports]** nell'oggetto.\n**Cosa ricevi:** Un report dettagliato con filtraggio intelligente delle informazioni.",
        "footer": "Digital Solutions & Consulting IT | Intelligenza in Ogni Processo | 2026"
    }
}

# 3. BARRA LATERAL (BRANDING, LÍNGUA & CONTACTOS)
with st.sidebar:
    # Seletor de Língua no topo da barra lateral com bandeiras (Inglês pré-selecionado)
    selected_lang = st.selectbox(
        "🌐 Language / Idioma / Langue", 
        ["🇬🇧 English", "🇵🇹 Português", "🇫🇷 Français", "🇪🇸 Español", "🇮🇹 Italiano"],
        index=0 
    )
    
    t = translations[selected_lang]

    st.markdown("---")
    try:
        st.image("IMG_6163.jpeg", use_container_width=True)
    except:
        st.markdown(f"### **Digital Solutions & Consulting IT**")
    
    st.markdown("---")
    
    # Gestão de Navegação com base na língua selecionada
    if 'menu_option' not in st.session_state:
        st.session_state.menu_option = t["menu"][0]
    else:
        # Sincroniza a opção atual caso mude de idioma
        current_idx = 0
        for i, m in enumerate(translations["🇬🇧 English"]["menu"]):
            if st.session_state.menu_option in [translations[lang]["menu"][i] for lang in translations]:
                current_idx = i
                break
        st.session_state.menu_option = t["menu"][current_idx]

    st.radio(t["nav_title"], t["menu"], key="menu_option")

    st.markdown("---")
    st.markdown(f"### {t['contact_title']}")
    st.write("📩 [ds.consulting.it@outlook.com](mailto:ds.consulting.it@outlook.com)")
    st.markdown("[🔗 LinkedIn Institucional](https://www.linkedin.com/company/digital-solutions-consulting-it/)")
    
    st.caption("© 2026 Digital Solutions & Consulting IT")

# --- PÁGINA 1: INÍCIO E MISSÃO ---
if st.session_state.menu_option == t["menu"][0]:
    st.markdown(f'<h1 class="stTitle">{t["home_title"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<p class="subtitle">{t["home_subtitle"]}</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f'<h2 class="section-header">{t["mission_title"]}</h2>', unsafe_allow_html=True)
        st.markdown(f"{t['mission_text']}")
        
        st.markdown(f'<h2 class="section-header">{t["vision_title"]}</h2>', unsafe_allow_html=True)
        st.markdown(f"{t['vision_text']}")
    
    with col2:
        st.info(t["why_us"])
        st.success(t["specialists"])

# --- PÁGINA 2: ESTRATÉGIA ---
elif st.session_state.menu_option == t["menu"][1]:
    st.markdown(f'<h1 class="stTitle">{t["strat_title"]}</h1>', unsafe_allow_html=True)
    st.write(t["strat_sub"])

    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown(f"### {t['p1_title']}")
        st.write(t["p1_desc"])
        
        st.markdown(f"### {t['p2_title']}")
        st.write(t["p2_desc"])

    with col_b:
        st.markdown(f"### {t['p3_title']}")
        st.write(t["p3_desc"])
        
        st.markdown(f"### {t['p4_title']}")
        st.write(t["p4_desc"])

# --- PÁGINA 3: CATÁLOGO ---
elif st.session_state.menu_option == t["menu"][2]:
    st.markdown(f'<h1 class="stTitle">{t["cat_title"]}</h1>', unsafe_allow_html=True)
    st.write(t["cat_sub"])

    servicos = t["services"]

    cols = st.columns(2)
    for idx, s in enumerate(servicos):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="service-card">
                <h3 style="color:#1e40af;">{s['T']}</h3>
                <p><span style="color:#2563eb; font-size:1.1em; font-weight:600;">✨ {t['solution_label']}</span></p>
                <p style="color:#475569;">{s['D']}</p>
            </div><br>
            """, unsafe_allow_html=True)

# --- PÁGINA 4: LABORATÓRIO ---
elif st.session_state.menu_option == t["menu"][3]:
    st.markdown(f'<h1 class="stTitle">{t["lab_title"]}</h1>', unsafe_allow_html=True)
    st.markdown(f"### {t['lab_sub_title']}")
    st.write(t["lab_desc"])

    st.markdown(f"""
    <div class="lab-box">
        <h4>{t['lab_box_title']}</h4>
        <p>{t['lab_box_text']}</p>
        <a href="https://agente-ia-digital-solutions-consulting-it.streamlit.app/" style="color:white; font-weight:bold; text-decoration:underline;">{t['lab_box_btn']}</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"#### {t['email_proc_title']}")
    st.info(t["email_proc_info"])

    with st.expander(t["exp1_title"]):
        st.write(t["exp1_text"])

    with st.expander(t["exp2_title"]):
        st.write(t["exp2_text"])

    with st.expander(t["exp3_title"]):
        st.write(t["exp3_text"])

st.markdown("---")
st.markdown(f'<div class="footer">{t["footer"]}</div>', unsafe_allow_html=True)
