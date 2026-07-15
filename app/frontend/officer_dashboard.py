import streamlit as st
from streamlit_option_menu import option_menu
from components import *
from styles import load_css

dashboard_header()

dashboard_metrics()
command_center()
analytics_dashboard()
dashboard_bottom()
dashboard_footer()
# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="AyushEquity AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------

st.markdown("""
<style>

.main{
    background-color:#F5F9FF;
}

section[data-testid="stSidebar"]{
    background:#0F52BA;
}

section[data-testid="stSidebar"] *{
    color:white;
}

.dashboard-title{
    font-size:34px;
    color:#0F52BA;
    font-weight:bold;
}

.subtitle{
    color:gray;
    font-size:18px;
}

.card{

    background:white;

    padding:20px;

    border-radius:15px;

    box-shadow:0px 4px 10px rgba(0,0,0,0.1);

    border-left:8px solid #00C853;

    text-align:center;

}

.metric{

    font-size:30px;

    color:#0F52BA;

    font-weight:bold;

}

.label{

    color:gray;

    font-size:18px;

}

</style>
""",unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.image(
        "app/assets/logo.png",
        width=120
    )

    st.markdown("# AyushEquity AI")

    selected = option_menu(

        menu_title="Navigation",

        options=[

            "Dashboard",

            "Beneficiaries",

            "Hospitals",

            "Claims",

            "Eligibility",

            "Fraud",

            "Analytics",

            "Map",

            "Reports",

            "Settings"

        ],

        icons=[

            "house",

            "people",

            "hospital",

            "cash",

            "robot",

            "shield-exclamation",

            "bar-chart",

            "geo-alt",

            "file-earmark",

            "gear"

        ],

        default_index=0

    )

# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<p class="dashboard-title">🏥 AyushEquity AI Officer Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">AI-powered Healthcare Inclusion & Fraud Detection System</p>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------
# KPI Cards
# -----------------------------

col1,col2,col3,col4,col5 = st.columns(5)

with col1:

    st.markdown("""
    <div class="card">

        <div class="metric">10,000</div>

        <div class="label">Beneficiaries</div>

    </div>
    """,unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card">

        <div class="metric">500</div>

        <div class="label">Hospitals</div>

    </div>
    """,unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="card">

        <div class="metric">50,000</div>

        <div class="label">Claims</div>

    </div>
    """,unsafe_allow_html=True)

with col4:

    st.markdown("""
    <div class="card">

        <div class="metric">8,234</div>

        <div class="label">Eligible</div>

    </div>
    """,unsafe_allow_html=True)

with col5:

    st.markdown("""
    <div class="card">

        <div class="metric">1,432</div>

        <div class="label">Fraud Cases</div>

    </div>
    """,unsafe_allow_html=True)

st.write("")

st.success("✅ System Running Successfully")

st.info("🤖 AI Models Connected")

st.warning("⚠ 12 High Risk Claims Detected")

st.write("")

st.subheader("Dashboard Overview")

st.write("""
Welcome to the AyushEquity AI Officer Dashboard.

Use the sidebar to navigate between:

- Beneficiary Management
- Fraud Detection
- Eligibility Prediction
- Claims
- Reports
- Analytics
- GIS Map

""")