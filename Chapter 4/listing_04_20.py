import matplotlib.dates as mdates

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(daily["date"], daily["revenue"])

# time locators and formatters
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(
    mdates.ConciseDateFormatter(ax.xaxis.get_major_locator())
)

ax.set_title("Daily revenue")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue, units")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


