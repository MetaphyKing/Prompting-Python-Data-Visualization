import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales": [120, 135, 150, 145, 160, 180]
})

fig, ax = plt.subplots(figsize=(7, 4), dpi=100)
ax.plot(df["month"], df["sales"], marker="o")

ax.set_title("Half-year sales trend")
ax.set_xlabel("Month")
ax.set_ylabel("Sales, units")
ax.grid(True, alpha=0.3)

plt.tight_layout()
fig.savefig("sales_trend.png", dpi=300, bbox_inches="tight")
plt.show()
