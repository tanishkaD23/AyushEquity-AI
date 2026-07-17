import streamlit as st

st.set_page_config(
    page_title="AyushEquity AI",
    page_icon="🏥",
    layout="wide"
)

st.title("🏥 AyushEquity AI")

st.subheader("PM-JAY Healthcare Inclusion Platform")

st.info("👈 Select a page from the sidebar.")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Beneficiaries", "10,000")
col2.metric("Hospitals", "500")
col3.metric("Claims", "50,000")
col4.metric("Frauds", "2,500")

st.success("Welcome Officer 👋")