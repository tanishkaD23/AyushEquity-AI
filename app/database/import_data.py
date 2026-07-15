import sqlite3
import pandas as pd

DATABASE = "app/database/database.db"

conn = sqlite3.connect(DATABASE)

beneficiaries = pd.read_csv("app/datasets/beneficiaries.csv")
hospitals = pd.read_csv("app/datasets/hospitals.csv")
claims = pd.read_csv("app/datasets/claims.csv")
blockchain = pd.read_csv("app/datasets/blockchain_transactions.csv")

beneficiaries.to_sql(
    "Beneficiaries",
    conn,
    if_exists="append",
    index=False
)

hospitals.to_sql(
    "Hospitals",
    conn,
    if_exists="append",
    index=False
)

claims.to_sql(
    "Claims",
    conn,
    if_exists="append",
    index=False
)

blockchain.to_sql(
    "Blockchain_Transactions",
    conn,
    if_exists="append",
    index=False
)

conn.close()

print("Beneficiaries Imported")
print("Hospitals Imported")
print("Claims Imported")
print("Blockchain Imported")
print("All Data Imported Successfully!")