import streamlit as st



st.title("⚙ Settings")

    # rest of code

theme = st.selectbox(
    "Theme",
    [
        "Light",
        "Dark"
    ]
)

st.write("Current Theme:", theme)

st.success("Database Connected")

st.success("FastAPI Running")

st.success("Models Loaded")

st.button("Logout")