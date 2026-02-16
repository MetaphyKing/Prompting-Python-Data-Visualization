# Uncertainty bands and “visualization passport”
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText

rng = np.random.default_rng(1)
x = np.linspace(0, 10, 200)
samples = [np.sin(x) + 0.3*rng.standard_normal(len(x)) for _ in range(300)]
arr = np.vstack(samples)
mean = arr.mean(axis=0)
low, high = np.percentile(arr, [2.5, 97.5], axis=0)

fig, ax = plt.subplots()
ax.plot(x, mean, linewidth=2)
ax.fill_between(x, low, high, alpha=0.25)

ax.set_xlabel("time, s")
ax.set_ylabel("value")
ax.set_title("Trend and 95% Confidence Interval")

explain = AnchoredText(
    "Explanation: showing a bootstrap-based 95% confidence interval of the mean; "
    "no logarithmic scales applied; raw data available in the repository.",
    loc="lower right", prop={"size":8}, frameon=True
)
ax.add_artist(explain)

passport = AnchoredText(
    "Source: sensor_v2.csv, window 2019–2024; filters: removed NaN; code: commit a1b2c3",
    loc="upper left", prop={"size":8}, frameon=True
)
ax.add_artist(passport)

plt.tight_layout()
plt.show()

# Simple “honesty linter” for bar charts
def lint_bar(ax):
    messages = []
    x0, x1 = ax.get_xlim(); y0, y1 = ax.get_ylim()
    if any(isinstance(ch, plt.Rectangle) and ch.get_height()!=0 for ch in ax.get_children()):
        if abs(y0) > 1e-12 and abs(y1) > 1e-12 and y0 != 0:
            messages.append("Y-axis in bar chart does not start at zero.")
    if not ax.get_xlabel() or not ax.get_ylabel():
        messages.append("Missing axis labels.")
    if not ax.get_title():
        messages.append("Missing chart title.")
    return messages
