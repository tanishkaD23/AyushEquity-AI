import pandas as pd
import os

# -----------------------------
# Dataset Paths
# -----------------------------
BASE_PATH = "app/datasets"

beneficiary_path = os.path.join(BASE_PATH, "beneficiaries.csv")
hospital_path = os.path.join(BASE_PATH, "hospitals.csv")
claim_path = os.path.join(BASE_PATH, "claims.csv")

print("=" * 50)
print("AYUSHEQUITY AI - DATA VALIDATION")
print("=" * 50)

# -----------------------------
# Load Datasets
# -----------------------------
try:
    beneficiaries = pd.read_csv(beneficiary_path)
    hospitals = pd.read_csv(hospital_path)
    claims = pd.read_csv(claim_path)

    print("✅ All datasets loaded successfully.\n")

except Exception as e:
    print("❌ Error loading datasets:")
    print(e)
    exit()

# -----------------------------
# Dataset Shapes
# -----------------------------
print("Dataset Shapes")
print("---------------------------")
print(f"Beneficiaries : {beneficiaries.shape}")
print(f"Hospitals     : {hospitals.shape}")
print(f"Claims        : {claims.shape}")

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values")
print("---------------------------")

print("\nBeneficiaries")
print(beneficiaries.isnull().sum())

print("\nHospitals")
print(hospitals.isnull().sum())

print("\nClaims")
print(claims.isnull().sum())

# -----------------------------
# Duplicate IDs
# -----------------------------
print("\nDuplicate Records")
print("---------------------------")

print("Beneficiary IDs :", beneficiaries["Beneficiary_ID"].duplicated().sum())
print("Hospital IDs    :", hospitals["Hospital_ID"].duplicated().sum())
print("Claim IDs       :", claims["Claim_ID"].duplicated().sum())

# -----------------------------
# Referential Integrity
# -----------------------------
print("\nRelationship Validation")
print("---------------------------")

invalid_beneficiary = claims[
    ~claims["Beneficiary_ID"].isin(beneficiaries["Beneficiary_ID"])
]

invalid_hospital = claims[
    ~claims["Hospital_ID"].isin(hospitals["Hospital_ID"])
]

print("Invalid Beneficiary IDs :", len(invalid_beneficiary))
print("Invalid Hospital IDs    :", len(invalid_hospital))

# -----------------------------
# Final Status
# -----------------------------
print("\n" + "=" * 50)

if (
    beneficiaries["Beneficiary_ID"].duplicated().sum() == 0
    and hospitals["Hospital_ID"].duplicated().sum() == 0
    and claims["Claim_ID"].duplicated().sum() == 0
    and len(invalid_beneficiary) == 0
    and len(invalid_hospital) == 0
):
    print("🎉 DATA VALIDATION SUCCESSFUL")
else:
    print("⚠️ DATA VALIDATION COMPLETED WITH WARNINGS")

print("=" * 50)