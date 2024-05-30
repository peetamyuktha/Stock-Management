# Stock-management

# Stock Management System

This is a simple Stock Management System implemented in Python using MySQL database for storage. It allows three types of users: Admin, Customer, and Supplier to interact with the stock.

## Features

- **Admin**:
  - Can check the existing stock.
  - Can order more stock.
  - Can exit the system.
  
- **Customer**:
  - Can view existing stock.
  - Can add items to the cart and place orders.
  - Can view total amount to be paid and checkout.
  - Can exit the system.
  
- **Supplier**:
  - Can view remaining orders.
  - Can update the stock by supplying ordered items.
  - Can exit the system.
  
## Setup

1. **Database Setup**:
   - Create a MySQL database named `inventory`.
   - Import the provided SQL file `inventory.sql` to set up the necessary tables.

2. **Python Environment**:
   - Make sure you have Python installed on your system.
   - Install the required dependencies using pip:
     ```
     pip install mysql-connector-python prettytable
     ```

3. **Configuration**:
   - Open the Python script `inventory_management.py` and update the database connection details such as `host`, `user`, `passwd`, and `database` according to your MySQL setup.

4. **Running the Script**:
   - Execute the Python script `inventory_management.py`.
   - Choose the appropriate login option (Admin, Customer, or Supplier) and follow the prompts to interact with the system.

## Usage

- **Admin**: 
  - Login with admin credentials and choose options to check stock, order stock, or exit.

- **Customer**:
  - Login with customer credentials and browse the available stock.
  - Enter the PID of items to add them to the cart.
  - Finish adding items by entering 'F'.
  - View the total amount to be paid and checkout.

- **Supplier**:
  - Login with supplier credentials to view remaining orders.
  - Choose to supply ordered items or exit.
 
# mysql code

- create database
-- Create the database
CREATE DATABASE IF NOT EXISTS inventory;

-- Use the database
USE inventory;

-- Create the admin table
CREATE TABLE IF NOT EXISTS admin (
    id VARCHAR(50) PRIMARY KEY,
    pswd VARCHAR(50)
);

-- Create the customer table
CREATE TABLE IF NOT EXISTS customer (
    id VARCHAR(50) PRIMARY KEY,
    pswd VARCHAR(50)
);

-- Create the supplier table
CREATE TABLE IF NOT EXISTS supplier (
    id VARCHAR(50) PRIMARY KEY,
    pswd VARCHAR(50)
);

-- Create the stock table
CREATE TABLE IF NOT EXISTS stock (
    pid INT AUTO_INCREMENT PRIMARY KEY,
    pname VARCHAR(255),
    price DECIMAL(10, 2),
    quantity INT
);

-- Create the orders table
CREATE TABLE IF NOT EXISTS orders (
    pid INT,
    quantity INT,
    FOREIGN KEY (pid) REFERENCES stock(pid)
);
- inserting values database
  -- Insert sample data into the admin table
INSERT INTO admin (id, pswd) VALUES ('admin1', 'password1'), ('admin2', 'password2');

-- Insert sample data into the customer table
INSERT INTO customer (id, pswd) VALUES ('customer1', 'password1'), ('customer2', 'password2');

-- Insert sample data into the supplier table
INSERT INTO supplier (id, pswd) VALUES ('supplier1', 'password1'), ('supplier2', 'password2');

-- Insert sample data into the stock table
INSERT INTO stock (pname, price, quantity) VALUES 
('Product1', 10.00, 100),
('Product2', 20.00, 150),
('Product3', 30.00, 200);

-- Insert sample data into the orders table
INSERT INTO orders (pid, quantity) VALUES 
(1, 20),
(2, 30),
(3, 40);



<img width="1440" alt="Screenshot 2024-05-11 at 10 20 37 PM" src="https://github.com/chintalapudipiyush/inventory-management/assets/146371407/5afdc0ec-64bd-49cf-9033-8b737cc9bee5">
