from app.database.database_manager import (
    get_cursor,
    close_connection
)

connection, cursor = get_cursor()

print("=" * 60)
print("AYUSHEQUITY AI DATABASE REPORT")
print("=" * 60)

# ------------------------------
# Total Beneficiaries
# ------------------------------
cursor.execute("""
SELECT COUNT(*)
FROM Beneficiaries
""")

print("Total Beneficiaries :", cursor.fetchone()[0])

# ------------------------------
# Total Hospitals
# ------------------------------
cursor.execute("""
SELECT COUNT(*)
FROM Hospitals
""")

print("Total Hospitals :", cursor.fetchone()[0])

# ------------------------------
# Total Claims
# ------------------------------
cursor.execute("""
SELECT COUNT(*)
FROM Claims
""")

print("Total Claims :", cursor.fetchone()[0])

# ------------------------------
# Fraud Claims
# ------------------------------
cursor.execute("""
SELECT COUNT(*)
FROM Claims
WHERE Fraud_Label='Yes'
""")

print("Fraud Claims :", cursor.fetchone()[0])

# ------------------------------
# Eligible Beneficiaries
# ------------------------------
cursor.execute("""
SELECT COUNT(*)
FROM Beneficiaries
WHERE Eligible='Yes'
""")

print("Eligible Beneficiaries :", cursor.fetchone()[0])

# ------------------------------
# Previous Fraud Hospitals
# ------------------------------
cursor.execute("""
SELECT COUNT(*)
FROM Hospitals
WHERE Previous_Fraud='Yes'
""")

print("Hospitals with Previous Fraud :", cursor.fetchone()[0])

close_connection(connection)
print("=" * 60)