import pandas as pd 

#Load JSON
df = pd.read_json("data/sales.json")

#show first rows 
print("\n---Data Preview---")
print(df.head())

#Shape 
print("Shape")
print(df.shape)

#Show column names
print("Coloums")
print(df.columns.tolist())

#Show data types
print("Data types")
print(df.dtypes)


#Missing values
print("Missing Values")
print(df.isnull().sum())


#Show basic statistics 
print("summary")
print(df.describe(include="all"))