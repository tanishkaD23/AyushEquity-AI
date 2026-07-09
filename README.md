
#  AyushEquity AI
### AI-Powered Healthcare Inclusion & Fraud Detection System for Ayushman Bharat (PM-JAY)

## 📌 Overview

AyushEquity AI is an AI-driven platform designed to improve healthcare accessibility and reduce fraudulent insurance claims under the Ayushman Bharat PM-JAY scheme.

The system helps government officials identify eligible families who have been excluded from the scheme while simultaneously detecting suspicious hospital claims using Machine Learning.

---

## 🎯 Problem Statement

Millions of eligible citizens remain excluded from government healthcare schemes due to:

- Incomplete or incorrect documentation
- Lack of awareness
- Remote geographical locations
- Manual verification delays

At the same time, healthcare systems also suffer from:

- Fake patient registrations
- Duplicate insurance claims
- Unnecessary medical procedures
- Hospital fraud

AyushEquity AI addresses both challenges using Artificial Intelligence.

---

## ✨ Features

### 👨‍👩‍👧 Citizen Inclusion Prediction
- Predicts healthcare scheme eligibility
- Calculates inclusion score
- Explains prediction
- Suggests required documents

### 🏥 Hospital Fraud Detection
- Detects suspicious insurance claims
- Assigns fraud risk score
- Identifies duplicate claims
- Flags abnormal claim patterns

### 📊 Officer Dashboard
- District-wise inclusion statistics
- Pending verification cases
- Fraud analytics
- Hospital performance monitoring

### 📱 Citizen Portal
- Check eligibility
- Upload documents
- Track application status
- View scheme information

### 🏥 Hospital Portal
- Submit claims
- View fraud alerts
- Track claim history
- Risk assessment dashboard

---

# 🛠 Tech Stack

## Programming
- Python

## Machine Learning
- Scikit-learn
- Random Forest
- XGBoost
- Isolation Forest

## Backend
- FastAPI

## Frontend
- Streamlit

## Database
- SQLite
- SQLAlchemy

## Data Processing
- Pandas
- NumPy

## Data Generation
- Faker

## Visualization
- Plotly
- Matplotlib

---

# 📂 Project Structure

```

AyushEquityAI/
│
├── data/
│   ├── raw/
│   ├── processed/
│   ├── beneficiary_data/
│   ├── claims_data/
│   └── hospital_data/
│
├── database/
│   ├── db_setup.py
│   └── models.py
│
├── models/
│
├── scripts/
│   ├── generate_data.py
│   ├── preprocess.py
│   ├── train_inclusion_model.py
│   ├── train_fraud_model.py
│   └── evaluate_models.py
│
├── backend/
│   ├── api.py
│   ├── routes.py
│   ├── schemas.py
│   └── utils.py
│
├── frontend/
│   ├── citizen_portal.py
│   ├── officer_dashboard.py
│   ├── hospital_dashboard.py
│   └── analytics.py
│
├── notebooks/
├── reports/
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore

````

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AyushEquityAI.git
````

Move into the project:

```bash
cd AyushEquityAI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

### Start FastAPI

```bash
uvicorn backend.api:app --reload
```

### Start Streamlit Dashboard

```bash
streamlit run frontend/officer_dashboard.py
```

---

# 🤖 Machine Learning Models

## Inclusion Prediction

* Random Forest Classifier
* XGBoost Classifier

Predicts whether a citizen is:

* Eligible
* Not Eligible
* Needs Verification

---

## Fraud Detection

* Isolation Forest
* Random Forest

Detects:

* Duplicate claims
* Fake hospitals
* Abnormal claim amounts
* Multiple claims within a short time
* Suspicious treatment patterns

---

# 📈 Future Enhancements

* Aadhaar/eKYC integration
* OCR-based document verification
* Real-time fraud alerts
* Explainable AI (XAI)
* GIS-based healthcare inclusion maps
* AI chatbot for beneficiaries
* Mobile application
* Cloud deployment

---

# 🎯 Project Goals

* Improve healthcare accessibility
* Reduce beneficiary exclusion
* Minimize insurance fraud
* Assist government officers in decision-making
* Increase transparency in healthcare claim processing

---

