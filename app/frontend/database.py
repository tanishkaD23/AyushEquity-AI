import sqlite3
import pandas as pd

def get_beneficiaries():

    conn = sqlite3.connect("app/database/database.db")

    df = pd.read_sql(
        "SELECT * FROM Beneficiaries",
        conn
    )

    conn.close()

    return df