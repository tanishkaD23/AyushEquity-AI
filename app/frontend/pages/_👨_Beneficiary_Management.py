from database import get_beneficiaries

df = get_beneficiaries()
import streamlit as st
import pandas as pd
import sqlite3


st.title("👨 Beneficiary Management")

# ==========================
# DATABASE CONNECTION
# ==========================

conn = sqlite3.connect("app/database/database.db")

df = pd.read_sql(
    "SELECT * FROM Beneficiaries",
    conn
)

conn.close()
tab1, tab2, tab3 = st.tabs([
    "Beneficiaries",
    "Add Beneficiary",
    "Analytics"
])
with tab2:

    st.subheader("➕ Add Beneficiary")

    with st.form("add_beneficiary"):

        name = st.text_input("Name")

        age = st.number_input("Age",18,100)

        gender = st.selectbox(
            "Gender",
            ["Male","Female"]
        )

        income = st.number_input(
            "Monthly Income"
        )

        submit = st.form_submit_button("Save")

        if submit:

            st.success("Beneficiary Added")

# ==========================
# SEARCH
# ==========================

st.subheader("🔍 Search Beneficiary")

search = st.text_input(
    "Search by Beneficiary ID, Name, Aadhaar or Mobile"
)

if search:

    search = search.lower()

    df = df[
        df.astype(str)
        .apply(lambda x: x.str.lower())
        .apply(
            lambda row: row.str.contains(search).any(),
            axis=1
        )
    ]

# ==========================
# FILTERS
# ==========================

st.subheader("🎯 Filters")

c1, c2, c3, c4 = st.columns(4)

with c1:

    state = st.selectbox(
        "State",
        ["All"] + sorted(df["State"].unique().tolist())
    )

with c2:

    gender = st.selectbox(
        "Gender",
        ["All"] + sorted(df["Gender"].unique().tolist())
    )

with c3:

    occupation = st.selectbox(
        "Occupation",
        ["All"] + sorted(df["Occupation"].unique().tolist())
    )

with c4:

    eligible = st.selectbox(
        "Eligibility",
        ["All"] + sorted(df["Eligible"].unique().tolist())
    )

# ==========================
# APPLY FILTERS
# ==========================

filtered_df = df.copy()

if state != "All":

    filtered_df = filtered_df[
        filtered_df["State"] == state
    ]

if gender != "All":

    filtered_df = filtered_df[
        filtered_df["Gender"] == gender
    ]

if occupation != "All":

    filtered_df = filtered_df[
        filtered_df["Occupation"] == occupation
    ]

if eligible != "All":

    filtered_df = filtered_df[
        filtered_df["Eligible"] == eligible
    ]

# ==========================
# DASHBOARD SUMMARY
# ==========================

st.subheader("📊 Summary")

c1, c2, c3, c4 = st.columns(4)

with c1:

    st.metric(
        "Total",
        len(filtered_df)
    )

with c2:

    st.metric(
        "Eligible",
        len(
            filtered_df[
                filtered_df["Eligible"] == "Yes"
            ]
        )
    )

with c3:

    st.metric(
        "Not Eligible",
        len(
            filtered_df[
                filtered_df["Eligible"] == "No"
            ]
        )
    )

with c4:

    st.metric(
        "Average Income",
        f"₹{int(filtered_df['Annual_Income'].mean()):,}"
    )

# ==========================
# TABLE
# ==========================

st.subheader("📋 Beneficiary Records")

columns = [

    "Beneficiary_ID",

    "Name",

    "Age",

    "Gender",

    "Occupation",

    "State",

    "District",

    "Annual_Income",

    "Eligible"

]

st.dataframe(

    filtered_df[columns],

    use_container_width=True,

    hide_index=True

)

# ==========================
# DOWNLOAD CSV
# ==========================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(

    "⬇ Download CSV",

    csv,

    "beneficiaries.csv",

    "text/csv"

)
import requests

st.divider()

st.subheader("👤 Beneficiary Profile")

beneficiary_ids = filtered_df["Beneficiary_ID"].tolist()

selected_id = st.selectbox(
    "Select Beneficiary",
    beneficiary_ids
)

selected = filtered_df[
    filtered_df["Beneficiary_ID"] == selected_id
].iloc[0]

c1, c2 = st.columns(2)

with c1:

    st.markdown("### Personal Information")

    st.write(f"**Name:** {selected['Name']}")
    st.write(f"**Age:** {selected['Age']}")
    st.write(f"**Gender:** {selected['Gender']}")
    st.write(f"**Occupation:** {selected['Occupation']}")
    st.write(f"**Family Size:** {selected['Family_Size']}")

with c2:

    st.markdown("### Scheme Information")

    st.write(f"**State:** {selected['State']}")
    st.write(f"**District:** {selected['District']}")
    st.write(f"**Annual Income:** ₹{selected['Annual_Income']:,}")
    st.write(f"**PMJAY Registered:** {selected['PMJAY_Registered']}")
    st.write(f"**Eligible:** {selected['Eligible']}")
# ==========================
# ACTION BUTTONS
# ==========================

col1, col2 = st.columns(2)

with col1:

    if st.button("✏ Edit Beneficiary"):

        st.info("Edit Beneficiary Feature Coming Soon")

with col2:

    if st.button("🗑 Delete Beneficiary"):

        st.warning("Delete Beneficiary Feature Coming Soon")
        with st.form("edit_form"):

         name = st.text_input(
        "Name",
        selected["Name"]
    )

    age = st.number_input(
        "Age",
        value=int(selected["Age"])
    )

    occupation = st.text_input(
        "Occupation",
        selected["Occupation"]
    )

    income = st.number_input(
        "Monthly Income",
        value=int(selected["Monthly_Income"])
    )

    submit = st.form_submit_button(
        "Update Beneficiary"
    )

    if submit:

        conn = sqlite3.connect(
            "app/database/database.db"
        )

        cursor = conn.cursor()

        cursor.execute("""

        UPDATE Beneficiaries

        SET

        Name=?,

        Age=?,

        Occupation=?,

        Monthly_Income=?

        WHERE Beneficiary_ID=?

        """,

        (

        name,

        age,

        occupation,

        income,

        selected_id

        )

        )

        conn.commit()

        conn.close()

        st.success("Beneficiary Updated Successfully")
        with st.form("edit_form"):

         name = st.text_input(
        "Name",
        selected["Name"]
    )

    age = st.number_input(
        "Age",
        value=int(selected["Age"])
    )

    occupation = st.text_input(
        "Occupation",
        selected["Occupation"]
    )

    income = st.number_input(
        "Monthly Income",
        value=int(selected["Monthly_Income"])
    )

    submit = st.form_submit_button(
        "Update Beneficiary"
    )

    if submit:

        conn = sqlite3.connect(
            "app/database/database.db"
        )

        cursor = conn.cursor()

        cursor.execute("""

        UPDATE Beneficiaries

        SET

        Name=?,

        Age=?,

        Occupation=?,

        Monthly_Income=?

        WHERE Beneficiary_ID=?

        """,

        (

        name,

        age,

        occupation,

        income,

        selected_id

        )

        )

        conn.commit()

        conn.close()

        st.success("Beneficiary Updated Successfully")
        st.divider()

st.subheader("Delete Beneficiary")
if st.button("🗑 Delete"):

    conn = sqlite3.connect(
        "app/database/database.db"
    )

    cursor = conn.cursor()

    cursor.execute(

    """

    DELETE FROM Beneficiaries

    WHERE Beneficiary_ID=?

    """,

    (

    selected_id,

    )

    )

    conn.commit()

    conn.close()

    st.success("Beneficiary Deleted")
st.divider()

st.subheader("🤖 AI Eligibility Prediction")

if st.button("Predict Eligibility"):

    payload = {

        "Age": int(selected["Age"]),

        "Gender": selected["Gender"],

        "Monthly_Income": int(selected["Monthly_Income"]),

        "Annual_Income": int(selected["Annual_Income"]),

        "Family_Size": int(selected["Family_Size"]),

        "BPL_Status": selected["BPL_Status"],

        "Ration_Card": selected["Ration_Card"],

        "Disability": selected["Disability"],

        "Chronic_Disease": selected["Chronic_Disease"],

        "PMJAY_Registered": selected["PMJAY_Registered"],

        "Occupation": selected["Occupation"],

        "State": selected["State"]

    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict/inclusion",
            json=payload
        )

        if response.status_code == 200:

            result = response.json()

            prediction = result.get("Prediction", "Unknown")
            confidence = result.get("Confidence", "N/A")

            if prediction == "Eligible":

                st.success(f"✅ Prediction : {prediction}")

            else:

                st.error(f"❌ Prediction : {prediction}")

            st.info(f"Confidence : {confidence}")

        else:

            st.error(response.text)

    except Exception:

        st.error("FastAPI server is not running.")