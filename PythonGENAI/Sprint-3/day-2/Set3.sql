CREATE TABLE Rides (
    id INT PRIMARY KEY,
    driver_id INT,
    passenger_id INT,
    start_location VARCHAR(255),
    end_location VARCHAR(255),
    distance DECIMAL(5,2),
    ride_time DECIMAL(5,2),
    fare DECIMAL(6,2)
);

INSERT INTO Rides (id, driver_id, passenger_id, start_location, end_location, distance, ride_time, fare)
VALUES 
(1, 101, 201, 'Location A', 'Location B', 10.5, 15.3, 25.50),
(2, 102, 202, 'Location C', 'Location D', 8.2, 12.5, 20.75),
(3, 103, 203, 'Location E', 'Location F', 5.7, 8.9, 15.20),
(4, 104, 204, 'Location G', 'Location H', 3.9, 6.2, 10.50),
(5, 105, 205, 'Location I', 'Location J', 12.3, 18.7, 30.80),
(6, 106, 206, 'Location K', 'Location L', 9.8, 14.5, 24.00),
(7, 107, 207, 'Location M', 'Location N', 7.2, 10.8, 18.50),
(8, 108, 208, 'Location O', 'Location P', 6.5, 9.3, 16.75),
(9, 109, 209, 'Location Q', 'Location R', 4.3, 7.1, 12.40),
(10, 110, 210, 'Location S', 'Location T', 11.6, 17.2, 28.90);

SELECT * FROM Rides ORDER BY fare  DESC
SELECT SUM(distance) AS total_distance , SUM(fare) AS total_fare FROM Rides
SELECT AVG(ride_time) AS average_ride_time FROM Rides;
SELECT * FROM Rides WHERE start_location LIKE '%Downtown%' OR end_location LIKE '%Downtown%';
SELECT COUNT(driver_id) FROM Rides

UPDATE Rides SET fare = 25.5 WHERE id = 4;
SELECT driver_id, SUM(fare) AS total_fare FROM Rides GROUP BY driver_id;
DELETE FROM Rides WHERE id = 2;
