import matplotlib.pyplot as plt

daily = (
    df.set_index("date")
      .resample("D")["amount"].sum()
      .rename("revenue")
      .to_frame()
      .reset_index()
)

fig, ax = plt.subplots(figsize=(8, 4.5), dpi=110)
ax.plot(daily["date"], daily["revenue"], marker="")

ax.set_title("Daily revenue")
ax.set_xlabel("Date")
ax.set_ylabel("Revenue, units")
ax.grid(True, alpha=0.3)

plt.tight_layout()
fig.savefig("daily_revenue.png", dpi=300, bbox_inches="tight")
plt.show()
