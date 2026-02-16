import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, df["A"], linewidth=2.4, label="A")
ax.plot(df.index, df["B"], linewidth=2.0, linestyle="--", label="B")
ax.plot(df.index, df["C"], linewidth=2.0, linestyle="-.", label="C")

# Concise, informative labels and left-aligned title
ax.set_title("Trends of three series: focused on readability", 
             loc="left", fontsize=13, fontweight="bold")
ax.set_xlabel("x (rad)", labelpad=6)
ax.set_ylabel("value", labelpad=8)

# Compact, semi-transparent legend without covering data
leg = ax.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.12),
                frameon=True, framealpha=0.9, title="Series")
leg.get_frame().set_linewidth(0.8)

ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, df["A"], label="Control", linewidth=2.6)
ax.plot(df.index, df["B"], label="Variant 1", linestyle="--", alpha=0.9)
ax.plot(df.index, df["C"], label="Variant 2", linestyle="-.", alpha=0.9)

ax.set_title("Comparison with control series", loc="left", fontsize=13, fontweight="bold")
ax.set_xlabel("x (rad)")
ax.set_ylabel("value")
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), frameon=True, framealpha=0.9)
ax.grid(True, axis="y", alpha=0.25)

# Short note outside the axes
fig.text(0.01, 0.02, "Note: control = solid line; variants = dashed.", fontsize=9)

plt.tight_layout()
plt.show()



fig, ax = plt.subplots(figsize=(6.4, 3.6))
xv = df.index.to_numpy()
y = df["A"].to_numpy()

ax.plot(xv[:40], y[:40], label="Observed", linewidth=2.4, color="#2ca02c")
ax.plot(xv[39:], y[39:], label="Forecast", linewidth=2.4, linestyle="--", color="#2ca02c")

ax.set_title("Series A: observed vs short-term forecast", loc="left")
ax.set_xlabel("x (rad)")
ax.set_ylabel("value")
ax.legend(loc="lower right", frameon=True, framealpha=0.9)
ax.grid(True, alpha=0.25)
plt.show()



from matplotlib.lines import Line2D

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, df["A"], color="#4C78A8", linewidth=2.2)
ax.plot(df.index, df["B"], color="#F58518", linewidth=2.2, linestyle="--")
ax.plot(df.index, df["C"], color="#54A24B", linewidth=2.2, linestyle="-.")

legend_handles = [
    Line2D([0], [0], color="#4C78A8", lw=2.2, label="Solid"),
    Line2D([0], [0], color="#F58518", lw=2.2, ls="--", label="Dashed"),
    Line2D([0], [0], color="#54A24B", lw=2.2, ls="-.", label="Dash-dot"),
]
ax.legend(handles=legend_handles, ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.10),
          frameon=True, framealpha=0.9, title="Line types",
          handlelength=1.6, handletextpad=0.5, labelspacing=0.4, borderaxespad=0.4)

ax.set_title("Custom legend: samples instead of raw data", loc="left")
ax.set_xlabel("x (rad)")
ax.set_ylabel("value")
ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.show()



fig, ax = plt.subplots(figsize=(6.8, 3.6))
lines = []
lines += ax.plot(df.index, df["A"], label="Control", linewidth=2.6, color="#4C78A8")
lines += ax.plot(df.index, df["B"], label="Variant 1", linestyle="--", color="#F58518")
lines += ax.plot(df.index, df["C"], label="Variant 2", linestyle="-.", color="#54A24B")

# Enforce order: Control first, then variants
handles, labels = ax.get_legend_handles_labels()
order = [labels.index("Control"), labels.index("Variant 1"), labels.index("Variant 2")]
ax.legend([handles[i] for i in order], [labels[i] for i in order],
          loc="upper left", bbox_to_anchor=(1.02, 1.0), frameon=True, framealpha=0.9)

ax.set_title("Logical legend order and placement outside axes", loc="left")
ax.set_xlabel("x (rad)")
ax.set_ylabel("value")
ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(6.6, 3.6))
ax.plot(df.index, df["A"], linewidth=2.6, label="Control")
ax.plot(df.index, df["B"], linewidth=2.0, linestyle="--", alpha=0.9, label="Variant 1")
ax.plot(df.index, df["C"], linewidth=2.0, linestyle="-.", alpha=0.9, label="Variant 2")

ax.set_title("Comparison: control and two variants", loc="left", fontsize=13, fontweight="bold")
ax.set_xlabel("x (rad)", labelpad=6)
ax.set_ylabel("value", labelpad=8)
ax.grid(True, axis="y", alpha=0.25)

ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), frameon=True, framealpha=0.9, ncol=1)
fig.text(0.01, 0.01, "Note: distinctness ensured by both line style and color.", fontsize=9)

plt.tight_layout()
plt.show()


