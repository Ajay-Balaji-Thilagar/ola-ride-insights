import sqlite3
import pandas as pd

# Connect to the database
db_path = r'A:\ajay\Labmentix_Internship\OLA_Project_7\ola_database.db'
conn = sqlite3.connect(db_path)

# Test Query 2: Average ride distance by vehicle type
query_2 = "SELECT Vehicle_Type, ROUND(AVG(Ride_Distance), 2) as Avg_Ride_Distance FROM ola_rides GROUP BY Vehicle_Type;"
result_2 = pd.read_sql_query(query_2, conn)
print("Query 2 Result: Average Ride Distance by Vehicle Type")
print(result_2)
print("\n")

# Test Query 3: Total cancelled rides by customer
query_3 = "SELECT COUNT(*) as Total_Cancelled_By_Customer FROM ola_rides WHERE Booking_Status = 'Canceled by Customer';"
result_3 = pd.read_sql_query(query_3, conn)
print("Query 3 Result: Total Cancelled Rides by Customer")
print(result_3)
print("\n")

# Test Query 9: Total booking value of successful rides
query_9 = "SELECT SUM(Booking_Value) as Total_Booking_Value FROM ola_rides WHERE Booking_Status = 'Success';"
result_9 = pd.read_sql_query(query_9, conn)
print("Query 9 Result: Total Booking Value of Successful Rides")
print(result_9)

# Close connection
conn.close()