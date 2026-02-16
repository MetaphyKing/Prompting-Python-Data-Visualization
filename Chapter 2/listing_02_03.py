import sqlite3  
import pandas as pd  

connection = sqlite3.connect("database.db")  
query = "SELECT * FROM sales"  
data = pd.read_sql_query(query, connection)  
print(data.head())  