
# Minimal imports
import matplotlib.pyplot as plt
import pandas as pd

# Assume df contains 'date' and 'value' columns
fig, ax = plt.subplots(figsize=(8, 4))  # Compact for report layout

ax.plot(df["date"], df["value"], linewidth=2)

ax.set_title("Metric Trend Over Time")
ax.set_xlabel("Date")
ax.set_ylabel("Value")

ax.grid(True, which="major", alpha=0.3)

# Checklist:
# - ticks are readable; - legend does not overlap data;
# - axis labels have units; - no extra dependencies;
# - figure renders without warnings.
plt.tight_layout()
