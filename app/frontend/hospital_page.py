import streamlit as st
import pandas as pd
import sqlite3
import requests
import folium
from streamlit_folium import st_folium
import streamlit as st

def show():

    st.title("🏥 Hospital Management")


conn = sqlite3.connect(
    "app/database/database.db"
)

hospital_df = pd.read_sql(

"SELECT * FROM Hospitals",

conn

)

claims_df = pd.read_sql(

"SELECT * FROM Claims",

conn

)

conn.close()
c1,c2,c3,c4 = st.columns(4)

c1.metric(

"Total Hospitals",

len(hospital_df)

)

c2.metric(

"PMJAY",

len(

hospital_df[

hospital_df["PMJAY_Empanelled"]=="Yes"

]

)

)

c3.metric(

"Private",

len(

hospital_df[

hospital_df["Hospital_Type"]=="Private"

]

)

)

c4.metric(

"Fraud Hospitals",

len(

hospital_df[

hospital_df["Previous_Fraud"]=="Yes"

]

)

)
search = st.text_input(

"Search Hospital"

)

if search:

    hospital_df = hospital_df[

    hospital_df["Hospital_Name"]

    .str.contains(

    search,

    case=False

    )

    ]
    c1,c2,c3 = st.columns(3)

state = c1.selectbox(

"State",

["All"]

+

sorted(

hospital_df["State"].unique()

)

)

hospital = c2.selectbox(

"Hospital Type",

["All"]

+

sorted(

hospital_df["Hospital_Type"].unique()

)

)

fraud = c3.selectbox(

"Fraud History",

["All","Yes","No"]

)
if state!="All":

    hospital_df = hospital_df[

    hospital_df["State"]==state

    ]

if hospital!="All":

    hospital_df = hospital_df[

    hospital_df["Hospital_Type"]==hospital

    ]

if fraud!="All":

    hospital_df = hospital_df[

    hospital_df["Previous_Fraud"]==fraud

    ]
    st.dataframe(

hospital_df,

use_container_width=True

)
    selected = st.selectbox(

"Hospital",

hospital_df["Hospital_Name"]

)

profile = hospital_df[

hospital_df["Hospital_Name"]==selected

].iloc[0]
c1,c2 = st.columns(2)

with c1:

    st.write(

    "### Hospital Information"

    )

    st.write(

    profile["Hospital_Name"]

    )

    st.write(

    profile["Hospital_Type"]

    )

    st.write(

    profile["Beds"]

    )

    st.write(

    profile["Doctors"]

    )

with c2:

    st.write(

    "### Performance"

    )

    st.write(

    profile["Rating"]

    )

    st.write(

    profile["PMJAY_Empanelled"]

    )

    st.write(

    profile["Previous_Fraud"]

    )
    claims = claims_df[

claims_df["Hospital_ID"]

==

profile["Hospital_ID"]

]
import plotly.graph_objects as go

st.subheader("⭐ Hospital Rating")

fig = go.Figure(go.Indicator(

    mode="gauge+number",

    value=profile["Rating"],

    title={"text":"Hospital Rating"},

    gauge={

        "axis":{"range":[0,5]},

        "bar":{"color":"green"},

        "steps":[

            {"range":[0,2],"color":"red"},

            {"range":[2,4],"color":"yellow"},

            {"range":[4,5],"color":"lightgreen"}

        ]

    }

))

st.plotly_chart(
    fig,
    use_container_width=True
)   

st.subheader(

"Claims"

)

st.dataframe(

claims
)
fraud_claims = claims[

claims["Fraud_Label"]=="Yes"

]

st.metric(

"Fraud Claims",

len(

fraud_claims

))
st.subheader("🚨 Top Fraud Hospitals")

conn = sqlite3.connect(
    "app/database/database.db"
)

top = pd.read_sql("""

SELECT

Hospital_Name,

COUNT(*) AS Fraud_Cases

FROM Claims

JOIN Hospitals

ON Claims.Hospital_ID = Hospitals.Hospital_ID

WHERE Fraud_Label='Yes'

GROUP BY Hospital_Name

ORDER BY Fraud_Cases DESC

LIMIT 10

""",conn)

conn.close()
import plotly.express as px

claims_df["Admission_Date"] = pd.to_datetime(
    claims_df["Admission_Date"]
)

claims_df["Month"] = claims_df["Admission_Date"].dt.month_name()

fraud = claims_df[
    claims_df["Fraud_Label"]=="Yes"
]

trend = fraud.groupby(
    "Month"
).size().reset_index(name="Fraud Cases")

fig = px.line(

    trend,

    x="Month",

    y="Fraud Cases",

    markers=True,

    title="Monthly Fraud Trend"

)

st.plotly_chart(
    fig,
    use_container_width=True
)
district = claims_df.merge(

hospital_df,

on="Hospital_ID"

)

district = district[
district["Fraud_Label"]=="Yes"
]

district = district.groupby(
"District"
).size().reset_index(name="Frauds")

fig = px.bar(

district,

x="District",

y="Frauds",

color="Frauds"

)

st.plotly_chart(
fig,
use_container_width=True
)

st.dataframe(top,use_container_width=True)


if profile["Previous_Fraud"]=="Yes":

    st.error(

    "High Risk Hospital"

    )
st.subheader("🤖 AI Recommendation")

if profile["Previous_Fraud"]=="Yes":

    st.error("🚨 High Risk Hospital")

    st.write("### Recommended Actions")

    st.write("✔ Conduct Financial Audit")

    st.write("✔ Verify Claims")

    st.write("✔ Suspend High Value Claims")

    st.write("✔ Notify District Officer")

    st.write("✔ Monitor Future Transactions")

else:

    st.success("✅ Low Risk Hospital")

    st.write("### Recommendation")

    st.write("✔ Continue Monitoring")

    st.write("✔ Eligible for PMJAY")

    st.write("✔ Good Performance")  
    st.subheader("📍 Nearby Beneficiaries")

conn = sqlite3.connect(
"app/database/database.db"
)

beneficiaries = pd.read_sql(

"SELECT * FROM Beneficiaries",

conn

)

conn.close()

beneficiaries["Distance"] = (

(

beneficiaries["Latitude"]

-

profile["Latitude"]

)**2

+

(

beneficiaries["Longitude"]

-

profile["Longitude"]

)**2

)**0.5

nearby = beneficiaries.sort_values(
"Distance"
).head(10)

st.dataframe(

nearby[

[

"Beneficiary_ID",

"Name",

"Village",

"District",

"Distance"

]

],

use_container_width=True
) 
c1,c2,c3 = st.columns(3)

c1.metric(

"Total Claims",

len(claims)

)

c2.metric(

"Fraud Claims",

len(fraud_claims)

)

c3.metric(

"Fraud Rate",

f"{len(fraud_claims)/len(claims)*100:.2f}%"

if len(claims)>0 else "0%"

)

st.success(

    "Low Risk Hospital"

    )
m = folium.Map(

location=[

profile["Latitude"],

profile["Longitude"]

],

zoom_start=8

)

folium.Marker(

[

profile["Latitude"],

profile["Longitude"]

],

popup=profile["Hospital_Name"]

).add_to(m)

st_folium(

m,

width=900

)
csv = hospital_df.to_csv(

index=False

).encode("utf-8")

st.download_button(

"Download CSV",

csv,

"hospitals.csv",

"text/csv"

)