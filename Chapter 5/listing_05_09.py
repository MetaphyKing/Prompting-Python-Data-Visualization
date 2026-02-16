
import pandas as pd
import matplotlib.dates as mdates

ts = pd.date_range("2024-01-01", periods=60, freq="D")
y = np.sin(np.linspace(0, 3*np.pi, len(ts))) + 0.1*rng.standard_normal(len(ts))

fig, ax = plt.subplots(figsize=(6.8, 3.6))
ax.plot(ts, y, color="#54A24B", linewidth=2.2)
locator = mdates.AutoDateLocator(minticks=4, maxticks=8)
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.tick_params(axis="x", rotation=0)
ax.grid(True, axis="y", alpha=0.25)
ax.set_title("Compact date labels (ConciseDateFormatter)", loc="left")
plt.tight_layout()
plt.show()
