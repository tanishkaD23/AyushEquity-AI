
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

🚀 Technology Stack
💻 Programming Language
Python 3.11
🤖 Artificial Intelligence & Machine Learning
Scikit-learn
XGBoost
Pandas
NumPy
Joblib

Algorithms Used:

Logistic Regression
Decision Tree
Random Forest
XGBoost
Label Encoding
Feature Engineering
🌐 Backend Development
FastAPI
Uvicorn
Pydantic
SQLAlchemy (optional)
🎨 Frontend
Streamlit
HTML (optional)
CSS (optional)
Plotly
Matplotlib
🗄 Database
SQLite3
🔗 Blockchain
SHA-256 Hashing (hashlib)
Custom Blockchain Implementation
Blockchain Transaction Ledger
Smart Contract Simulation (Python)
🤖 AI Agents (Agentic AI)
Inclusion Agent
Fraud Detection Agent
Blockchain Agent
Analytics Agent
Notification Agent
📊 Data Analytics
Pandas
Plotly
Matplotlib

Charts:

Bar Charts
Pie Charts
Line Charts
Donut Charts
Heatmaps
KPI Cards
📍 GIS & Mapping
Folium
Streamlit-Folium
🧪 Testing
Pytest
📄 Reports
JSON
CSV
Markdown
PDF
🛠 Development Tools
VS Code
Git
GitHub
Swagger UI
---

# 📂 Project Structure

AyushEquity-AI/
│
├── app/
│
│   ├── backend/
│   │   ├── api.py
│   │   ├── schemas.py
│   │   ├── routes.py
│   │   ├── database_routes.py
│   │   ├── utils.py
│   │   ├── config.py
│   │   └── auth.py
│   │
│   ├── frontend/
│   │   ├── officer_dashboard.py
│   │   ├── citizen_portal.py
│   │   ├── beneficiary_page.py
│   │   ├── fraud_page.py
│   │   ├── analytics.py
│   │   ├── maps.py
│   │   ├── reports.py
│   │   ├── settings.py
│   │   └── assets/
│   │       ├── logo.png
│   │       ├── style.css
│   │       └── background.png
│   │
│   ├── agents/
│   │   ├── inclusion_agent.py
│   │   ├── fraud_agent.py
│   │   ├── blockchain_agent.py
│   │   ├── analytics_agent.py
│   │   ├── notification_agent.py
│   │   └── agent_roles.json
│   │
│   ├── ml/
│   │   ├── train_inclusion.py
│   │   ├── evaluate_model.py
│   │   ├── predict.py
│   │   ├── train_fraud.py
│   │   ├── evaluate_fraud.py
│   │   ├── predict_fraud.py
│   │   ├── explain_fraud.py
│   │   ├── fraud_preprocess.py
│   │   ├── validate_data.py
│   │   └── feature_engineering.py
│   │
│   ├── models/
│   │   ├── inclusion_model.pkl
│   │   ├── fraud_model.pkl
│   │   ├── label_encoders.pkl
│   │   └── fraud_label_encoders.pkl
│   │
│   ├── blockchain/
│   │   ├── blockchain.py
│   │   ├── smart_contract.py
│   │   ├── transaction.py
│   │   ├── verifier.py
│   │   └── hash_utils.py
│   │
│   ├── database/
│   │   ├── database.db
│   │   ├── db_setup.py
│   │   ├── db_utils.py
│   │   └── seed_database.py
│   │
│   ├── data/
│   │   ├── beneficiaries.csv
│   │   ├── hospitals.csv
│   │   ├── claims.csv
│   │   ├── blockchain_transactions.csv
│   │   ├── officers.csv
│   │   ├── applications.csv
│   │   ├── processed/
│   │   └── raw/
│   │
│   ├── reports/
│   │   ├── Inclusion_Model_Report.md
│   │   ├── Fraud_Model_Report.md
│   │   ├── API_Documentation.md
│   │   ├── model_metrics.json
│   │   ├── fraud_metrics.json
│   │   ├── dashboard_report.pdf
│   │   └── analytics_report.pdf
│   │
│   ├── notebook/
│   │   ├── EDA.ipynb
│   │   ├── Inclusion_Model.ipynb
│   │   └── Fraud_Model.ipynb
│   │
│   └── utils/
│       ├── helper.py
│       ├── logger.py
│       ├── constants.py
│       └── encryption.py
│
├── tests/
│   ├── test_api.py
│   ├── test_model.py
│   ├── test_database.py
│   └── test_agents.py
│
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── main.py

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

