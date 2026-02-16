
import numpy as np

daily["revenue_ma7"] = daily["revenue"].rolling(7, min_periods=1).mean()

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(daily["date"], daily["revenue"], alpha=0.5, label="Daily")
ax.plot(daily["date"], daily["revenue_ma7"], label="MA 7")

# annotate the maximum of the smoothed series
i_max = int(np.nanargmax(daily["revenue_ma7"].values))
x_max = daily.loc[i_max, "date"]
y_max = daily.loc[i_max, "revenue_ma7"]
ax.annotate("MA 7 peak", xy=(x_max, y_max), xytext=(x_max, y_max*1.05),
            arrowprops=dict(arrowstyle="->"))

ax.set_title("Daily revenue with moving average")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue, units")
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.show()
