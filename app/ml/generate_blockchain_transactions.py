import pandas as pd
import hashlib
import random
from faker import Faker
import os

fake = Faker("en_IN")

# -----------------------------
# Load Claims Dataset
# -----------------------------
claims_path = "app/datasets/claims.csv"

claims = pd.read_csv(claims_path)

# Generate transactions for first 100 claims
claims = claims.head(100)

transactions = []

status_list = [
    "Pending",
    "Approved",
    "Rejected",
    "Verified"
]

for i, row in claims.iterrows():

    transaction_id = f"TXN{i+1:06d}"

    claim_id = row["Claim_ID"]

    # Create SHA-256 Hash
    hash_input = (
        str(claim_id)
        + str(fake.date_time())
        + str(random.randint(1000, 9999))
    )

    transaction_hash = hashlib.sha256(
        hash_input.encode()
    ).hexdigest()

    timestamp = fake.date_time_between(
        start_date="-30d",
        end_date="now"
    )

    status = random.choice(status_list)

    transactions.append({
        "Transaction_ID": transaction_id,
        "Claim_ID": claim_id,
        "Hash": transaction_hash,
        "Timestamp": timestamp,
        "Status": status
    })

# -----------------------------
# Save Dataset
# -----------------------------
df = pd.DataFrame(transactions)

os.makedirs("app/datasets", exist_ok=True)

output_path = "app/datasets/blockchain_transactions.csv"

df.to_csv(output_path, index=False)

print("=" * 50)
print("Blockchain Transactions Dataset Created Successfully")
print("=" * 50)
print(df.head())
print("\nSaved at:", output_path)
print("Total Records:", len(df))