import pandas as pd
import numpy as np
import os

print("=" * 70)
print("AYUSHEQUITY AI - FEATURE ENGINEERING")
print("=" * 70)

# ==========================================================
# Create processed data directory
# ==========================================================

os.makedirs("app/data/processed", exist_ok=True)

# ==========================================================
# Load Datasets
# ==========================================================

beneficiaries = pd.read_csv("app/datasets/beneficiaries.csv")
claims = pd.read_csv("app/datasets/claims.csv")
hospitals = pd.read_csv("app/datasets/hospitals.csv")

print("\nDatasets Loaded Successfully!")

print("\nBeneficiaries :", beneficiaries.shape)
print("Hospitals      :", hospitals.shape)
print("Claims         :", claims.shape)

# ==========================================================
# Missing Values
# ==========================================================

print("\nChecking Missing Values...")

print("\nBeneficiaries")
print(beneficiaries.isnull().sum())

print("\nHospitals")
print(hospitals.isnull().sum())

print("\nClaims")
print(claims.isnull().sum())

beneficiaries.fillna("Unknown", inplace=True)
claims.fillna(0, inplace=True)
hospitals.fillna("Unknown", inplace=True)

print("\nMissing Values Handled")

# ==========================================================
# Remove Duplicate Records
# ==========================================================

beneficiaries.drop_duplicates(inplace=True)
claims.drop_duplicates(inplace=True)
hospitals.drop_duplicates(inplace=True)

print("\nDuplicate Records Removed")

# ==========================================================
# Encode Gender
# ==========================================================

beneficiaries["Gender"] = beneficiaries["Gender"].map({
    "Male": 1,
    "Female": 0
})

# ==========================================================
# Encode Yes / No Columns
# ==========================================================

beneficiary_columns = [
    "BPL_Status",
    "Disability",
    "Chronic_Disease",
    "PMJAY_Registered",
    "Eligible"
]

for col in beneficiary_columns:
    beneficiaries[col] = beneficiaries[col].map({
        "Yes": 1,
        "No": 0
    })

hospital_columns = [
    "PMJAY_Empanelled",
    "Previous_Fraud"
]

for col in hospital_columns:
    hospitals[col] = hospitals[col].map({
        "Yes": 1,
        "No": 0
    })

claim_columns = [
    "Duplicate_Claim",
    "Fraud_Label"
]

for col in claim_columns:
    claims[col] = claims[col].map({
        "Yes": 1,
        "No": 0
    })

print("\nCategorical Encoding Completed")

# ==========================================================
# Feature Engineering
# ==========================================================

print("\nCreating New Features...")

# Claim Difference

claims["Claim_Difference"] = (
    claims["Claim_Amount"] -
    claims["Package_Amount"]
)

# Income Group

def income_group(x):

    if x < 100000:
        return "Low"

    elif x < 300000:
        return "Medium"

    else:
        return "High"

beneficiaries["Income_Group"] = beneficiaries[
    "Annual_Income"
].apply(income_group)

# Senior Citizen

beneficiaries["Senior_Citizen"] = (
    beneficiaries["Age"] >= 60
).astype(int)

# Family Risk Score

beneficiaries["Family_Risk_Score"] = (
    beneficiaries["Family_Size"] +
    beneficiaries["Disability"] +
    beneficiaries["Chronic_Disease"]
)

# Hospital Size

def hospital_size(beds):

    if beds < 100:
        return "Small"

    elif beds < 300:
        return "Medium"

    else:
        return "Large"

hospitals["Hospital_Size"] = hospitals[
    "Beds"
].apply(hospital_size)

# Hospital Risk Score

hospitals["Hospital_Risk_Score"] = (
    hospitals["Previous_Fraud"] * 2 +
    (5 - hospitals["Rating"])
)

# Fraud Risk Index

claims["Fraud_Risk_Index"] = (
    claims["Duplicate_Claim"] +
    (claims["Claim_Difference"] > 0).astype(int)
)

print("New Features Created Successfully")

# ==========================================================
# Merge Datasets
# ==========================================================

print("\nMerging Datasets...")

merged = claims.merge(
    beneficiaries,
    on="Beneficiary_ID",
    how="left"
)

merged = merged.merge(
    hospitals,
    on="Hospital_ID",
    how="left"
)

print("Merged Dataset Shape :", merged.shape)

# ==========================================================
# Save Processed Files
# ==========================================================

beneficiaries.to_csv(
    "app/data/processed/processed_beneficiaries.csv",
    index=False
)

claims.to_csv(
    "app/data/processed/processed_claims.csv",
    index=False
)

hospitals.to_csv(
    "app/data/processed/processed_hospitals.csv",
    index=False
)

merged.to_csv(
    "app/data/processed/final_training_data.csv",
    index=False
)

print("\nProcessed Files Saved Successfully")

# ==========================================================
# Summary
# ==========================================================

print("\n" + "=" * 70)
print("FEATURE ENGINEERING COMPLETED")
print("=" * 70)

print("Processed Beneficiaries :", beneficiaries.shape)
print("Processed Hospitals     :", hospitals.shape)
print("Processed Claims        :", claims.shape)
print("Final Training Dataset  :", merged.shape)

print("\nFiles Generated:")

print("processed_beneficiaries.csv")
print("processed_hospitals.csv")
print("processed_claims.csv")
print("final_training_data.csv")

print("=" * 70)