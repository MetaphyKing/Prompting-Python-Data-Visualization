
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Synthetic daily data for 9 months
rng = pd.date_range("2023-01-01", "2023-09-30", freq="D")
values = 100 + np.cumsum(np.random.normal(0, 1.2, size=len(rng)))  # random walk
s = pd.Series(values, index=rng)

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(s.index, s.values, linewidth=1.5)

ax.set_title("Daily Time Series")
ax.set_ylabel("Value")
ax.grid(True, which="both", alpha=0.2)

# Smart auto-formatting of dates
ax.xaxis.set_major_locator(mdates.AutoDateLocator())
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

fig.autofmt_xdate()  # neat tilt of date labels
plt.tight_layout()
plt.show()


start, end = pd.Timestamp("2023-04-01"), pd.Timestamp("2023-06-30")
ax.set_xlim(start, end)  # focus on spring



ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))   # every quarter
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))   # Apr 2023, etc.
ax.xaxis.set_minor_locator(mdates.MonthLocator())             # every month


