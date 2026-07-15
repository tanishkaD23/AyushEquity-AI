import streamlit as st
from datetime import datetime


def dashboard_header():

    col1, col2 = st.columns([1, 6])

    with col1:
     st.image("app/assets/logo.png", width=80)

     with col2:
        st.markdown(
            """
            <div class='dashboard-title'>
            🏥 AyushEquity AI
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class='dashboard-subtitle'>
            AI Powered Healthcare Inclusion & Fraud Detection Platform
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()


def dashboard_footer():

    st.divider()

    st.markdown(
        """
        <div class='footer'>
        © 2026 AyushEquity AI | Government Healthcare Intelligence Platform
        </div>
        """,
        unsafe_allow_html=True,
    )


def current_datetime():

    now = datetime.now()

    return now.strftime("%d %B %Y | %I:%M:%S %p")
def metric_card(title, value, change, icon):

    st.markdown(
        f"""
        <div class="metric-card">

            <div style="font-size:40px;">
                {icon}
            </div>

            <div class="metric-title">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div class="metric-change">
                ▲ {change}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def dashboard_metrics():

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        metric_card(
            "Beneficiaries",
            "10,000",
            "12%",
            "👨‍👩‍👧"
        )

    with c2:
        metric_card(
            "Hospitals",
            "500",
            "5%",
            "🏥"
        )

    with c3:
        metric_card(
            "Claims",
            "50,000",
            "18%",
            "💰"
        )

    with c4:
        metric_card(
            "Eligible Families",
            "8,234",
            "8%",
            "✅"
        )

    st.write("")

    c5, c6, c7, c8 = st.columns(4)

    with c5:
        metric_card(
            "Fraud Cases",
            "1,432",
            "2%",
            "🚨"
        )

    with c6:
        metric_card(
            "Blockchain Records",
            "50,000",
            "100%",
            "⛓️"
        )

    with c7:
        metric_card(
            "AI Predictions",
            "18,562",
            "16%",
            "🤖"
        )

    with c8:
        metric_card(
            "API Requests",
            "95,430",
            "28%",
            "⚡"
        )
def fraud_alert_panel():

    st.markdown(
        """
        <div class="danger-card">

            <h3>🚨 Live Fraud Alerts</h3>

            <hr>

            <b>Hospital :</b> City Care Hospital <br><br>

            <b>Claim ID :</b> CLM004523 <br><br>

            <b>Risk Score :</b> 99.42% <br><br>

            <b>Status :</b>
            <span class="status-offline">
            Immediate Investigation Required
            </span>

        </div>
        """,
        unsafe_allow_html=True
    )


def ai_recommendation_panel():

    st.markdown(
        """
        <div class="ai-card">

            <h3>🤖 AI Recommendations</h3>

            <hr>

            ✅ Enroll 245 new beneficiaries from Gwalior.<br><br>

            🚨 Audit 3 hospitals with abnormal claim patterns.<br><br>

            📈 Fraud increased by 8% this week.<br><br>

            🏥 PM-JAY registrations are low in Morena.<br><br>

            🔍 Review duplicate claims from District Hospital.

        </div>
        """,
        unsafe_allow_html=True
    )


def blockchain_status_panel():

    st.markdown(
        """
        <div class="block-card">

            <h3>⛓ Blockchain Network</h3>

            <hr>

            Latest Block : <b>#10528</b><br><br>

            Transactions : <b>50,000</b><br><br>

            Hash Verified : ✅<br><br>

            Network Status :

            <span style="color:white;font-weight:bold;">
            ACTIVE
            </span>

        </div>
        """,
        unsafe_allow_html=True
    )


def system_health_panel():

    st.markdown(
        """
        <div class="section-card">

        <h3>🖥 System Health</h3>

        <hr>

        🟢 FastAPI Server <br><br>

        🟢 SQLite Database <br><br>

        🟢 Inclusion Model Loaded <br><br>

        🟢 Fraud Model Loaded <br><br>

        🟢 AI Agents Active <br><br>

        🟢 Blockchain Running

        </div>
        """,
        unsafe_allow_html=True
    )


def command_center():

    col1, col2 = st.columns([2,2])

    with col1:

        fraud_alert_panel()

        st.write("")

        blockchain_status_panel()

    with col2:

        ai_recommendation_panel()

        st.write("")

        system_health_panel() 
import plotly.express as px
import pandas as pd


def analytics_dashboard():

    st.markdown("## 📊 AI Analytics Dashboard")

    state_data = pd.DataFrame({
        "State": [
            "MP",
            "UP",
            "Maharashtra",
            "Rajasthan",
            "Gujarat",
            "Bihar"
        ],
        "Beneficiaries": [
            1800,
            2400,
            1650,
            1300,
            1200,
            1650
        ]
    })

    fraud_data = pd.DataFrame({
        "Category": [
            "Fraud",
            "Genuine"
        ],
        "Cases": [
            1432,
            48568
        ]
    })

    claims_data = pd.DataFrame({
        "Month": [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun"
        ],
        "Claims": [
            6200,
            7100,
            7600,
            8450,
            9100,
            9800
        ]
    })

    hospital_data = pd.DataFrame({
        "Hospital": [
            "City Care",
            "Apollo",
            "AIIMS",
            "District",
            "Metro"
        ],
        "Fraud Cases": [
            72,
            41,
            18,
            56,
            29
        ]
    })

    c1, c2 = st.columns(2)

    with c1:

        fig1 = px.bar(
            state_data,
            x="State",
            y="Beneficiaries",
            color="Beneficiaries",
            title="Beneficiaries by State"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with c2:

        fig2 = px.pie(
            fraud_data,
            names="Category",
            values="Cases",
            hole=0.55,
            title="Fraud Distribution"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    c3, c4 = st.columns(2)

    with c3:

        fig3 = px.line(
            claims_data,
            x="Month",
            y="Claims",
            markers=True,
            title="Monthly Claims"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    with c4:

        fig4 = px.bar(
            hospital_data,
            x="Hospital",
            y="Fraud Cases",
            color="Fraud Cases",
            title="Top Fraud Hospitals"
        )

        st.plotly_chart(
            fig4,
            use_container_width=True
        )        
import streamlit as st
import pandas as pd
import time
from datetime import datetime


def live_clock():

    current = datetime.now().strftime("%d %B %Y | %I:%M:%S %p")

    st.markdown(
        f"""
        <div class="section-card">

        <h3>🕒 Current Time</h3>

        <h2 style="color:#1565C0;">{current}</h2>

        </div>
        """,
        unsafe_allow_html=True
    )


def notifications_panel():

    st.markdown(
        """
        <div class="warning-card">

        <h3>🔔 Notifications</h3>

        <hr>

        📌 25 new beneficiaries added.<br><br>

        🚨 12 new fraud cases detected.<br><br>

        🏥 Hospital audit scheduled tomorrow.<br><br>

        🤖 AI model updated successfully.

        </div>
        """,
        unsafe_allow_html=True
    )


def recent_claims():

    st.subheader("📄 Recent Claims")

    data = pd.DataFrame({

        "Claim ID":[
            "CLM1001",
            "CLM1002",
            "CLM1003",
            "CLM1004",
            "CLM1005"
        ],

        "Hospital":[
            "Apollo",
            "City Care",
            "AIIMS",
            "Metro",
            "District"
        ],

        "Amount":[
            65000,
            120000,
            45000,
            98000,
            71000
        ],

        "Status":[
            "Approved",
            "Fraud",
            "Approved",
            "Pending",
            "Fraud"
        ]

    })

    st.dataframe(
        data,
        use_container_width=True
    )


def global_search():

    st.subheader("🔍 Global Search")

    search = st.text_input(
        "Search Beneficiary, Hospital, Claim..."
    )

    if search:

        st.success(
            f"Searching for : {search}"
        )


def reports_section():

    st.subheader("📥 Download Reports")

    c1,c2,c3 = st.columns(3)

    with c1:

        st.download_button(

            "⬇ Beneficiary Report",

            data="Beneficiary Report",

            file_name="beneficiaries.csv"

        )

    with c2:

        st.download_button(

            "⬇ Fraud Report",

            data="Fraud Report",

            file_name="fraud.csv"

        )

    with c3:

        st.download_button(

            "⬇ Claims Report",

            data="Claims Report",

            file_name="claims.csv"

        )


def user_profile():

    st.markdown(
        """
        <div class="section-card">

        <h3>👤 Logged In Officer</h3>

        <hr>

        Name : Admin Officer<br><br>

        Role : PM-JAY Administrator<br><br>

        Department : Healthcare Ministry<br><br>

        Access : Full

        </div>
        """,
        unsafe_allow_html=True
    )


def dashboard_bottom():

    c1,c2 = st.columns(2)

    with c1:

        live_clock()

        st.write("")

        notifications_panel()

    with c2:

        user_profile()

    st.write("")

    global_search()

    st.write("")

    recent_claims()

    st.write("")

    reports_section()

    st.write("")

    st.markdown(
        """
        <div class="footer">

        © 2026 AyushEquity AI

        AI Powered Healthcare Inclusion & Fraud Detection Platform

        </div>
        """,
        unsafe_allow_html=True
    )