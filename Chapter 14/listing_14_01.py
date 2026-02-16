import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_daily.csv", parse_dates=["date"])
plt.figure(figsize=(10, 5))
sns.lineplot(data=df, x="date", y="sales_a", label="Product A")
sns.lineplot(data=df, x="date", y="sales_b", label="Product B")
plt.title("Daily Sales")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.legend()
plt.show()
