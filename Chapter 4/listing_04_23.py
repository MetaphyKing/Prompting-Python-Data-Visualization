fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(daily["date"], daily["revenue"])

ax.set_yscale("log")            # logarithmic scale on y
ax.margins(x=0.01, y=0.05)      # small edge margins
ax.set_title("Dynamics in log scale")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue, units (log)")
ax.grid(True, which="both", alpha=0.3)

plt.tight_layout()
plt.show()
