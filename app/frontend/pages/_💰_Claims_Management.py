import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

import streamlit as st



st.title("💰 Claims Management")

    # rest of code

# ==========================================
# LOAD DATABASE
# ==========================================

conn = sqlite3.connect("app/database/database.db")

claims_df = pd.read_sql("SELECT * FROM Claims", conn)

beneficiary_df = pd.read_sql("SELECT * FROM Beneficiaries", conn)

hospital_df = pd.read_sql("SELECT * FROM Hospitals", conn)

conn.close()

# ==========================================
# KPI CARDS
# ==========================================

st.subheader("📊 Dashboard Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Total Claims",
        len(claims_df)
    )

with c2:

    approved = len(
        claims_df[
            claims_df["Status"]=="Approved"
        ]
    ) if "Status" in claims_df.columns else 0

    st.metric(
        "Approved",
        approved
    )

with c3:

    pending = len(
        claims_df[
            claims_df["Status"]=="Pending"
        ]
    ) if "Status" in claims_df.columns else 0

    st.metric(
        "Pending",
        pending
    )

with c4:

    fraud = len(
        claims_df[
            claims_df["Fraud_Label"]=="Yes"
        ]
    )

    st.metric(
        "Fraud Claims",
        fraud
    )

# ==========================================
# SEARCH
# ==========================================

st.divider()

st.subheader("🔍 Search Claims")

search = st.text_input(
    "Search by Claim ID / Beneficiary ID / Hospital ID"
)

filtered_df = claims_df.copy()

if search:

    search = search.lower()

    filtered_df = filtered_df[
        filtered_df.astype(str)
        .apply(lambda x: x.str.lower())
        .apply(
            lambda row: row.str.contains(search).any(),
            axis=1
        )
    ]

# ==========================================
# FILTERS
# ==========================================

st.subheader("🎯 Filters")

c1,c2,c3,c4 = st.columns(4)

with c1:

    disease = st.selectbox(

        "Disease",

        ["All"]+

        sorted(

            filtered_df["Disease"].unique().tolist()

        )

    )

with c2:

    duplicate = st.selectbox(

        "Duplicate Claim",

        ["All"]+

        sorted(

            filtered_df["Duplicate_Claim"].unique().tolist()

        )

    )

with c3:

    fraud_filter = st.selectbox(

        "Fraud",

        ["All"]+

        sorted(

            filtered_df["Fraud_Label"].unique().tolist()

        )

    )

with c4:

    if "Status" in filtered_df.columns:

        status = st.selectbox(

            "Status",

            ["All"]+

            sorted(

                filtered_df["Status"].unique().tolist()

            )

        )

    else:

        status = "All"

# ==========================================
# APPLY FILTERS
# ==========================================

if disease!="All":

    filtered_df = filtered_df[
        filtered_df["Disease"]==disease
    ]

if duplicate!="All":

    filtered_df = filtered_df[
        filtered_df["Duplicate_Claim"]==duplicate
    ]

if fraud_filter!="All":

    filtered_df = filtered_df[
        filtered_df["Fraud_Label"]==fraud_filter
    ]

if status!="All":

    filtered_df = filtered_df[
        filtered_df["Status"]==status
    ]

# ==========================================
# CLAIMS TABLE
# ==========================================

st.divider()

st.subheader("📋 Claims")

display_columns = [

    "Claim_ID",

    "Beneficiary_ID",

    "Hospital_ID",

    "Disease",

    "Treatment",

    "Claim_Amount",

    "Fraud_Label"

]

if "Status" in filtered_df.columns:

    display_columns.append("Status")

st.dataframe(

    filtered_df[display_columns],

    use_container_width=True,

    hide_index=True

)

# ==========================================
# SELECT CLAIM
# ==========================================

st.divider()

st.subheader("📄 Select Claim")

selected_claim = st.selectbox(

    "Claim ID",

    filtered_df["Claim_ID"]

)

selected = filtered_df[

    filtered_df["Claim_ID"]==selected_claim

].iloc[0]
# ==========================================
# CLAIM DETAILS
# ==========================================

st.divider()

st.subheader("📄 Claim Details")

c1, c2 = st.columns(2)

with c1:

    st.write(f"**Claim ID:** {selected['Claim_ID']}")
    st.write(f"**Disease:** {selected['Disease']}")
    st.write(f"**Treatment:** {selected['Treatment']}")
    st.write(f"**Claim Amount:** ₹{selected['Claim_Amount']:,}")
    st.write(f"**Package Amount:** ₹{selected['Package_Amount']:,}")

with c2:

    st.write(f"**Admission Date:** {selected['Admission_Date']}")
    st.write(f"**Discharge Date:** {selected['Discharge_Date']}")
    st.write(f"**Duplicate Claim:** {selected['Duplicate_Claim']}")
    st.write(f"**Fraud Label:** {selected['Fraud_Label']}")

# ==========================================
# BENEFICIARY DETAILS
# ==========================================

st.divider()

st.subheader("👤 Beneficiary Details")

beneficiary = beneficiary_df[
    beneficiary_df["Beneficiary_ID"] == selected["Beneficiary_ID"]
].iloc[0]

c1, c2 = st.columns(2)

with c1:

    st.write(f"**Name:** {beneficiary['Name']}")
    st.write(f"**Age:** {beneficiary['Age']}")
    st.write(f"**Gender:** {beneficiary['Gender']}")
    st.write(f"**Occupation:** {beneficiary['Occupation']}")

with c2:

    st.write(f"**State:** {beneficiary['State']}")
    st.write(f"**District:** {beneficiary['District']}")
    st.write(f"**Annual Income:** ₹{beneficiary['Annual_Income']:,}")
    st.write(f"**Eligible:** {beneficiary['Eligible']}")

# ==========================================
# HOSPITAL DETAILS
# ==========================================

st.divider()

st.subheader("🏥 Hospital Details")

hospital = hospital_df[
    hospital_df["Hospital_ID"] == selected["Hospital_ID"]
].iloc[0]

c1, c2 = st.columns(2)

with c1:

    st.write(f"**Hospital:** {hospital['Hospital_Name']}")
    st.write(f"**Type:** {hospital['Hospital_Type']}")
    st.write(f"**Beds:** {hospital['Beds']}")
    st.write(f"**Doctors:** {hospital['Doctors']}")

with c2:

    st.write(f"**Rating:** ⭐ {hospital['Rating']}")
    st.write(f"**PMJAY:** {hospital['PMJAY_Empanelled']}")
    st.write(f"**Previous Fraud:** {hospital['Previous_Fraud']}")

# ==========================================
# AI FRAUD DETECTION
# ==========================================

import requests

st.divider()

st.subheader("🤖 AI Fraud Detection")

if st.button("🚨 Detect Fraud"):

    payload = {

        "Claim_Amount": float(selected["Claim_Amount"]),

        "Package_Amount": float(selected["Package_Amount"]),

        "Duplicate_Claim": selected["Duplicate_Claim"],

        "Disease": selected["Disease"],

        "Treatment": selected["Treatment"],

        "Hospital_Type": hospital["Hospital_Type"],

        "Previous_Fraud": hospital["Previous_Fraud"],

        "Beds": int(hospital["Beds"]),

        "Doctors": int(hospital["Doctors"]),

        "Rating": float(hospital["Rating"]),

        "Length_of_Stay": (
            pd.to_datetime(selected["Discharge_Date"])
            -
            pd.to_datetime(selected["Admission_Date"])
        ).days,

        "Claim_Ratio": float(
            selected["Claim_Amount"]
        ) / float(
            selected["Package_Amount"]
        ),

        "High_Claim": 1 if float(selected["Claim_Amount"]) > 450000 else 0,

        "Fraud_Hospital": 1 if hospital["Previous_Fraud"]=="Yes" else 0,

        "Doctor_Bed_Ratio":
            float(hospital["Doctors"]) /
            float(hospital["Beds"]),

        "Claim_Per_Bed":
            float(selected["Claim_Amount"]) /
            float(hospital["Beds"]),

        "Claim_Difference":
            float(selected["Claim_Amount"]) -
            float(selected["Package_Amount"])

    }

    try:

        response = requests.post(

            "http://127.0.0.1:8000/predict/fraud",

            json=payload

        )

        if response.status_code == 200:

            result = response.json()

            prediction = result.get("Prediction","Unknown")
            confidence = result.get("Confidence","N/A")

            if prediction == "Fraud":

                st.error(f"🚨 {prediction}")

            else:

                st.success(f"✅ {prediction}")

            st.info(f"Confidence : {confidence}")

        else:

            st.error(response.text)

    except Exception:

        st.error("FastAPI server is not running.")

# ==========================================
# APPROVE / REJECT CLAIM
# ==========================================

st.divider()

st.subheader("📝 Officer Decision")

c1, c2 = st.columns(2)

with c1:

    if st.button("✅ Approve Claim"):

        conn = sqlite3.connect(
            "app/database/database.db"
        )

        cursor = conn.cursor()

        cursor.execute(

            """

            UPDATE Claims

            SET Status='Approved'

            WHERE Claim_ID=?

            """,

            (selected_claim,)

        )

        conn.commit()

        conn.close()

        st.success("Claim Approved Successfully")

with c2:

    if st.button("❌ Reject Claim"):

        conn = sqlite3.connect(
            "app/database/database.db"
        )

        cursor = conn.cursor()

        cursor.execute(

            """

            UPDATE Claims

            SET Status='Rejected'

            WHERE Claim_ID=?

            """,

            (selected_claim,)

        )

        conn.commit()

        conn.close()

        st.success("Claim Rejected Successfully")
with c2:

    if st.button("❌ Reject Claim"):

        conn = sqlite3.connect(
            "app/database/database.db"
        )

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE Claims
            SET Status='Rejected'
            WHERE Claim_ID=?
            """,
            (selected_claim,)
        )

        conn.commit()
        conn.close()

        st.success("Claim Rejected Successfully")        