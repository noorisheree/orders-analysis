import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

print("Customer orders (joined):")

cursor.execute("""
SELECT customers.name, orders.amount
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
""")

for row in cursor.fetchall():
    print(row)

print("\nTotal spend per customer:")

cursor.execute("""
SELECT customers.name, SUM(orders.amount) AS total_spent
FROM customers
INNER JOIN orders
ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_id, customers.name
ORDER BY total_spent DESC
""")

for row in cursor.fetchall():
    print(row)
    
conn.close()