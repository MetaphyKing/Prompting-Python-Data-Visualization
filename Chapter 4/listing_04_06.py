import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 200)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y)

# annotation in Axes coordinates: 0.02, 0.95  -  top-left corner of the Axes
ax.text(0.02, 0.95, "Signal sin(x)", transform=ax.transAxes, va="top")

ax.set_title("Axes coordinate systems demo")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
