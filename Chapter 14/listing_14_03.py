import matplotlib.dates as mdates
from datetime import datetime

campaign_date = datetime(2024, 9, 1)

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=monthly, x="month", y="sales_a", ax=ax, label="Product A", linewidth=2)
sns.lineplot(data=monthly, x="month", y="sales_b", ax=ax, label="Product B", linewidth=2)

ax.axvline(campaign_date, linestyle="--", linewidth=1)
ax.text(campaign_date, ax.get_ylim()[1]*0.95, "Campaign Start", va="top", ha="left")

ax.set_title("Monthly Sales: Impact of Marketing Campaign")
ax.set_xlabel("Month")
ax.set_ylabel("Units Sold")

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
fig.autofmt_xdate()

ax.grid(True, alpha=0.25)
ax.legend(title="Line", loc="upper left", bbox_to_anchor=(1.02, 1.0), borderaxespad=0)

plt.tight_layout()
plt.show()
