import sqlite3
import pandas as pd

conn = sqlite3.connect("app/database/database.db")

claims = pd.read_sql(
    "SELECT * FROM Claims",
    conn
)

beneficiaries = pd.read_sql(
    "SELECT * FROM Beneficiaries",
    conn
)

hospitals = pd.read_sql(
    "SELECT * FROM Hospitals",
    conn
)
df = claims.merge(
    beneficiaries,
    on="Beneficiary_ID",
    how="left"
)
df = df.merge(
    hospitals,
    on="Hospital_ID",
    how="left"
)
print(df.head())

print(df.shape)

print(df.info())
feature_columns = [
    "Claim_Amount",
    "Package_Amount",
    "Duplicate_Claim",
    "Disease",
    "Treatment",
    "Admission_Date",
    "Discharge_Date",
    "Previous_Fraud",
    "Hospital_Type",
    "Beds",
    "Doctors",
    "Rating"
]

X = df[feature_columns]

y = df["Fraud_Label"]
print("=" * 50)

print("Feature Selection Completed")

print("=" * 50)

print(X.head())

print()

print(y.head())

print()

print("Features Shape :", X.shape)

print("Target Shape :", y.shape)
# =====================================================
# STEP 3 : DATA PREPROCESSING
# =====================================================


from sklearn.preprocessing import LabelEncoder
import joblib
import os

# -----------------------------
# Handle Missing Values
# -----------------------------

X = X.ffill()

print("Missing Values Handled")

# -----------------------------
# Encode Target Variable
# -----------------------------

y = y.map({
    "Yes": 1,
    "No": 0
})

print("Target Variable Encoded")

# -----------------------------
# Categorical Columns
# -----------------------------

categorical_columns = [

    "Duplicate_Claim",

    "Disease",

    "Treatment",

    "Hospital_Type",

    "Previous_Fraud"

]

# -----------------------------
# Label Encoding
# -----------------------------

encoders = {}

for col in categorical_columns:

    encoder = LabelEncoder()

    X[col] = encoder.fit_transform(X[col])

    encoders[col] = encoder

print("Categorical Columns Encoded")

# -----------------------------
# Convert Date Columns
# -----------------------------

X["Admission_Date"] = pd.to_datetime(
    X["Admission_Date"]
)

X["Discharge_Date"] = pd.to_datetime(
    X["Discharge_Date"]
)

print("Date Columns Converted")

# -----------------------------
# Save Encoders
# -----------------------------

os.makedirs("app/models", exist_ok=True)

joblib.dump(
    encoders,
    "app/models/fraud_label_encoders.pkl"
)

print("Label Encoders Saved")

print("=" * 60)
print("STEP 3 COMPLETED")
print("=" * 60)
# =====================================================
# STEP 4 : FEATURE ENGINEERING
# =====================================================

print("\n" + "=" * 60)
print("STEP 4 : FEATURE ENGINEERING")
print("=" * 60)

# -----------------------------------------------------
# Feature 1 : Length of Stay
# -----------------------------------------------------

X["Length_of_Stay"] = (
    X["Discharge_Date"] -
    X["Admission_Date"]
).dt.days

print("✔ Length_of_Stay Created")

# -----------------------------------------------------
# Feature 2 : Claim Ratio
# -----------------------------------------------------

X["Claim_Ratio"] = (
    X["Claim_Amount"] /
    X["Package_Amount"].replace(0, 1)
)

print("✔ Claim_Ratio Created")

# -----------------------------------------------------
# Feature 3 : High Claim
# -----------------------------------------------------

X["High_Claim"] = (
    X["Claim_Amount"] >
    X["Package_Amount"]
).astype(int)

print("✔ High_Claim Created")

# -----------------------------------------------------
# Feature 4 : Fraud Hospital
# -----------------------------------------------------

X["Fraud_Hospital"] = X["Previous_Fraud"]

print("✔ Fraud_Hospital Created")

# -----------------------------------------------------
# Feature 5 : Hospital Capacity
# -----------------------------------------------------

X["Doctor_Bed_Ratio"] = (
    X["Doctors"] /
    X["Beds"].replace(0, 1)
)

print("✔ Doctor_Bed_Ratio Created")

# -----------------------------------------------------
# Feature 6 : Claim Per Bed
# -----------------------------------------------------

X["Claim_Per_Bed"] = (
    X["Claim_Amount"] /
    X["Beds"].replace(0, 1)
)

print("✔ Claim_Per_Bed Created")

# -----------------------------------------------------
# Feature 7 : Claim Difference
# -----------------------------------------------------

X["Claim_Difference"] = (
    X["Claim_Amount"] -
    X["Package_Amount"]
)

print("✔ Claim_Difference Created")

# -----------------------------------------------------
# Remove Date Columns
# -----------------------------------------------------

X.drop(
    columns=[
        "Admission_Date",
        "Discharge_Date"
    ],
    inplace=True
)

print("✔ Date Columns Removed")

# -----------------------------------------------------
# Check Dataset
# -----------------------------------------------------

print("\nDataset Shape :", X.shape)

print("\nColumns")

print(X.columns.tolist())

print("\nSample Data")

print(X.head())

print("=" * 60)
print("STEP 4 COMPLETED SUCCESSFULLY")
print("=" * 60)
# =====================================================
# STEP 5 : TRAIN-TEST SPLIT & MODEL TRAINING
# =====================================================

print("\n" + "=" * 60)
print("STEP 5 : TRAINING FRAUD DETECTION MODELS")
print("=" * 60)

import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# -----------------------------------------------------
# Train-Test Split
# -----------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

print("\nTraining Shape :", X_train.shape)
print("Testing Shape :", X_test.shape)

# -----------------------------------------------------
# Models
# -----------------------------------------------------

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Decision Tree":
        DecisionTreeClassifier(random_state=42),

    "Random Forest":
        RandomForestClassifier(random_state=42),

    "XGBoost":
        XGBClassifier(
            random_state=42,
            eval_metric="logloss"
        )

}

best_model = None

best_model_name = ""

best_accuracy = 0

# -----------------------------------------------------
# Train Models
# -----------------------------------------------------

for name, model in models.items():

    print("\n" + "-" * 50)

    print("Training :", name)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    print("Accuracy :", round(accuracy * 100, 2), "%")

    print("\nConfusion Matrix")

    print(confusion_matrix(
        y_test,
        predictions
    ))

    print("\nClassification Report")

    print(classification_report(
        y_test,
        predictions
    ))

    if accuracy > best_accuracy:

        best_accuracy = accuracy

        best_model = model

        best_model_name = name

# -----------------------------------------------------
# Save Best Model
# -----------------------------------------------------

print("\n" + "=" * 60)

print("BEST MODEL")

print("=" * 60)

print("Model :", best_model_name)

print("Accuracy :", round(best_accuracy * 100, 2), "%")

os.makedirs(
    "app/models",
    exist_ok=True
)

joblib.dump(

    best_model,

    "app/models/fraud_model.pkl"

)

print("\nFraud Model Saved Successfully")

print("Location : app/models/fraud_model.pkl")

print("=" * 60)
import joblib
import pandas as pd

# -------------------------------
# Load Model
# -------------------------------

model = joblib.load("app/models/fraud_model.pkl")

encoders = joblib.load("app/models/fraud_label_encoders.pkl")


class FraudAgent:

    def preprocess(self, claim):

        df = pd.DataFrame([claim])

        categorical_columns = [

            "Duplicate_Claim",

            "Disease",

            "Treatment",

            "Hospital_Type",

            "Previous_Fraud"

        ]

        for col in categorical_columns:

            df[col] = encoders[col].transform(df[col])

        return df

    def predict(self, claim):

        df = self.preprocess(claim)

        prediction = model.predict(df)[0]

        probability = model.predict_proba(df)[0].max() * 100

        if prediction == 1:

            status = "Fraud"

            risk = "High"

        else:

            status = "Genuine"

            risk = "Low"

        return {

            "Prediction": status,

            "Risk": risk,

            "Confidence": round(probability,2)

        }


if __name__ == "__main__":

    sample = {

        "Claim_Amount":95000,

        "Package_Amount":70000,

        "Duplicate_Claim":"Yes",

        "Disease":"Heart Disease",

        "Treatment":"Angioplasty",

        "Hospital_Type":"Private",

        "Previous_Fraud":"Yes",

        "Beds":120,

        "Doctors":30,

        "Rating":2.9,

        "Length_of_Stay":6,

        "Claim_Ratio":1.35,

        "High_Claim":1,

        "Fraud_Hospital":1,

        "Doctor_Bed_Ratio":0.25,

        "Claim_Per_Bed":791,

        "Claim_Difference":25000

    }

    agent = FraudAgent()

    result = agent.predict(sample)

    print(result)
conn.close()