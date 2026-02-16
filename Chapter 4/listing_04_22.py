
by_cat = (
    df.groupby("category")["amount"]
      .sum()
      .sort_values(ascending=True)
)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh(by_cat.index, by_cat.values)

ax.set_title("Revenue by category")
ax.set_xlabel("Revenue, units")
ax.grid(True, axis="x", alpha=0.3)

# value labels to the right of bars
for y, v in enumerate(by_cat.values):
    ax.text(v, y, f" {v:,.0f}", va="center")

plt.tight_layout()
plt.show()

num = df[["feature_x", "feature_y"]].dropna()

# gentle trimming by quantiles
lo, hi = num["feature_y"].quantile([0.01, 0.99])
num = num[(num["feature_y"] >= lo) & (num["feature_y"] <= hi)]

