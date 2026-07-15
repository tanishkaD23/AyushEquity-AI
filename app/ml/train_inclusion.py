import sqlite3
import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

# =====================================================
# STEP 1 : LOAD DATASET
# =====================================================

print("=" * 60)
print("STEP 1 : Loading Dataset")
print("=" * 60)

conn = sqlite3.connect("app/database/database.db")

df = pd.read_sql(
    "SELECT * FROM Beneficiaries",
    conn
)

conn.close()

print(df.head())

print("\nDataset Shape :", df.shape)

# =====================================================
# STEP 2 : FEATURE SELECTION
# =====================================================

print("\n" + "=" * 60)
print("STEP 2 : Feature Selection")
print("=" * 60)

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

print("Features Selected Successfully")

print(X.head())

# =====================================================
# STEP 3 : DATA PREPROCESSING
# =====================================================

print("\n" + "=" * 60)
print("STEP 3 : Data Preprocessing")
print("=" * 60)

# Missing Values

X = X.ffill()
# Encode Target

y = y.map({

    "Yes":1,

    "No":0

})

# Label Encoding

label_columns = [

    "Gender",

    "BPL_Status",

    "Ration_Card",

    "Disability",

    "Chronic_Disease",

    "PMJAY_Registered",

    "Occupation",

    "State"

]

# Dictionary to store all encoders
encoders = {}

for col in label_columns:
    encoder = LabelEncoder()
    X[col] = encoder.fit_transform(X[col].astype(str))
    encoders[col] = encoder

print("Preprocessing Completed")

# =====================================================
# Train Test Split
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42

)

print("\nTraining Shape :", X_train.shape)

print("Testing Shape :", X_test.shape)

# =====================================================
# STEP 4 : MODEL TRAINING
# =====================================================

print("\n" + "=" * 60)
print("STEP 4 : Training Models")
print("=" * 60)

models = {

    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Decision Tree": DecisionTreeClassifier(random_state=42),

    "Random Forest": RandomForestClassifier(random_state=42),

    "XGBoost": XGBClassifier(
        random_state=42,
        eval_metric="logloss"
    )

}

best_accuracy = 0

best_model = None

best_model_name = ""

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\n{name}")

    print("Accuracy :", round(accuracy*100,2),"%")

    print(classification_report(y_test,predictions))

    if accuracy > best_accuracy:

        best_accuracy = accuracy

        best_model = model

        best_model_name = name

# =====================================================
# STEP 5 : SAVE BEST MODEL
# =====================================================

print("\n" + "=" * 60)
print("BEST MODEL")
print("=" * 60)

print("Model :",best_model_name)

print("Accuracy :",round(best_accuracy*100,2),"%")
os.makedirs("app/models", exist_ok=True)

joblib.dump(
    best_model,
    "app/models/inclusion_model.pkl"
)

joblib.dump(
    encoders,
    "app/models/label_encoders.pkl"
)

print("=" * 60)
print("Training Completed Successfully")
print("=" * 60)

print("Model Saved At:")
print("app/models/inclusion_model.pkl")

print("\nEncoders Saved At:")
print("app/models/label_encoders.pkl")