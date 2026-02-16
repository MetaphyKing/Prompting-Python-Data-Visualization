
import matplotlib.pyplot as plt

categories = ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]
values = [120, 90, 150, 110, 95]

order = sorted(zip(values, categories))
vals_sorted, cats_sorted = zip(*order)

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh(cats_sorted, vals_sorted)

ax.set_title("Revenue by category")
ax.set_xlabel("Revenue, units")
ax.grid(True, axis="x", alpha=0.3)

for y, v in enumerate(vals_sorted):
    ax.text(v, y, f" {v:,.0f}", va="center")

plt.tight_layout()
plt.show()
