import streamlit as st
import sqlite3
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(
    page_title="Beneficiary Map",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Beneficiary Location Map")

conn = sqlite3.connect("app/database/database.db")

df = pd.read_sql(
    "SELECT * FROM Beneficiaries",
    conn
)

conn.close()

st.sidebar.header("Filters")

state = st.sidebar.selectbox(
    "State",
    ["All"] + sorted(df["State"].dropna().unique().tolist())
)

eligible = st.sidebar.selectbox(
    "Eligibility",
    ["All"] + sorted(df["Eligible"].dropna().unique().tolist())
)

if state != "All":
    df = df[df["State"] == state]

if eligible != "All":
    df = df[df["Eligible"] == eligible]

st.metric(
    "Beneficiaries Showing",
    len(df)
)

india_map = folium.Map(
    location=[22.97, 78.65],
    zoom_start=5,
    tiles="CartoDB Positron"
)

for _, row in df.iterrows():

    if pd.isna(row["Latitude"]) or pd.isna(row["Longitude"]):
        continue

    color = "green"

    if row["Eligible"] == "No":
        color = "red"

    popup = f"""
    <b>{row['Name']}</b><br>
    ID : {row['Beneficiary_ID']}<br>
    State : {row['State']}<br>
    District : {row['District']}<br>
    Occupation : {row['Occupation']}<br>
    Annual Income : ₹{row['Annual_Income']}<br>
    Eligible : {row['Eligible']}
    """

    folium.Marker(
        location=[
            row["Latitude"],
            row["Longitude"]
        ],
        popup=popup,
        tooltip=row["Name"],
        icon=folium.Icon(
            color=color,
            icon="user",
            prefix="fa"
        )
    ).add_to(india_map)

st_folium(
    india_map,
    width=1400,
    height=700
)