import sqlite3
import pandas as pd

# Connect to the database
db_path = r'A:\ajay\Labmentix_Internship\OLA_Project_7\ola_database.db'
conn = sqlite3.connect(db_path)

# Test query: Fetch first 5 rows
query = "SELECT * FROM ola_rides LIMIT 5;"
result = pd.read_sql_query(query, conn)
print(result)

# Close connection
conn.close()