import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Beneficiary Statistics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Beneficiary Statistics Dashboard")

conn = sqlite3.connect("app/database/database.db")

beneficiaries = pd.read_sql(
    "SELECT * FROM Beneficiaries",
    conn
)

claims = pd.read_sql(
    "SELECT * FROM Claims",
    conn
)

hospitals = pd.read_sql(
    "SELECT * FROM Hospitals",
    conn
)

conn.close()

total_beneficiaries = len(beneficiaries)

eligible = len(
    beneficiaries[
        beneficiaries["Eligible"] == "Yes"
    ]
)

not_eligible = len(
    beneficiaries[
        beneficiaries["Eligible"] == "No"
    ]
)

pmjay = len(
    beneficiaries[
        beneficiaries["PMJAY_Registered"] == "Yes"
    ]
)

disabled = len(
    beneficiaries[
        beneficiaries["Disability"] == "Yes"
    ]
)

chronic = len(
    beneficiaries[
        beneficiaries["Chronic_Disease"] == "Yes"
    ]
)

total_claims = len(claims)

fraud = len(
    claims[
        claims["Fraud_Label"] == "Yes"
    ]
)

total_hospitals = len(hospitals)

st.subheader("📌 Dashboard Summary")

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.metric(
        "Beneficiaries",
        total_beneficiaries
    )

with c2:
    st.metric(
        "Hospitals",
        total_hospitals
    )

with c3:
    st.metric(
        "Claims",
        total_claims
    )

with c4:
    st.metric(
        "Fraud Cases",
        fraud
    )

st.write("")

c5,c6,c7,c8 = st.columns(4)

with c5:
    st.metric(
        "Eligible",
        eligible
    )

with c6:
    st.metric(
        "Not Eligible",
        not_eligible
    )

with c7:
    st.metric(
        "PMJAY Registered",
        pmjay
    )

with c8:
    st.metric(
        "Disabled",
        disabled
    )

st.write("")

c9,c10 = st.columns(2)

with c9:
    st.metric(
        "Chronic Disease",
        chronic
    )

with c10:
    st.metric(
        "Average Annual Income",
        f"₹{int(beneficiaries['Annual_Income'].mean()):,}"
    )

st.divider()

left,right = st.columns(2)

with left:

    state_chart = (
        beneficiaries
        .groupby("State")
        .size()
        .reset_index(name="Beneficiaries")
    )

    fig1 = px.bar(
        state_chart,
        x="State",
        y="Beneficiaries",
        color="Beneficiaries",
        title="Beneficiaries by State"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with right:

    fig2 = px.pie(
        beneficiaries,
        names="Eligible",
        title="Eligibility Distribution",
        hole=0.55
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

left,right = st.columns(2)

with left:

    fig3 = px.histogram(
        beneficiaries,
        x="Annual_Income",
        nbins=20,
        title="Income Distribution"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

with right:

    gender = (
        beneficiaries
        .groupby("Gender")
        .size()
        .reset_index(name="Count")
    )

    fig4 = px.bar(
        gender,
        x="Gender",
        y="Count",
        color="Gender",
        title="Gender Distribution"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

st.divider()

st.subheader("🏆 Top 10 States")

top_states = (
    beneficiaries
    .groupby("State")
    .size()
    .reset_index(name="Beneficiaries")
    .sort_values(
        by="Beneficiaries",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    top_states,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.subheader("🏥 Hospital Statistics")

hospital_stats = hospitals[
    [
        "Hospital_Name",
        "State",
        "Beds",
        "Doctors",
        "Rating"
    ]
]

st.dataframe(
    hospital_stats,
    use_container_width=True,
    hide_index=True
)

st.divider()

st.success("Dashboard Updated Successfully")