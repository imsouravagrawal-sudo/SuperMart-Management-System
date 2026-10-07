# SuperMart Management System

A Python-based SuperMart Management System built as a practical project for managing customers, products, stock, orders, and business information.

## 📌 Project Overview

SuperMart Management System is a console-based Python application that uses an Excel workbook as its data source.

The project was developed to practice Python programming, file handling, Excel data management, modular programming, error handling, logging, and Git/GitHub.

## 🚀 Features

### Customer Management
- View Customers
- Search Customer
- Delete Customer

### Product Management
- View Products
- Search Products
- Update Product Stock
- Restock Products
- Low Stock Report
- Out of Stock Report
- Delete Product

### Order Management
- View Orders
- Search Orders
- Add New Order
- Delete Order

### Dashboard
- Total Customers
- Total Products
- Total Stock
- Low Stock Products
- Out of Stock Products
- Total Orders

### Logging
- Records important activities in a log file
- Tracks selected actions and errors

## 🛠️ Technologies Used

- Python
- OpenPyXL
- Excel
- Git
- GitHub

## 📂 Project Structure

```text
SuperMart_Project/
│
├── data/
│   └── SuperMart_Raw_Data.xlsx
│
├── customers.py
├── products.py
├── orders.py
├── dashboard.py
├── logger.py
├── utils.py
├── main.py
├── .gitignore
└── README.md