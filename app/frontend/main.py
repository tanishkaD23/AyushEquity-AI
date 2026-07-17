import streamlit as st

import officer_dashboard
import beneficiary_page
import hospital_page
import claims_page
import fraud_page
import analytics_page
import citizen_portal
import reports_page
import settings

st.set_page_config(
    page_title="AyushEquity AI",
    layout="wide",
    page_icon="🏥"
)

st.sidebar.title("🏥 AyushEquity AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Beneficiaries",
        "Hospitals",
        "Claims",
        "Fraud",
        "Analytics",
        "Citizen Portal",
        "Reports",
        "Settings"
    ]
)

if page == "Dashboard":
    officer_dashboard.show()

elif page == "Beneficiaries":
    beneficiary_page.show()

elif page == "Hospitals":
    hospital_page.show()

elif page == "Claims":
    claims_page.show()

elif page == "Fraud":
    fraud_page.show()

elif page == "Analytics":
    analytics_page.show()

elif page == "Citizen Portal":
    citizen_portal.show()

elif page == "Reports":
    reports_page.show()

elif page == "Settings":
    settings.show()