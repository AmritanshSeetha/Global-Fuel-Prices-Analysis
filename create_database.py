import pandas as pd
import sqlite3
import os

csv_file = "global_fuel_prices_cleaned.csv"
db_file = "global_fuel_prices.db"

# Read the cleaned CSV dataset
df = pd.read_csv(csv_file)

# Create SQLite database
conn = sqlite3.connect(db_file)

# Store dataset in SQL table
df.to_sql("fuel_prices", conn, if_exists="replace", index=False)

# Verify database
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM fuel_prices")
total_rows = cursor.fetchone()[0]

print("Database created successfully!")
print("Table name: fuel_prices")
print("Total records:", total_rows)
print("Database location:", os.path.abspath(db_file))

conn.close()