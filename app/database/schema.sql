import sqlite3

DATABASE = "app/database/database.db"
SCHEMA = "app/database/schema.sql"

conn = sqlite3.connect(DATABASE)

cursor = conn.cursor()

print("Connected to SQLite Database")

with open(SCHEMA, "r") as file:
    sql_script = file.read()

cursor.executescript(sql_script)

conn.commit()

conn.close()

print("Database Created Successfully!")
print("All Tables Created Successfully!")