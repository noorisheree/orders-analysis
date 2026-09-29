import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    city TEXT
)
""")

cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

customers = [
    (1, "Ali", "Islamabad"),
    (2, "Sara", "Lahore"),
    (3, "Bilal", "Islamabad"),
    (4, "Ayesha", "Karachi"),
    (5, "Hamza", "Lahore"),
    (6, "Zainab", "Karachi")
]

orders = [
    (1, 1, 4500),
    (2, 1, 7200),
    (3, 2, 3000),
    (4, 2, 5800),
    (5, 3, 9800),
    (6, 4, 4000),
    (7, 5, 5800),
    (8, 6, 2500),
    (9, 3, 6200),
    (10, 4, 7000)
]

cursor.executemany(
    "INSERT INTO customers VALUES (?, ?, ?)",
    customers
)

cursor.executemany(
    "INSERT INTO orders VALUES (?, ?, ?)",
    orders
)

conn.commit()
conn.close()

print("orders.db created successfully with 6 customers and 10 orders.")