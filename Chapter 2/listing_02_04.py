import requests  
import pandas as pd  

url = "https://api.exchangerate.host/latest?base=USD"  
response = requests.get(url)  
data_json = response.json()  
print(data_json["rates"]["EUR"])  