import pandas as pd 

df = pd.read_json("data/sales.json")

#convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"],errors="coerce")

#Filling the missing value and 
df["price"] = df["price"].fillna(df['price'].mean())

#Filling the mssing value of order date
df["order_date"] = df["order_date"].fillna(df["order_date"].mode()[0])

#Add a new coloumn : total amount 
df["total_amount"] = df["quantity"] * df["price"]

#To chceck that there are no duplicates
print("Duplicated rows:",df.duplicated().sum())

#to check the order of date
df["order_date"] = pd.to_datetime(df["order_date"]) 

#to ensure the class type of price and quantity
df["price"] = df["price"].astype(float)
df["quantity"] = df["quantity"].astype(int)


print(df[["order_id","customer_name","product","quantity","price","total_amount","order_date"]])

df.to_csv("data/sales_cleaned.csv",index=False)
