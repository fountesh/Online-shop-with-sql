import sqlite3

conn = sqlite3.connect("shop.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
);
''')

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE 
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    order_date DATE NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

cursor.executemany("""
INSERT INTO products (product_id, name, category, price) VALUES (?, ?, ?, ?)
""", [
    (101, 'Lenovo', 'Ноутбуки', 24000),
    (102, 'Redmi note 4', 'Смартфони', 5000),
    (103, 'Samsung galaxy S1', 'Планшети', 10000),
    (104, "JBL", 'Навушники', 500),
    (105, "Philips", "Холодильники", 50000)
])

cursor.executemany("""
INSERT INTO customers (customer_id, first_name, last_name, email) VALUES (?, ?, ?, ?)
""", [
    (1, 'Тарас', "Шевченко", "batkonashbandera@gmail.com"),
    (2, 'Леся', "Українка", "coolpysmennik@gmail.com"),
    (3, 'Віталій', "Семиволос", "wowsoinsane@gmail.com"),
    (4, 'Андрій', "Андрійович", "aaaaa8777@gmail.com"),
    (5, "Павло", "Трамп", "realtrumpofficialll@gmail.com")
])

cursor.executemany("""
INSERT INTO orders (order_id, customer_id, product_id, quantity, order_date) VALUES (?, ?, ?, ?, ?)
""", [
    (201, 2, 101, 1, "25.08.2024"),
    (202, 5, 104, 100, "01.01.1488"),
    (203, 1, 105, 3, "10.02.2010"),
    (204, 3, 102, 2, "24.07.2023"),
    (205, 4, 103, 5, "27.09.1945")
])

conn.commit()