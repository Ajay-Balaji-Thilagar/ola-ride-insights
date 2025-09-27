-- File: ola_queries.sql
-- Project: OLA Ride Insights
-- Description: SQL queries to extract insights from OLA ride-sharing data

-- 1. Retrieve all successful bookings
SELECT *
FROM ola_rides
WHERE Booking_Status = 'Success';

-- 2. Find the average ride distance for each vehicle type
SELECT Vehicle_Type, ROUND(AVG(Ride_Distance), 2) as Avg_Ride_Distance
FROM ola_rides
GROUP BY Vehicle_Type;

-- 3. Get the total number of cancelled rides by customers
SELECT COUNT(*) as Total_Cancelled_By_Customer
FROM ola_rides
WHERE Booking_Status = 'Canceled by Customer';

-- 4. List the top 5 customers who booked the highest number of rides
SELECT Customer_ID, COUNT(*) as Total_Rides
FROM ola_rides
GROUP BY Customer_ID
ORDER BY Total_Rides DESC
LIMIT 5;

-- 5. Get the number of rides cancelled by drivers due to personal and car-related issues
SELECT COUNT(*) as Cancelled_Due_Personal_Car
FROM ola_rides
WHERE Booking_Status = 'Canceled by Driver'
AND Canceled_Rides_by_Driver = 'Personal & Car related issue';

-- 6. Find the maximum and minimum driver ratings for Prime Sedan bookings
SELECT MAX(Driver_Ratings) as Max_Driver_Rating, MIN(Driver_Ratings) as Min_Driver_Rating
FROM ola_rides
WHERE Vehicle_Type = 'Prime Sedan'
AND Driver_Ratings > 0;

-- 7. Retrieve all rides where payment was made using UPI
SELECT *
FROM ola_rides
WHERE Payment_Method = 'UPI';

-- 8. Find the average customer rating per vehicle type
SELECT Vehicle_Type, ROUND(AVG(Customer_Rating), 2) as Avg_Customer_Rating
FROM ola_rides
WHERE Customer_Rating > 0
GROUP BY Vehicle_Type;

-- 9. Calculate the total booking value of rides completed successfully
SELECT SUM(Booking_Value) as Total_Booking_Value
FROM ola_rides
WHERE Booking_Status = 'Success';

-- 10. List all incomplete rides along with the reason
SELECT Booking_ID, Incomplete_Rides_Reason
FROM ola_rides
WHERE Incomplete_Rides = 'Yes';
