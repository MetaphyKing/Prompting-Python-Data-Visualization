
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(1)
group_a = rng.normal(10, 2, size=200)
group_b = rng.normal(11, 3, size=200)
group_c = rng.normal(9,  1.5, size=200)

fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.boxplot([group_a, group_b, group_c], labels=["A", "B", "C"])

ax.set_title("Group distribution comparison")
ax.set_ylabel("Value, units")
ax.grid(True, axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
