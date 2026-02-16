
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(df["date"], df["value"], linewidth=2)
ax.set_xlabel("Date"); ax.set_ylabel("Value")
ax.grid(True, alpha=0.3)
ax.legend(["Metric"], loc="upper right")
plt.tight_layout()
