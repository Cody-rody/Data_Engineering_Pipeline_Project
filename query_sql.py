import sqlite3
import pandas as pd 

#Connect the database
conn = sqlite3.connect("sales.db")

#trying queries 
#First 5 rows 
query1 = "SELECT * FROM  sales LIMIT 5;"
df_preview = pd.read_sql_query(query1,conn)
print("First 5 rows")
print(df_preview)

#Total sales value
query2 = "SELECT ROUND(SUM(total_amount),2)AS total_sales FROM sales"
df_total = pd.read_sql_query(query2,conn)
print("Sum of total values of sales")
print(df_total)

query3 = """
SELECT customer_name, SUM(total_amount) AS total_spent
FROM sales
GROUP BY customer_name
ORDER BY total_spent DESC;
"""

df_customers = pd.read_sql_query(query3,conn)
print("Top Customers by Total Purchase")
print(df_customers)

query4=  """
SELECT product, SUM(quantity) AS total_qty, SUM(total_amount) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;
"""

df_Best_product = pd.read_sql_query(query4,conn)
print("Best Selling product from company")
print(df_Best_product)

query5 = """
SELECT city, SUM(total_amount) AS city_sales
FROM sales
GROUP BY city
ORDER BY city_sales DESC;
"""
df_city = pd.read_sql_query(query5,conn)
print("City wise Sales distribution")
print(df_city)

query6="""
SELECT strftime('%Y-%m', order_date) AS month, SUM(total_amount) AS monthly_sales
FROM sales
GROUP BY month
ORDER BY month;
"""
df_month = pd.read_sql_query(query6,conn)
print("Monthly sales")
print(df_month)

query7 = """
SELECT order_id, customer_name, total_amount
FROM sales
ORDER BY total_amount DESC
LIMIT 1;
"""
df_highest = pd.read_sql_query(query7,conn)
print("Highest Single order value")
print(df_highest)


#Close the connection
conn.close()
