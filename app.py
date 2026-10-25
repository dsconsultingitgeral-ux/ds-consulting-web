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
