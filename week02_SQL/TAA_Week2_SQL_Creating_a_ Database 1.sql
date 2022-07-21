CREATE DATABASE bens_bazaar;

USE bens_bazaar;

CREATE TABLE customer(
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR (30) NOT NULL,
    last_name VARCHAR (50) NOT NULL, 
    date_of_birth DATE NOT NULL,
    address VARCHAR (255) NOT NULL, 
    postcode VARCHAR (8) NOT NULL
);

EXPLAIN customer;

ALTER TABLE customer
MODIFY address VARCHAR (200) NOT NULL; 

CREATE TABLE products(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR (30) NOT NULL,
    price DECIMAL (6,2) NOT NULL,
    depreciated BOOLEAN NOT NULL,
    number_in_stock INT NOT NULL
);

DROP TABLE products;

CREATE TABLE product(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR (30) NOT NULL,
    price DECIMAL (6,2) NOT NULL,
    discontinued BOOLEAN NOT NULL,
    number_in_stock INT NOT NULL
);

EXPLAIN product;

CREATE TABLE orders(
    id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    customer_id INT NOT NULL,
    shipping_address VARCHAR (255) NOT NULL, 
    shipping_postcode VARCHAR (8) NOT NULL,
    shipping_date DATE,
    shipped BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (product_id) REFERENCES product(id),
    FOREIGN KEY (customer_id) REFERENCES customer(id)
);

EXPLAIN orders;

INSERT INTO customer (first_name, last_name, date_of_birth, address, postcode)
VALUES ('Niall', 'Trelfa', '1985-05-14', '1 Test Street, Bristol', 'BA1 8UG'),
('Lanny', 'Smith', '1964-11-01', '253 Poplar Place, London', 'SE28 8BA'),
('Lizzie', 'Jones', '1989-01-21', '47 Hunt Street, Hull', 'HU12 3PN'),
('Devin', 'Strange', '1984-09-30', 'The Glades, Walkden, Manchester', 'M12 3AX'),
('Gabe', 'Rich', '1971-03-11', '29 Waterloo Road, London', 'W2 7XY'),
('Ben', 'Mason', '1989-09-27', '212 Titmuss Avenue, London', 'SE28 8BX'),
('Lauren', 'Carter', '1950-08-04', '1 John Street, Manchester', 'M3 7DX'),
('James', 'Thomas', '1999-02-23', '5 Smith Close, Cambridge', 'C32 1KJ'),
('James', 'Yearsly', '1991-12-17', '4 Dartford Road, Bexely', 'B13 9KO'),
('Emily', 'Hayes', '1983-01-25', '3 Bolton Road, Bolton', 'BO12 3LK');

SELECT * FROM customer;

INSERT INTO product (name, price, discontinued, number_in_stock)
VALUES ('PlayStation 3', 200, 1, 0),
('Playstation 1', 49.99, 1, 0),
('PlayStation 5', 499.99, 0, 10),
('Fifa 21', 39.78, 0, 8),
('Dulux Gaming Chair', 199.99, 0, 5),
('Basic Gaming Chair', 69.50, 0, 3),
('Hi-Spec Gaming Laptop', 2100, 0, 2),
('Laptop Cooling Stand', 17.50, 0, 30),
('Gaming Headphones', 55.55, 0, 20),
('I-Pod', 100, 1, 0),
('Samsung S22 Ultra', 1536.87, 0, 0);

SELECT name, price FROM product
WHERE discontinued = 0;

INSERT INTO orders (product_id, customer_id, shipping_address, shipping_postcode, shipping_date, shipped)
VALUES (1, 2, '253 Poplar Place, London', 'SE28 8BA', '2005-03-24', 1),
(7, 6, '70 Washington Street, Hull', 'HU5 1DK', '2020-05-03', 1),
(11, 6, '212 Titmuss Avenue, London', 'SE28 8BX', '2022-11-01',0),
(9, 8, '5 Smith Close, Cambridge', 'C32 1KJ', '2021-10-15', 1),
(8, 8, '5 Smith Close, Cambridge', 'C32 1KJ', '2021-10-15', 1),
(7, 1, '1 Test Street, Bristol', 'BA1 8UG', '2022-06-25', 0),
(8, 1, '1 Test Street, Bristol', 'BA1 8UG', '2022-06-25', 0),
(10, 5, '101 Manchester Road, Manchester', 'M28 3NT', '2002-02-20', 1 ),
(4, 3, '47 Hunt Street, Hull', 'HU12 3PN', '2022-05-01', 1),
(4, 10, '3 Bolton Road, Bolton', 'BO12 3LK', '2022-06-23', 0);

SELECT * FROM orders
WHERE shipped = 0;

DELETE FROM orders
WHERE id = 7;

SELECT * FROM orders;

Update product
SET price = 35.50
WHERE id = 4 AND name = 'Fifa 21';