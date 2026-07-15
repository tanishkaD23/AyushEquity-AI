import pandas as pd
import random
import os

random.seed(42)

# -----------------------------
# Number of Hospitals
# -----------------------------
NUM_HOSPITALS = 500

# -----------------------------
# States & Districts
# -----------------------------
locations = {
    "Madhya Pradesh": ["Gwalior", "Bhopal", "Indore", "Jabalpur", "Ujjain"],
    "Uttar Pradesh": ["Lucknow", "Kanpur", "Agra", "Varanasi", "Prayagraj"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad"],
    "Rajasthan": ["Jaipur", "Jodhpur", "Kota", "Ajmer", "Udaipur"],
    "Gujarat": ["Ahmedabad", "Surat", "Rajkot", "Vadodara", "Bhavnagar"]
}

hospital_prefix = [
    "City Care",
    "LifeCare",
    "Shree",
    "Sunrise",
    "Apollo",
    "Aarogya",
    "MediPlus",
    "Sanjeevani",
    "Jan Kalyan",
    "National",
    "District",
    "Prime",
    "Fortis",
    "Lotus",
    "Health First"
]

hospital_suffix = [
    "Hospital",
    "Medical Centre",
    "Multi Speciality Hospital",
    "Health Center",
    "Care Hospital"
]

hospital_types = [
    "Government",
    "Private"
]

records = []

for i in range(NUM_HOSPITALS):

    hospital_id = f"HOS{i+1:04d}"

    state = random.choice(list(locations.keys()))
    district = random.choice(locations[state])

    hospital_name = (
        random.choice(hospital_prefix)
        + " "
        + district
        + " "
        + random.choice(hospital_suffix)
    )

    latitude = round(random.uniform(8.0, 37.0), 6)
    longitude = round(random.uniform(68.0, 97.0), 6)

    hospital_type = random.choices(
        hospital_types,
        weights=[40,60]
    )[0]

    beds = random.randint(20,600)

    doctors = random.randint(10,120)

    pmjay = random.choices(
        ["Yes","No"],
        weights=[85,15]
    )[0]

    rating = round(random.uniform(2.5,5.0),1)

    previous_fraud = random.choices(
        ["Yes","No"],
        weights=[8,92]
    )[0]

    records.append({

        "Hospital_ID":hospital_id,

        "Hospital_Name":hospital_name,

        "State":state,

        "District":district,

        "Latitude":latitude,

        "Longitude":longitude,

        "Hospital_Type":hospital_type,

        "Beds":beds,

        "Doctors":doctors,

        "PMJAY_Empanelled":pmjay,

        "Rating":rating,

        "Previous_Fraud":previous_fraud
    })

df = pd.DataFrame(records)

os.makedirs("app/datasets",exist_ok=True)

output_path="app/datasets/hospitals.csv"

df.to_csv(output_path,index=False)

print("="*60)
print("HOSPITAL DATASET GENERATED SUCCESSFULLY")
print("="*60)
print("Total Hospitals :",len(df))
print("Columns :",len(df.columns))
print("Saved To :",output_path)
print("="*60)

print(df.head())