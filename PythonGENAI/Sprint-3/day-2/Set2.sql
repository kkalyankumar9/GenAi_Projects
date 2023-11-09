-- **Problem 16:**

-- - **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
-- - **Problem**: Create a **`Restaurants`** table / collection with the fields defined above.

-- **Problem 17:**

-- - **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
-- - **Problem**: Insert five rows / documents into the **`Restaurants`** table / collection with data of your choice.

-- **Problem 18:**

-- - **Prerequisite**: Understand how to order data in SQL / MongoDB
-- - **Problem**: Write a query to fetch all restaurants, ordered by **`average_rating`** in descending order.

-- **Problem 19:**

-- - **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
-- - **Problem**: Write a query to fetch all restaurants that offer **`delivery_available`** and have an **`average_rating`** of more than 4.

-- **Problem 20:**

-- - **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
-- - **Problem**: Write a query to fetch all restaurants where the **`cuisine_type`** field is not set or is null.

-- **Problem 21:**

-- - **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
-- - **Problem**: Write a query to count the number of restaurants that have **`delivery_available`**.

-- **Problem 22:**

-- - **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
-- - **Problem**: Write a query to fetch all restaurants whose **`location`** contains 'New York'.

-- **Problem 23:**

-- - **Prerequisite**: Understand how to use the AVG function in SQL / MongoDB's aggregate functions
-- - **Problem**: Write a query to calculate the average **`average_rating`** of all restaurants.

-- **Problem 24:**

-- - **Prerequisite**: Understand how to limit results in SQL / MongoDB
-- - **Problem**: Write a query to fetch the top 5 restaurants when ordered by **`average_rating`** in descending order.

-- **Problem 25:**

-- - **Prerequisite**: Understand data deletion in SQL / MongoDB
-- - **Problem**: Write a query to delete the restaurant with **`id`** 3.
-- Answers
-- 16
-- Create the Restaurants table
CREATE TABLE Restaurants (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    cuisine_type VARCHAR(100),
    location VARCHAR(255),
    average_rating DECIMAL(3,2),
    delivery_available BOOLEAN
);

-- 17
-- Insert 20 random rows of data into the Restaurants table
INSERT INTO Restaurants (id, name, cuisine_type, location, average_rating, delivery_available)
VALUES
    (1, 'Restaurant A', 'Italian', '123 Main St', 4.5, TRUE),
    (2, 'Restaurant B', 'Mexican', '456 Elm St', 4.2, TRUE),
    (3, 'Restaurant C', 'Chinese', '789 Oak St', 4.0, FALSE),
    (4, 'Restaurant D', 'Indian', '101 Pine St', 4.8, TRUE),
    (5, 'Restaurant E', 'Japanese', '202 Maple Ave', 4.3, TRUE),
    (6, 'Restaurant F', 'American', '303 Cedar St', 4.6, TRUE),
    (7, 'Restaurant G', 'Mediterranean', '404 Birch Ln', 3.9, FALSE),
    (8, 'Restaurant H', 'Thai', '505 Oak St', 4.1, TRUE),
    (9, 'Restaurant I', 'French', '606 Pine Rd', 4.7, TRUE),
    (10, 'Restaurant J', 'Vietnamese', '707 Elm Dr', 3.8, FALSE),
    (11, 'Restaurant K', 'Greek', '808 Cedar Ct', 4.4, TRUE),
    (12, 'Restaurant L', 'Korean', '909 Maple Way', 4.2, TRUE),
    (13, 'Restaurant M', 'Brazilian', '101 Pine St', 4.9, TRUE),
    (14, 'Restaurant N', 'Spanish', '202 Oak St', 3.7, FALSE),
    (15, 'Restaurant O', 'Steakhouse', '303 Pine St', 4.5, TRUE),
    (16, 'Restaurant P', 'Seafood', '404 Cedar St', 4.3, TRUE),
    (17, 'Restaurant Q', 'Vegetarian', '505 Elm St', 4.6, TRUE),
    (18, 'Restaurant R', 'Sushi', '606 Maple St', 4.2, TRUE),
    (19, 'Restaurant S', 'BBQ', '707 Pine St', 4.4, TRUE),
    (20, 'Restaurant T', 'Mexican', '808 Oak St', 4.1, TRUE);
-- 18
SELECT * FROM Restaurants ORDER BY average_rating  DESC
--19
SELECT * FROM Restaurants WHERE delivery_available = TRUE AND average_rating >4;
--20
SELECT * FROM Restaurants WHERE cuisine_type IS NULL OR  cuisine_type=''
--21
SELECT COUNT(*) FROM Restaurants WHERE delivery_available =TRUE 
--22
SELECT * FROM Restaurants WHERE location LIKE '%New York%'
--23
SELECT AVG(average_rating) AS average_rating_average FROM Restaurants;
--24
SELECT * FROM Restaurants ORDER BY average_rating DESC LIMIT 5;
--25

DELETE FROM Restaurants WHERE id = 3;


