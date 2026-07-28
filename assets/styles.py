"""
SalesAI – global CSS injected via st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
Dark gradient theme with glassmorphism elements.
"""

CUSTOM_CSS = """
<style>
/* -- Google Fonts -- */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* -- Base -- */
html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    color: #ffffff !important;
}

/* -- Hide Streamlit chrome -- */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }

/* -- App background – solid gradient (no image) -- */
.stApp {
    background: linear-gradient(135deg, #0a0f1a 0%, #1a1f2e 50%, #0d1117 100%);
    background-attachment: fixed;
    background-repeat: no-repeat;
    min-height: 100vh;
}

/* -- Main content padding -- */
.main .block-container {
    padding: 1.5rem 2.5rem 3rem;
    max-width: 1400px;
}

/* -- Page title -- */
h1 {
    font-family: 'Outfit', sans-serif !important;
    font-size: 2.2rem !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    letter-spacing: -0.04em !important;
    margin-bottom: 0.2rem !important;
    text-shadow: 0 2px 20px rgba(100, 150, 255, 0.4) !important;
}

/* -- Section headers -- */
h2, h3 {
    font-family: 'Outfit', sans-serif !important;
    color: #ffffff !important;
    letter-spacing: -0.02em !important;
    text-shadow: 0 1px 8px rgba(0,0,0,0.5) !important;
}

/* -- General text / labels -- */
p, label, .stMarkdown, .stText {
    color: #ffffff !important;
}

/* -- Nav buttons: PRIMARY (active) – dark gradient pill style -- */
.stButton > button[kind="primary"],
.stButton > button[data-testid="baseButton-primary"] {
    background: linear-gradient(135deg, #1a2332 0%, #2d3f55 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 20px !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    height: 2.8em !important;
    box-shadow: 0 4px 20px rgba(26,35,50,0.6) !important;
}

/* -- Nav buttons: SECONDARY (inactive) – transparent pill style -- */
.stButton > button[kind="secondary"],
.stButton > button[data-testid="baseButton-secondary"] {
    background: rgba(255,255,255,0.05) !important;
    color: #ffffff !important;
    border: 1.5px solid rgba(255,255,255,0.2) !important;
    border-radius: 20px !important;
    font-weight: 700 !important;
    font-size: 0.85rem !important;
    height: 2.8em !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
}

.stButton > button[kind="secondary"]:hover,
.stButton > button[data-testid="baseButton-secondary"]:hover {
    background: rgba(255,255,255,0.15) !important;
    color: #ffffff !important;
    border-color: rgba(255,255,255,0.3) !important;
}

/* -- Force text inside secondary buttons to white -- */
.stButton > button[kind="secondary"] p,
.stButton > button[kind="secondary"] span,
.stButton > button[data-testid="baseButton-secondary"] p,
.stButton > button[data-testid="baseButton-secondary"] span {
    color: #ffffff !important;
}

/* -- Divider -- */
hr { border-color: rgba(255,255,255,0.2) !important; margin: 0.6rem 0 1rem !important; }

/* -- KPI metric tiles – glassmorphism -- */
.kpi-tile {
    background: rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    box-shadow: 0 4px 24px rgba(0,0,0,0.3);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}

/* -- Selectbox / date selector – glassmorphism -- */
.stSelectbox > div > div {
    background: rgba(255,255,255,0.08) !important;
    border-radius: 10px !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #ffffff !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
}

.stSelectbox label {
    color: #ffffff !important;
    font-weight: 600 !important;
}

.stSelectbox [data-baseweb="select"] span {
    color: #ffffff !important;
}

/* -- Plotly chart frame – rounded corners with shadow -- */
.stPlotlyChart {
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(0,0,0,0.3);
    background: rgba(15, 20, 35, 0.5);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
}

/* -- Streamlit info/warning/error boxes -- */
.stAlert {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 12px !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    color: #ffffff !important;
}

/* -- Metric values -- */
[data-testid="stMetricValue"] {
    color: #ffffff !important;
}

[data-testid="stMetricLabel"] {
    color: #d0d8e0 !important;
}

/* -- Streamlit tabs -- */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
}

.stTabs [data-baseweb="tab"] {
    color: #ffffff !important;
    font-weight: 600 !important;
}

.stTabs [aria-selected="true"] {
    color: #ffffff !important;
    border-bottom-color: #4fc3f7 !important;
}

/* -- Streamlit tab panel background -- */
.stTabs [data-baseweb="tab-panel"] {
    background: transparent !important;
}
</style>
"""

def get_css() -> str:
    """Return the global CSS stylesheet."""
    return CUSTOM_CSS
