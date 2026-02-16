import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
x = rng.normal(size=5000)
y = 0.7*x + rng.normal(scale=0.7, size=5000)

fig, ax = plt.subplots(figsize=(7.5, 4.5))
hb = ax.hexbin(x, y, gridsize=35)
cb = fig.colorbar(hb, ax=ax, pad=0.02)
cb.set_label("Count")

ax.set_title("Relationship at high point density")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
