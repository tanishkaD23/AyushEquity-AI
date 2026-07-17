import streamlit as st
import requests
import pandas as pd

def show():

    st.title("🏥 AyushEquity AI")

    st.subheader("PM-JAY Healthcare Inclusion Platform")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        [
            "🏠 Home",
            "🔍 Check Eligibility",
            "📝 Apply",
            "📊 Track Status",
            "🏥 Nearby Hospitals",
            "📞 Contact"
        ]
    )

    # ==========================================
    # HOME
    # ==========================================

    with tab1:

        st.image(
            "https://images.unsplash.com/photo-1586773860418-d37222d8fce3?w=1200",
            use_container_width=True
        )

        st.write("""
### Welcome to AyushEquity AI

AyushEquity AI helps citizens to:

✔ Check PM-JAY Eligibility

✔ Apply Online

✔ Track Application

✔ Find Nearby Hospitals

✔ Get Healthcare Support
""")

        col1, col2, col3 = st.columns(3)

        col1.metric("Hospitals", 500)

        col2.metric("Beneficiaries", 10000)

        col3.metric("States", 10)

    # ==========================================
    # ELIGIBILITY
    # ==========================================

    with tab2:

        st.header("🔍 Eligibility Checker")

        age = st.number_input(
            "Age",
            1,
            100
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

        income = st.number_input(
            "Monthly Income",
            0
        )

        family = st.number_input(
            "Family Size",
            1,
            20
        )

        bpl = st.selectbox(
            "BPL Status",
            [
                "Yes",
                "No"
            ]
        )

        ration = st.selectbox(
            "Ration Card",
            [
                "Yes",
                "No"
            ]
        )

        disability = st.selectbox(
            "Disability",
            [
                "Yes",
                "No"
            ]
        )

        disease = st.selectbox(
            "Chronic Disease",
            [
                "Yes",
                "No"
            ]
        )

        pmjay = st.selectbox(
            "PMJAY Registered",
            [
                "Yes",
                "No"
            ]
        )

        occupation = st.selectbox(
            "Occupation",
            [
                "Farmer",
                "Labourer",
                "Driver",
                "Student",
                "Tailor",
                "Others"
            ]
        )

        state = st.selectbox(
            "State",
            [
                "Madhya Pradesh",
                "Maharashtra",
                "Uttar Pradesh",
                "Gujarat"
            ]
        )
            # ==========================================
    # APPLY
    # ==========================================

    with tab3:

        st.header("📝 Apply for PM-JAY")

        name = st.text_input("Full Name")

        aadhaar = st.text_input("Aadhaar Number")

        mobile = st.text_input("Mobile Number")

        village = st.text_input("Village")

        district = st.text_input("District")

        apply_state = st.selectbox(
            "State",
            [
                "Madhya Pradesh",
                "Maharashtra",
                "Gujarat",
                "Uttar Pradesh"
            ],
            key="apply_state"
        )

        if st.button("Submit Application"):

            st.success("✅ Application Submitted Successfully!")

            st.balloons()

    # ==========================================
    # TRACK STATUS
    # ==========================================

    with tab4:

        st.header("📊 Track Application")

        application_id = st.text_input(
            "Enter Application ID"
        )

        if st.button("Track"):

            st.success("Application Status")

            st.info("✔ Verification Completed")

            st.info("✔ Eligibility Verified")

            st.warning("⏳ Waiting for Officer Approval")

    # ==========================================
    # NEARBY HOSPITALS
    # ==========================================

    with tab5:

        st.header("🏥 Nearby Hospitals")

        hospitals = pd.DataFrame({

            "Hospital":[

                "AIIMS Bhopal",

                "MITS Hospital",

                "City Care",

                "Apollo"

            ],

            "City":[

                "Bhopal",

                "Gwalior",

                "Indore",

                "Delhi"

            ],

            "Distance":[

                "2 km",

                "5 km",

                "8 km",

                "10 km"

            ]

        })

        st.dataframe(

            hospitals,

            use_container_width=True,

            hide_index=True

        )

    # ==========================================
    # CONTACT
    # ==========================================

    with tab6:

        st.header("📞 Contact")

        st.write("📧 support@ayushequity.ai")

        st.write("☎ 1800-123-456")

        st.write("🌐 www.ayushequity.ai")

        st.success("24×7 Healthcare Support")

    # ==========================================
    # AI ELIGIBILITY PREDICTION
    # ==========================================

    with tab2:

        st.divider()

        if st.button("🤖 Check Eligibility"):

            payload = {

                "Age": age,

                "Gender": gender,

                "Monthly_Income": income,

                "Annual_Income": income * 12,

                "Family_Size": family,

                "BPL_Status": bpl,

                "Ration_Card": ration,

                "Disability": disability,

                "Chronic_Disease": disease,

                "PMJAY_Registered": pmjay,

                "Occupation": occupation,

                "State": state

            }

            try:

                response = requests.post(

                    "http://127.0.0.1:8000/predict/inclusion",

                    json=payload

                )

                if response.status_code == 200:

                    result = response.json()

                    prediction = result.get(
                        "Prediction",
                        "Unknown"
                    )

                    confidence = result.get(
                        "Confidence",
                        "N/A"
                    )

                    if prediction == "Eligible":

                        st.success(
                            f"✅ {prediction}"
                        )

                    else:

                        st.error(
                            f"❌ {prediction}"
                        )

                    st.info(
                        f"Confidence : {confidence}"
                    )

                else:

                    st.error(response.text)

            except Exception:

                st.error(
                    "FastAPI server is not running."
                )