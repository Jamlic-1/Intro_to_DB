-- Create Database
CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

-- Create Authors Table
CREATE TABLE authors (
  author_id INT PRIMARY KEY,
  author_name VARCHAR(215)
);

-- Create Books Table
CREATE TABLE books (
  book_id INT PRIMARY KEY,
  title VARCHAR(130),
  author_id INT,
  price DOUBLE,
  publication_date DATE,
  FOREIGN KEY (author_id) REFERENCES authors(author_id)
);

-- Create Customers Table
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(215),
  email VARCHAR(215),
  address TEXT
);

-- Create Orders Table
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create Order_Details Table
CREATE TABLE order_details (
  orderdetailid INT PRIMARY KEY,
  order_id INT,
  book_id INT,
  quantity DOUBLE,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (book_id) REFERENCES books(book_id)
);
