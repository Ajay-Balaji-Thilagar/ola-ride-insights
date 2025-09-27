import pandas as pd
import sqlite3
from pathlib import Path

# Define paths
csv_path = r'A:\ajay\Labmentix_Internship\OLA_Project_7\cleaned_ola_data.csv'
db_path = r'A:\ajay\Labmentix_Internship\OLA_Project_7\ola_database.db'

# Load cleaned CSV
ola_df = pd.read_csv(csv_path)

# Create SQLite database and connection
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Write DataFrame to SQLite (table name: ola_rides)
ola_df.to_sql('ola_rides', conn, if_exists='replace', index=False)

# Commit and close connection
conn.commit()
conn.close()

print(f"Database created successfully at {db_path}")