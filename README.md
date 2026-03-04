# Employee Management System

A console-based Employee Management System built using **Python** and **MySQL**.

This project demonstrates how to connect Python to a MySQL database and perform full CRUD (Create, Read, Update, Delete) operations.

---

## 📌 Features

- Add new employees
- View all employee records
- Update employee salary
- Delete employee records
- Menu-driven console interface

---

## 🛠 Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- Git & GitHub

---

## 🗄 Database Setup

Run the following SQL commands in MySQL:

```sql
CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employee (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10,2)
);
