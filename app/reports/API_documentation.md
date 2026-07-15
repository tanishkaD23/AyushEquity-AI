# AyushEquity AI API Documentation

## Base URL

http://127.0.0.1:8000

---

## GET /

Returns API status.

Response

{
    "Project":"AyushEquity AI",
    "Status":"Running"
}

---

## GET /health

Checks API health.

Response

{
    "Server":"Healthy",
    "Database":"Connected",
    "Models":"Loaded"
}

---

## POST /predict/inclusion

Predicts PM-JAY eligibility.

Request

{
    "Age":45,
    "Gender":"Male",
    "Monthly_Income":5000,
    "Annual_Income":60000,
    "Family_Size":5,
    "BPL_Status":"Yes",
    "Ration_Card":"PHH",
    "Disability":"No",
    "Chronic_Disease":"Yes",
    "PMJAY_Registered":"Yes",
    "Occupation":"Farmer",
    "State":"Madhya Pradesh"
}

Response

{
    "Prediction":"Eligible",
    "Confidence":"98.52%"
}

---

## POST /predict/fraud

Predicts whether a healthcare claim is fraudulent.

Response

{
    "Prediction":"Fraud",
    "Risk":"High",
    "Confidence":"99.11%"
}

---

## Swagger Documentation

http://127.0.0.1:8000/docs

---

## Technology Stack

- FastAPI
- Scikit-learn
- SQLite
- Joblib
- Pydantic
- Uvicorn

---

## Developed For

AyushEquity AI

AI-powered Healthcare Inclusion & Fraud Detection Platform