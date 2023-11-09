CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    address VARCHAR(255),
    phone_number VARCHAR(50)
);

INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
    (1, 'Alice Johnson', 'alice@example.com', '123 Main St', '555-1234'),
    (2, 'Bob Smith', 'bob@example.com', '456 Elm St', '555-5678'),
    (3, 'Charlie Brown', 'charlie@example.com', '789 Oak St', '555-9101'),
    (4, 'David White', 'david@example.com', '567 Maple Ave', '555-6789'),
    (5, 'Emma Lee', 'emma@example.com', '890 Cedar Blvd', '555-3456'),
    (6, 'Frank Brown', 'frank@example.com', '321 Birch Ln', '555-7890'),
    (7, 'Grace Miller', 'grace@example.com', '654 Pine Rd', '555-2345'),
    (8, 'Henry Clark', 'henry@example.com', '987 Elm Dr', '555-6789'),
    (9, 'Ivy Turner', 'ivy@example.com', '234 Oak Ct', '555-1234'),
    (10, 'Jack Davis', 'jack@example.com', '876 Maple Way', '555-7890'),
    (11, 'Katherine Moore', 'katherine@example.com', '543 Cedar Ave', '555-2345'),
    (12, 'Liam Adams', 'liam@example.com', '210 Pine St', '555-5678'),
    (13, 'Mia Scott', 'mia@example.com', '753 Elm St', '555-9101'),
    (14, 'Noah King', 'noah@example.com', '132 Oak St', '555-3456'),
    (15, 'Olivia Ward', 'olivia@example.com', '876 Birch St', '555-1234'),
    (16, 'Parker Turner', 'parker@example.com', '459 Cedar St', '555-5678'),
    (17, 'Quinn Lewis', 'quinn@example.com', '753 Maple St', '555-7890'),
    (18, 'Ruby Hayes', 'ruby@example.com', '210 Pine St', '555-2345'),
    (19, 'Samuel Hill', 'samuel@example.com', '543 Oak St', '555-6789'),
    (20, 'Taylor Reed', 'taylor@example.com', '876 Elm St', '555-9101');

SELECT name, email FROM Customers;
SELECT * FROM Customers WHERE id=3;
SELECT * FROM Customers WHERE name LIKE 'A%';
SELECT * FROM Customers ORDER BY name DESC;
SELECT * FROM Customers WHERE address LIKE ID=4;
DELETE FROM Customers WHERE id=2;
SELECT COUNT(*) FROM Customers
SELECT * FROM Customers ORDER BY id LIMIT -1 OFFSET 2;
SELECT * FROM Customers WHERE id > 2 AND name LIKE 'A%';
SELECT * FROM Customers WHERE id < 3 OR name LIKE 's%';
SELECT * FROM Customers WHERE phone_number IS NULL OR phone_number = '';


-- **Problem 1:**

-- - **Prerequisite**: Understand creating tables in SQL / collections in MongoDB
-- - **Problem**: Create a **`Customers`** table / collection with the following fields: **`id`** (unique identifier), **`name`**, **`email`**, **`address`**, and **`phone_number`**.

-- **Problem 2:**

-- - **Prerequisite**: Understand inserting data into SQL tables / MongoDB collections
-- - **Problem**: Insert five rows / documents into the **`Customers`** table / collection with data of your choice.

-- **Problem 3:**

-- - **Prerequisite**: Understand basic data fetching in SQL / MongoDB
-- - **Problem**: Write a query to fetch all data from the **`Customers`** table / collection.

-- **Problem 4:**

-- - **Prerequisite**: Understand how to select specific fields in SQL / MongoDB
-- - **Problem**: Write a query to select only the **`name`** and **`email`** fields for all customers.

-- **Problem 5:**

-- - **Prerequisite**: Understand basic WHERE clause in SQL / MongoDB's find method
-- - **Problem**: Write a query to fetch the customer with the **`id`** of 3.

-- **Problem 6:**

-- - **Prerequisite**: Understand using string patterns in SQL (LIKE clause) / using regex in MongoDB
-- - **Problem**: Write a query to fetch all customers whose **`name`** starts with 'A'.

-- **Problem 7:**

-- - **Prerequisite**: Understand how to order data in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers, ordered by **`name`** in descending order.

-- **Problem 8:**

-- - **Prerequisite**: Understand data updating in SQL / MongoDB
-- - **Problem**: Write a query to update the **`address`** of the customer with **`id`** 4.

-- **Problem 9:**

-- - **Prerequisite**: Understand how to limit results in SQL / MongoDB
-- - **Problem**: Write a query to fetch the top 3 customers when ordered by **`id`** in ascending order.

-- **Problem 10:**

-- - **Prerequisite**: Understand data deletion in SQL / MongoDB
-- - **Problem**: Write a query to delete the customer with **`id`** 2.

-- **Problem 11:**

-- - **Prerequisite**: Understand how to count rows / documents in SQL / MongoDB
-- - **Problem**: Write a query to count the number of customers.

-- **Problem 12:**

-- - **Prerequisite**: Understand how to skip rows / documents in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers except the first two when ordered by **`id`** in ascending order.

-- **Problem 13:**

-- - **Prerequisite**: Understand filtering with multiple conditions in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers whose **`id`** is greater than 2 and **`name`** starts with 'B'.

-- **Problem 14:**

-- - **Prerequisite**: Understand how to use OR conditions in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers whose **`id`** is less than 3 or **`name`** ends with 's'.

-- **Problem 15:**

-- - **Prerequisite**: Understand how to use NULL checks in SQL / MongoDB
-- - **Problem**: Write a query to fetch all customers where the **`phone_number`** field is not set or is null.