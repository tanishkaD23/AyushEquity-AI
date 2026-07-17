import sqlite3
import os

# -----------------------------
# Create database folder if needed
# -----------------------------
os.makedirs("app/database", exist_ok=True)

# -----------------------------
# Connect to SQLite
# -----------------------------
from app.database.database_manager import (
    get_cursor,
    close_connection
)

connection, cursor = get_cursor()

print("Database Connected Successfully!")


### Beneficiaries Table 
cursor.execute("""
CREATE TABLE IF NOT EXISTS Beneficiaries(

Beneficiary_ID TEXT PRIMARY KEY,

Name TEXT,

Age INTEGER,

Gender TEXT,

Mobile TEXT,

Aadhaar TEXT,

State TEXT,

District TEXT,

Village TEXT,

Occupation TEXT,

Monthly_Income INTEGER,

Annual_Income INTEGER,

Family_Size INTEGER,

BPL_Status TEXT,

Ration_Card TEXT,

Disability TEXT,

Chronic_Disease TEXT,

PMJAY_Registered TEXT,

Eligible TEXT,

Latitude REAL,

Longitude REAL

)
""")

print("Beneficiaries Table Created!")


## Hospitals Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Hospitals(

Hospital_ID TEXT PRIMARY KEY,

Hospital_Name TEXT,

State TEXT,

District TEXT,

Latitude REAL,

Longitude REAL,

Hospital_Type TEXT,

Beds INTEGER,

Doctors INTEGER,

PMJAY_Empanelled TEXT,

Rating REAL,

Previous_Fraud TEXT

)
""")

print("Hospitals Table Created!")


## Claims Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Claims(

Claim_ID TEXT PRIMARY KEY,

Beneficiary_ID TEXT,

Hospital_ID TEXT,

Disease TEXT,

Treatment TEXT,

Package_Amount REAL,

Claim_Amount REAL,

Admission_Date TEXT,

Discharge_Date TEXT,

Duplicate_Claim TEXT,

Fraud_Label TEXT,

FOREIGN KEY(Beneficiary_ID)
REFERENCES Beneficiaries(Beneficiary_ID),

FOREIGN KEY(Hospital_ID)
REFERENCES Hospitals(Hospital_ID)
                Status TEXT DEFAULT 'Pending'

)
""")

print("Claims Table Created!")

## Blockchain Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Blockchain_Transactions(

Transaction_ID TEXT PRIMARY KEY,

Claim_ID TEXT,

Hash TEXT,

Timestamp TEXT,

Status TEXT,

FOREIGN KEY(Claim_ID)
REFERENCES Claims(Claim_ID)

)
""")

print("Blockchain Table Created!")
connection.commit()
close_connection(connection)

print("Database Setup Completed Successfully!")