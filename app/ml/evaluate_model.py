import sqlite3
import pandas as pd
import joblib
import json

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# -------------------------------
# Load Dataset
# -------------------------------

conn = sqlite3.connect("app/database/database.db")

df = pd.read_sql("SELECT * FROM Beneficiaries", conn)

conn.close()

# -------------------------------
# Feature Selection
# -------------------------------

feature_columns = [
    "Age",
    "Gender",
    "Monthly_Income",
    "Annual_Income",
    "Family_Size",
    "BPL_Status",
    "Ration_Card",
    "Disability",
    "Chronic_Disease",
    "PMJAY_Registered",
    "Occupation",
    "State"
]

X = df[feature_columns]
y = df["Eligible"]

# -------------------------------
# Preprocessing
# -------------------------------

X = X.ffill()

y = y.map({"Yes": 1, "No": 0})

encoder = LabelEncoder()

categorical_columns = [
    "Gender",
    "BPL_Status",
    "Ration_Card",
    "Disability",
    "Chronic_Disease",
    "PMJAY_Registered",
    "Occupation",
    "State"
]

for col in categorical_columns:
    X[col] = encoder.fit_transform(X[col])

# -------------------------------
# Train-Test Split
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# -------------------------------
# Load Saved Model
# -------------------------------

model = joblib.load("app/models/inclusion_model.pkl")

# -------------------------------
# Prediction
# -------------------------------

predictions = model.predict(X_test)

# -------------------------------
# Metrics
# -------------------------------

accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions)
recall = recall_score(y_test, predictions)
f1 = f1_score(y_test, predictions)

print("="*50)
print("MODEL EVALUATION")
print("="*50)

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("\nConfusion Matrix")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report")
print(classification_report(y_test, predictions))

# -------------------------------
# Save Metrics
# -------------------------------

metrics = {
    "Accuracy": float(accuracy),
    "Precision": float(precision),
    "Recall": float(recall),
    "F1 Score": float(f1)
}

with open("app/reports/model_metrics.json", "w") as file:
    json.dump(metrics, file, indent=4)

print("\nMetrics saved to app/reports/model_metrics.json")