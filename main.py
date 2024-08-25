import sqlite3

conn = sqlite3.connect("shop.db")

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS products(
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS customers(
    customer_id INTEGER PRIMARY KEY, 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    email TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders(
    order_id INTEGER PRIMARY KEY, 
    customer_id INTEGER NOT NULL, 
    product_id INTEGER NOT NULL, 
    quantity INTEGER NOT NULL, 
    order_date DATE NOT NULL, 
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
''')

conn.commit()

cursor.executemany('''
INSERT INTO products(product_id, name, category, price) 
VALUES (?, ?, ?, ?)
''', [
    (101, "Lenovo", "Техніка", 24000),
    (102, "Redmi", "Смартфони", 4000),
    (103, "Samsung Galaxy s1", "Планшети", 14000),
    (104, "JBL", "Навушники", 500),
    (105, "Philips", "Холодильник", 24000)
])

cursor.executemany('''
INSERT INTO customers(customer_id, first_name, last_name, email)
VALUES (?, ?, ?, ?)
''',[
    (1, "Тарас", "Шевченко", "batkonashbandera@gmail.com"),
    (2, "Іван", "Семиволосов", "batkonashbandera@gmail.com"),
    (3, "Анна", "Ковалевська", "batkonashbandera@gmail.com"),
    (4, "Олексій", "Трамп", "batkonashbandera@gmail.com"),
    (5, "Павло", "Груша", "batkonashbandera@gmail.com"),
])

cursor.executemany('''
INSERT INTO orders(order_id, customer_id, product_id, quantity, order_data)
VALUES (?, ?, ?, ?, ?)
''', [
    (201, 2, 101, 1, "25.08.24"),
    (202, 5, 104, 100, "26.08.24"),
    (203, 3, 105, 3, "19.08.24"),
    (204, 1, 102, 25, "25.07.24"),
    (205, 4, 103, 6, "25.08.23")
])

conn.commit()