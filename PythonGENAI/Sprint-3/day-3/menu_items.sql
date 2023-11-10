CREATE TABLE menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    availability BOOLEAN NOT NULL
);
INSERT INTO menu_items (id, name, price, availability) VALUES
(1, 'Pasta', 12.99, 1),  
(2, 'Pizza', 14.99, 1),  
(3, 'Burger', 9.99, 0),  
(4, 'Salad', 7.99, 1),   
(5, 'idli', 12.99, 0),   
(6, 'dosa', 12.99, 1),
(7, 'Steak', 19.99, 1),   
(8, 'Sushi', 22.50, 1),   
(9, 'Fish and Chips', 15.75, 1),  
(10, 'Chicken Curry', 13.99, 0),  
(11, 'Vegetable Stir Fry', 11.50, 1),  
(12, 'Lasagna', 18.75, 1); 

USE foodie_haven;

CREATE TABLE menu_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    availability BOOLEAN NOT NULL
);
