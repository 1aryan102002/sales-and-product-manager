# 🛒 Sales and Product Manager

This is a **Sales and Product Management System** created using **Python** and **MySQL**. The project is built to help manage customers, orders, and sales data through a simple command-line interface (CLI).

It is especially useful for small businesses or academic use, and is designed with modular code for clarity and future scalability.

---

## 🔧 Features

- 👤 **Customer Management**  
  - Register and store customer details  
  - Secure login system  

- 📦 **Order Management**  
  - Place and track product orders  
  - Retrieve order history  
  - Calculate pricing based on product database  

- 📊 **Sales Management**  
  - Maintain records of all sales  
  - Employee-accessible dashboard to view sales history  
  - Sales data can be filtered and analyzed

---

## 📁 Project Structure

```
sales-and-product-manager/
│
├── customer.py       # Handles customer registration and login
├── order.py          # Manages order placement and order history
├── product.py        # (Optional) Handles product management (to be added)
├── sales.py          # Displays and tracks sales history
├── db.py             # Connects to MySQL database
└── README.md         # Project documentation
```

---

## 🧰 Tech Stack

- **Programming Language**: Python 3.x  
- **Database**: MySQL (via `mysql-connector-python`)  
- **Interface**: Command Line (CLI)

---

## 🗃️ Database Schema

You must create a MySQL database and the following tables:

### 🧑 customers
```sql
CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coustomer_name VARCHAR(100) NOT NULL,
    phone int not null,
    email VARCHAR(100) unique not null,
    address varchar(100) not null
);
```

### 📦 orders
```sql
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id VARCHAR(100),
    quantity INT,
    price DECIMAL(10, 2),
    order_at DATETIME,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

### 🧾 sales
```sql
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coustomer_id int,
    product_id int,
    quanty int,
    sale_date datetime,
    price decimal(10,2)
    foreign key (coustomer_id) references coustomer (id),
    foreign key (product_id) references product(product_id) 
);
```
### product 
```sql
CREATE TABLE product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    price decimal(10,2),
    stock int,
    quanty int
    );
```
### users
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(100),
    user_last_name varchar (100),
    password_user varchar(100),
    role varchar(20)
    );
```
## 🚀 How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/sales-and-product-manager.git
   cd sales-and-product-manager
   ```

2. **Install Dependencies**
   Make sure you have Python 3 installed. Then run:
   ```bash
   pip install mysql-connector-python
   ```

3. **Configure the Database**
   - Open `db.py` and enter your MySQL credentials and database name.
   - in config.py according to your mysql database enter the credentials it ask 

4. **Create the Tables**
   Use the SQL queries mentioned above in your MySQL terminal or MySQL Workbench to create the tables.

5. **Run Modules**
   You can run each script individually from the terminal:
   ```bash
   python customer.py
   python order.py
   python sales.py
   and others 
   ```

---

## 🎯 Future Enhancements

- Add product inventory module
- Admin dashboard with password authentication
- Export reports as CSV
- GUI interface using Tkinter or Flask
- Integrate with Django backend

---

## 🙋‍♂️ About the Author

**Aryan (aka Aelu )**  
🎮 junior Backend engineer and Game/Level Designer & Developer  
💻 Python | Unreal | MYSQL | MongoDB | Unity | Power-Bi | C++ | C# | c | DSA 
📫 Reach me at: aryansharma102003@gmail.com 
🌐 Portfolio: Coming soon! but here is my level design portfolio :- https://splendid-imagine-714456.framer.app/


---

