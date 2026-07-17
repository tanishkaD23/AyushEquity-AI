import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

import streamlit as st



st.title("🚨 Fraud Investigation")

    # rest of code
# ==========================================
# LOAD DATABASE
# ==========================================

conn = sqlite3.connect(
    "app/database/database.db"
)

claims_df = pd.read_sql(
    "SELECT * FROM Claims",
    conn
)

hospital_df = pd.read_sql(
    "SELECT * FROM Hospitals",
    conn
)

beneficiary_df = pd.read_sql(
    "SELECT * FROM Beneficiaries",
    conn
)

conn.close()

# ==========================================
# DASHBOARD CARDS
# ==========================================

st.subheader("📊 Dashboard Summary")

c1,c2,c3,c4 = st.columns(4)

with c1:

    st.metric(
        "Total Claims",
        len(claims_df)
    )

with c2:

    fraud = len(
        claims_df[
            claims_df["Fraud_Label"]=="Yes"
        ]
    )

    st.metric(
        "Fraud Claims",
        fraud
    )

with c3:

    duplicate = len(
        claims_df[
            claims_df["Duplicate_Claim"]=="Yes"
        ]
    )

    st.metric(
        "Duplicate Claims",
        duplicate
    )

with c4:

    high = len(
        claims_df[
            claims_df["Claim_Amount"]>400000
        ]
    )

    st.metric(
        "High Value Claims",
        high
    )

# ==========================================
# SEARCH
# ==========================================

st.divider()

st.subheader("🔍 Search")

search = st.text_input(
    "Search Claim ID / Hospital ID / Beneficiary ID"
)

filtered_df = claims_df.copy()

if search:

    search = search.lower()

    filtered_df = filtered_df[
        filtered_df.astype(str)
        .apply(lambda x:x.str.lower())
        .apply(
            lambda row:
            row.str.contains(search).any(),
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

            filtered_df["Disease"].unique()

        )

    )

with c2:

    duplicate = st.selectbox(

        "Duplicate",

        ["All"]+

        sorted(

            filtered_df["Duplicate_Claim"].unique()

        )

    )

with c3:

    fraud = st.selectbox(

        "Fraud",

        ["All"]+

        sorted(

            filtered_df["Fraud_Label"].unique()

        )

    )

with c4:

    if "Status" in filtered_df.columns:

        status = st.selectbox(

            "Status",

            ["All"]+

            sorted(

                filtered_df["Status"].unique()

            )

        )

    else:

        status="All"

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

if fraud!="All":

    filtered_df = filtered_df[
        filtered_df["Fraud_Label"]==fraud
    ]

if status!="All":

    filtered_df = filtered_df[
        filtered_df["Status"]==status
    ]

# ==========================================
# FRAUD TABLE
# ==========================================

st.divider()

st.subheader("🚨 Fraud Claims")

display = [

    "Claim_ID",

    "Beneficiary_ID",

    "Hospital_ID",

    "Disease",

    "Claim_Amount",

    "Duplicate_Claim",

    "Fraud_Label"

]

if "Status" in filtered_df.columns:

    display.append("Status")

st.dataframe(

    filtered_df[display],

    use_container_width=True,

    hide_index=True

)

# ==========================================
# SELECT CLAIM
# ==========================================

st.divider()

st.subheader("🔎 Select Claim")

selected_claim = st.selectbox(

    "Claim ID",

    filtered_df["Claim_ID"]

)

selected = filtered_df[
    filtered_df["Claim_ID"]==selected_claim
].iloc[0]
# ==========================================
# CLAIM INVESTIGATION
# ==========================================

st.divider()

st.header("🔍 Claim Investigation")

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
# BENEFICIARY PROFILE
# ==========================================

st.divider()

st.header("👤 Beneficiary Profile")

beneficiary = beneficiary_df[
    beneficiary_df["Beneficiary_ID"] == selected["Beneficiary_ID"]
].iloc[0]

c1, c2 = st.columns(2)

with c1:

    st.write(f"**Name:** {beneficiary['Name']}")
    st.write(f"**Age:** {beneficiary['Age']}")
    st.write(f"**Gender:** {beneficiary['Gender']}")
    st.write(f"**Occupation:** {beneficiary['Occupation']}")
    st.write(f"**Family Size:** {beneficiary['Family_Size']}")

with c2:

    st.write(f"**State:** {beneficiary['State']}")
    st.write(f"**District:** {beneficiary['District']}")
    st.write(f"**Annual Income:** ₹{beneficiary['Annual_Income']:,}")
    st.write(f"**Eligible:** {beneficiary['Eligible']}")

# ==========================================
# HOSPITAL PROFILE
# ==========================================

st.divider()

st.header("🏥 Hospital Profile")

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
# AI FRAUD PREDICTION
# ==========================================

import requests
import plotly.graph_objects as go

st.divider()

st.header("🤖 AI Fraud Prediction")

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

        "Claim_Ratio":
            float(selected["Claim_Amount"]) /
            float(selected["Package_Amount"]),

        "High_Claim":
            1 if float(selected["Claim_Amount"]) > 450000 else 0,

        "Fraud_Hospital":
            1 if hospital["Previous_Fraud"]=="Yes" else 0,

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
            confidence = result.get("Confidence",95)

            if prediction=="Fraud":

                st.error(f"🚨 {prediction}")

                risk = 95

            else:

                st.success(f"✅ {prediction}")

                risk = 20

            st.info(f"Confidence : {confidence}")

            # ==================================
            # RISK GAUGE
            # ==================================

            st.subheader("📊 Risk Meter")

            fig = go.Figure(

                go.Indicator(

                    mode="gauge+number",

                    value=risk,

                    title={"text":"Fraud Risk (%)"},

                    gauge={

                        "axis":{"range":[0,100]},

                        "bar":{"color":"red"},

                        "steps":[

                            {"range":[0,30],"color":"green"},

                            {"range":[30,70],"color":"yellow"},

                            {"range":[70,100],"color":"red"}

                        ]

                    }

                )

            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:

            st.error(response.text)

    except Exception:

        st.error("FastAPI server is not running.")
        # ==========================================
# EXPLAINABLE AI
# ==========================================

st.divider()

st.header("🧠 Explainable AI")

reasons = []

if selected["Duplicate_Claim"] == "Yes":
    reasons.append("✔ Duplicate Claim Detected")

if float(selected["Claim_Amount"]) > 450000:
    reasons.append("✔ High Claim Amount")

if hospital["Previous_Fraud"] == "Yes":
    reasons.append("✔ Hospital has Previous Fraud History")

stay = (
    pd.to_datetime(selected["Discharge_Date"])
    -
    pd.to_datetime(selected["Admission_Date"])
).days

if stay <= 2:
    reasons.append("✔ Very Short Hospital Stay")

claim_ratio = (
    float(selected["Claim_Amount"])
    /
    float(selected["Package_Amount"])
)

if claim_ratio > 1:
    reasons.append("✔ Claim exceeds Package Amount")

if len(reasons) == 0:
    st.success("No suspicious indicators detected.")

else:

    for r in reasons:

        st.warning(r)

# ==========================================
# OFFICER RECOMMENDATION
# ==========================================

st.divider()

st.header("👮 Officer Recommendation")

if len(reasons) >= 4:

    st.error("🚨 HIGH RISK")

    st.write("Recommended Actions")

    st.write("✔ Freeze Claim")

    st.write("✔ Notify Senior Officer")

    st.write("✔ Audit Hospital")

    st.write("✔ Verify Documents")

elif len(reasons) >= 2:

    st.warning("⚠ MEDIUM RISK")

    st.write("Recommended Actions")

    st.write("✔ Manual Verification")

    st.write("✔ Recheck Beneficiary")

    st.write("✔ Verify Hospital Records")

else:

    st.success("🟢 LOW RISK")

    st.write("Recommended Actions")

    st.write("✔ Approve Claim")

    st.write("✔ Continue Monitoring")

# ==========================================
# PREVIOUS FRAUD HISTORY
# ==========================================

st.divider()

st.header("📜 Previous Fraud History")

history = claims_df[

    claims_df["Hospital_ID"] == selected["Hospital_ID"]

]

fraud_history = history[
    history["Fraud_Label"]=="Yes"
]

c1,c2,c3 = st.columns(3)

with c1:

    st.metric(
        "Previous Claims",
        len(history)
    )

with c2:

    st.metric(
        "Fraud Claims",
        len(fraud_history)
    )

with c3:

    if len(history)>0:

        rate = len(fraud_history)/len(history)*100

    else:

        rate=0

    st.metric(
        "Fraud Rate",
        f"{rate:.2f}%"
    )

# ==========================================
# CLAIM TIMELINE
# ==========================================

st.divider()

st.header("📅 Investigation Timeline")

timeline = pd.DataFrame({

    "Stage":[

        "Admission",

        "Treatment",

        "Discharge",

        "Claim Submitted",

        "AI Screening",

        "Officer Review"

    ],

    "Status":[

        "Completed",

        "Completed",

        "Completed",

        "Completed",

        "Completed",

        "Pending"

    ]

})

st.table(timeline)

# ==========================================
# FRAUD ANALYTICS
# ==========================================

st.divider()

st.header("📊 Fraud Analytics")

tab1,tab2 = st.tabs(

    [

        "Disease",

        "Hospital"

    ]

)

with tab1:

    disease = claims_df[
        claims_df["Fraud_Label"]=="Yes"
    ]

    disease = disease.groupby(
        "Disease"
    ).size().reset_index(name="Frauds")

    fig = px.bar(

        disease,

        x="Disease",

        y="Frauds",

        color="Frauds",

        title="Fraud by Disease"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with tab2:

    hospital_chart = claims_df[
        claims_df["Fraud_Label"]=="Yes"
    ]

    hospital_chart = hospital_chart.groupby(

        "Hospital_ID"

    ).size().reset_index(name="Frauds")

    fig = px.bar(

        hospital_chart,

        x="Hospital_ID",

        y="Frauds",

        color="Frauds",

        title="Fraud by Hospital"

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ==========================================
# EXPORT REPORT
# ==========================================

st.divider()

st.header("📥 Export Report")

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(

    "⬇ Download Fraud Report",

    csv,

    "fraud_report.csv",

    "text/csv"

)

# ==========================================
# SUMMARY
# ==========================================

st.divider()

st.success("✅ Fraud Investigation Completed Successfully")