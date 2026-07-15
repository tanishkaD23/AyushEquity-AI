import pandas as pd
import random
import os
from faker import Faker

fake = Faker("en_IN")
random.seed(42)

# -----------------------------
# Number of Records
# -----------------------------
NUM_RECORDS = 10000

# -----------------------------
# States and Districts
# -----------------------------
locations = {
    "Madhya Pradesh": ["Gwalior", "Bhopal", "Indore", "Jabalpur", "Ujjain"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Prayagraj"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Kota", "Ajmer", "Udaipur"],
    "Gujarat": ["Ahmedabad", "Surat", "Rajkot", "Vadodara", "Bhavnagar"]
}

occupations = [
    "Farmer",
    "Labourer",
    "Driver",
    "Electrician",
    "Teacher",
    "Shopkeeper",
    "Tailor",
    "Mason",
    "Student",
    "Homemaker",
    "Retired",
    "Nurse",
    "Mechanic"
]

ration_cards = ["AAY", "PHH", "None"]

records = []

for i in range(NUM_RECORDS):

    beneficiary_id = f"BEN{i+1:05d}"

    state = random.choice(list(locations.keys()))
    district = random.choice(locations[state])

    village = fake.city()

    age = random.randint(18, 90)

    gender = random.choice(["Male", "Female"])

    monthly_income = random.randint(3000, 70000)
    annual_income = monthly_income * 12

    family_size = random.randint(1, 8)

    bpl = random.choices(
        ["Yes", "No"],
        weights=[40, 60]
    )[0]

    disability = random.choices(
        ["Yes", "No"],
        weights=[10, 90]
    )[0]

    chronic = random.choices(
        ["Yes", "No"],
        weights=[20, 80]
    )[0]

    registered = random.choices(
        ["Yes", "No"],
        weights=[75, 25]
    )[0]

    if bpl == "Yes":
        ration = random.choice(["AAY", "PHH"])
    else:
        ration = "None"

    occupation = random.choice(occupations)

    latitude = round(random.uniform(8.0, 37.0), 6)
    longitude = round(random.uniform(68.0, 97.0), 6)

    # -----------------------------
    # Eligibility Logic
    # -----------------------------
    eligible = "No"

    if annual_income <= 120000 and bpl == "Yes":
        eligible = "Yes"

    elif disability == "Yes":
        eligible = "Yes"

    elif age >= 60 and annual_income <= 180000:
        eligible = "Yes"

    elif chronic == "Yes" and annual_income <= 150000:
        eligible = "Yes"

    records.append({

        "Beneficiary_ID": beneficiary_id,

        "Name": fake.name(),

        "Age": age,

        "Gender": gender,

        "Mobile": fake.msisdn()[:10],

        "Aadhaar": str(random.randint(
            100000000000,
            999999999999
        )),

        "State": state,

        "District": district,

        "Village": village,

        "Occupation": occupation,

        "Monthly_Income": monthly_income,

        "Annual_Income": annual_income,

        "Family_Size": family_size,

        "BPL_Status": bpl,

        "Ration_Card": ration,

        "Disability": disability,

        "Chronic_Disease": chronic,

        "PMJAY_Registered": registered,

        "Eligible": eligible,

        "Latitude": latitude,

        "Longitude": longitude
    })

df = pd.DataFrame(records)

os.makedirs("app/datasets", exist_ok=True)

output_file = "app/datasets/beneficiaries.csv"

df.to_csv(output_file, index=False)

print("=" * 60)
print("BENEFICIARIES DATASET GENERATED SUCCESSFULLY")
print("=" * 60)
print("Records :", len(df))
print("Columns :", len(df.columns))
print("Saved to:", output_file)
print("=" * 60)
print(df.head())