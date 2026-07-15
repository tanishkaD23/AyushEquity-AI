from faker import Faker
import pandas as pd
import random
import os

fake = Faker("en_IN")
Faker.seed(42)
random.seed(42)

NUM_OFFICERS = 100

states = [
    "Madhya Pradesh",
    "Uttar Pradesh",
    "Rajasthan",
    "Bihar",
    "Maharashtra",
    "Jharkhand",
    "Chhattisgarh",
    "Odisha",
    "Gujarat",
    "West Bengal"
]

districts = [
    "Bhopal",
    "Indore",
    "Gwalior",
    "Jabalpur",
    "Lucknow",
    "Jaipur",
    "Patna",
    "Nagpur",
    "Ranchi",
    "Raipur"
]

designations = [
    "District Health Officer",
    "Block Medical Officer",
    "Ayushman Mitra",
    "Enrollment Officer",
    "Medical Superintendent",
    "Health Inspector",
    "Verification Officer",
    "Claims Officer"
]

departments = [
    "PM-JAY",
    "Health Department",
    "District Administration",
    "Insurance Cell"
]

rows = []

for i in range(1, NUM_OFFICERS + 1):

    rows.append({

        "Officer_ID": f"OFF{i:04d}",

        "Officer_Name": fake.name(),

        "Gender": random.choice(["Male", "Female"]),

        "Age": random.randint(25, 60),

        "Designation": random.choice(designations),

        "Department": random.choice(departments),

        "State": random.choice(states),

        "District": random.choice(districts),

        "Years_of_Experience": random.randint(1, 30),

        "Verified_Beneficiaries": random.randint(100, 10000),

        "Fraud_Cases_Investigated": random.randint(0, 150),

        "Performance_Rating": round(random.uniform(2.5, 5.0), 1),

        "Email": fake.company_email(),

        "Phone_Number": fake.phone_number()

    })

df = pd.DataFrame(rows)

os.makedirs("app/data", exist_ok=True)

df.to_csv("app/data/officers.csv", index=False)

print("=" * 60)
print("Officers Dataset Generated Successfully!")
print(f"Total Records : {len(df)}")
print("Saved at : app/data/officers.csv")
print("=" * 60)

print(df.head())