import pandas as pd
import sqlite3


#Load cleaned csv file 
df = pd.read_csv("data/sales_cleaned.csv")

#connect the sales database
conn = sqlite3.connect("sales.db")

#Load data into sql table
df.to_sql("sales",conn,if_exists="replace",index=False)

#Test base query 
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in database:", tables)

print("Data is successfully loaded into SQLite3")

#close the connnection
conn.close()