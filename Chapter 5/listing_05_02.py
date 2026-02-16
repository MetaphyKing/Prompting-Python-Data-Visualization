import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, df["A"], linewidth=2.4, marker="o", markersize=4, label="A (primary)")
ax.plot(df.index, df["B"], linewidth=1.8, linestyle="--", alpha=0.9, label="B (comparison)")
ax.plot(df.index, df["C"], linewidth=1.8, linestyle="-.", marker="s", markersize=3, alpha=0.9, label="C (detail)")
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_xlabel("x (rad)")
ax.set_ylabel("value")
ax.set_title("Contrasting lines, dashes, and markers for visual hierarchy")
plt.show()


fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, df["A"], color="#1f77b4", linewidth=2.2, marker="o", markersize=4, markevery=4, label="A (every 4th)")
ax.plot(df.index, df["B"], color="#ff7f0e", linewidth=2.0, linestyle="--", alpha=0.8, label="B (no markers)")
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_title("Selective markers for clarity")
plt.show()


fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index[:40], df["A"].iloc[:40], color="#2ca02c", linewidth=2.4, label="Observed")
ax.plot(df.index[39:], df["A"].iloc[39:], color="#2ca02c", linewidth=2.4, linestyle="--", label="Forecast")
ax.legend()
ax.grid(True, alpha=0.3)
ax.set_title("Semantic line styles: solid = observed, dashed = forecast")
plt.show()
