import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_daily.csv", parse_dates=["date"])

monthly = (
    df.set_index("date")
      .resample("M")
      .agg({"sales_a": "sum", "sales_b": "sum"})
      .rename_axis("month")
      .reset_index()
)

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly, x="month", y="sales_a", ax=ax, label="Product A")
sns.lineplot(data=monthly, x="month", y="sales_b", ax=ax, label="Product B")

ax.set_title("Monthly Sales: Comparing Product Lines")
ax.set_xlabel("Month")
ax.set_ylabel("Units Sold")

ax.xaxis.set_major_formatter(
    plt.matplotlib.dates.DateFormatter("%b %Y")
)
fig.autofmt_xdate()

ax.grid(True, alpha=0.3)
ax.legend(title="Line", loc="upper left", bbox_to_anchor=(1.02, 1.0), borderaxespad=0)

plt.tight_layout()
plt.show()
