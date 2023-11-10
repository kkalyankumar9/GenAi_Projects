--Problem: Write a query to find the ride with the highest and lowest fare.
SELECT * FROM Rides WHERE fare=(SELECT MAX(fare) FROM Rides)
SELECT * FROM Rides WHERE fare=(SELECT MIN(fare) FROM Rides)
--Problem: Write a query to find the average fare and distance for each driver_id.
SELECT driver_id, AVG(fare) AS average_fare, AVG(distance) AS average_distance FROM Rides GROUP BY driver_id;
 --Write a query to find driver_id that have completed more than 5 rides.
SELECT driver_id, COUNT(*) AS ride_count
FROM Rides
GROUP BY driver_id
HAVING COUNT(*) > 5;

--Problem: Assuming there is another collection/table called Drivers with driver_id and name fields, write a query to find the name of the driver with the highest fare.
SELECT Drivers.name
FROM Riders
INNER JOIN Drivers ON Riders.driver_id = Drivers.driver_id
ORDER BY Riders.fare DESC
LIMIT 1;
--Problem: Write a query to find the top 3 drivers who have earned the most from fares. Return the drivers' ids and total earnings.
SELECT driver_id, SUM(fare) AS total_earnings
FROM Riders
GROUP BY driver_id
ORDER BY total_earnings DESC
LIMIT 3;
--Problem: Assuming there's a ride_date field of date type in the Rides table / collection, write a query to find all rides that happened in the last 7 days.
SELECT *
FROM Rides
WHERE ride_date >= CURDATE() - INTERVAL 7 DAY;
--Write a query to find all rides where the end_location is not set.
SELECT *
FROM Rides
WHERE end_location IS NULL;

--Problem: Write a query to calculate the fare per mile for each ride and return the ride ids and their fare per mile, ordered by fare per mile in descending order.
SELECT ride_id, fare / distance AS fare_per_mile
FROM Rides
ORDER BY fare_per_mile DESC;
--Problem: Assuming there's another collection/table Passengers with passenger_id and name fields, write a query to return a list of all rides including the driver's name and passenger's name.


SELECT R.ride_id, D.name AS driver_name, P.name AS passenger_name
FROM Rides R
JOIN Drivers D ON R.driver_id = D.driver_id
JOIN Passengers P ON R.passenger_id = P.passenger_id;
--Problem: Write a query to add a tip field to the Rides table / collection.
ALTER TABLE Rides
ADD COLUMN tip DECIMAL(10, 2);
