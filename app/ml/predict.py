import joblib
import pandas as pd

# -----------------------------
# Load Trained Model
# -----------------------------
model = joblib.load("app/models/inclusion_model.pkl")

# -----------------------------
# Sample Citizen Data
# (Must match training features)
# -----------------------------
sample = pd.DataFrame([{
    "Age": 45,
    "Gender": 1,                # Male=1 Female=0
    "Monthly_Income": 5000,
    "Annual_Income": 60000,
    "Family_Size": 5,
    "BPL_Status": 1,            # Yes=1 No=0
    "Ration_Card": 1,           # Encode as in training
    "Disability": 0,
    "Chronic_Disease": 1,
    "PMJAY_Registered": 1,
    "Occupation": 2,            # Encoded value
    "State": 3                  # Encoded value
}])

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict(sample)[0]

# -----------------------------
# Confidence Score
# -----------------------------
confidence = model.predict_proba(sample)[0].max() * 100

# -----------------------------
# Display Result
# -----------------------------
print("=" * 50)
print("AYUSHEQUITY AI - ELIGIBILITY PREDICTION")
print("=" * 50)

if prediction == 1:
    print("Prediction : Eligible ✅")
else:
    print("Prediction : Not Eligible ❌")

print(f"Confidence : {confidence:.2f}%")

print("=" * 50)