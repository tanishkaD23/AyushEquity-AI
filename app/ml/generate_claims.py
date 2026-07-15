import pandas as pd
import random
import os
from faker import Faker
from datetime import timedelta

fake = Faker("en_IN")
random.seed(42)

# ---------------------------------
# Load Datasets
# ---------------------------------
beneficiaries = pd.read_csv("app/datasets/beneficiaries.csv")
hospitals = pd.read_csv("app/datasets/hospitals.csv")

NUM_CLAIMS = 50000

# ---------------------------------
# Diseases and Treatments
# ---------------------------------

disease_treatment = {
    "Dengue": ("Medical Management", 25000),
    "Malaria": ("Medical Management", 18000),
    "Pneumonia": ("ICU Care", 60000),
    "Appendicitis": ("Appendectomy", 45000),
    "Kidney Stone": ("Lithotripsy", 70000),
    "Heart Disease": ("Angioplasty", 180000),
    "Cancer": ("Chemotherapy", 250000),
    "Cataract": ("Cataract Surgery", 30000),
    "Fracture": ("Orthopedic Surgery", 85000),
    "Tuberculosis": ("Medical Management", 35000)
}

records = []

for i in range(NUM_CLAIMS):

    claim_id = f"CLM{i+1:06d}"

    beneficiary = beneficiaries.sample(1).iloc[0]
    hospital = hospitals.sample(1).iloc[0]

    disease = random.choice(list(disease_treatment.keys()))

    treatment, package_amount = disease_treatment[disease]

    admission = fake.date_between(
        start_date="-365d",
        end_date="today"
    )

    discharge = admission + timedelta(
        days=random.randint(1,10)
    )

    duplicate_claim = random.choices(
        ["Yes","No"],
        weights=[5,95]
    )[0]

    fraud = "No"

    # ------------------------------
    # Generate Claim Amount
    # ------------------------------

    if random.random() < 0.08:

        claim_amount = package_amount + random.randint(
            10000,
            100000
        )

        fraud = "Yes"

    else:

        claim_amount = random.randint(
            int(package_amount*0.70),
            package_amount
        )

    # Duplicate claims are fraud

    if duplicate_claim == "Yes":

        fraud = "Yes"

    # Previous fraud hospital

    if hospital["Previous_Fraud"] == "Yes":

        if random.random() < 0.40:

            fraud = "Yes"

    records.append({

        "Claim_ID":claim_id,

        "Beneficiary_ID":beneficiary["Beneficiary_ID"],

        "Hospital_ID":hospital["Hospital_ID"],

        "Disease":disease,

        "Treatment":treatment,

        "Package_Amount":package_amount,

        "Claim_Amount":claim_amount,

        "Admission_Date":admission,

        "Discharge_Date":discharge,

        "Duplicate_Claim":duplicate_claim,

        "Fraud_Label":fraud
    })

df = pd.DataFrame(records)

os.makedirs("app/datasets",exist_ok=True)

output="app/datasets/claims.csv"

df.to_csv(output,index=False)

print("="*60)
print("CLAIMS DATASET GENERATED SUCCESSFULLY")
print("="*60)
print("Records :",len(df))
print("Columns :",len(df.columns))
print("Saved :",output)
print("="*60)

print(df.head())