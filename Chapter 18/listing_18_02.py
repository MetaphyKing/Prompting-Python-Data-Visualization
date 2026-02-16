# Switching scatter → hexbin adaptively
import numpy as np
import matplotlib.pyplot as plt

def adaptive_scatter(ax, x, y, density_threshold=2000, gridsize=40):
    ax.clear()
    n = len(x)
    area = (ax.get_xlim()[1]-ax.get_xlim()[0]) * (ax.get_ylim()[1]-ax.get_ylim()[0])
    density = n / max(area, 1e-6)
    if n < density_threshold or density < density_threshold:
        ax.scatter(x, y, s=10, alpha=0.6)
        ax.set_title("mode: scatter")
    else:
        ax.hexbin(x, y, gridsize=gridsize)
        ax.set_title("mode: hexbin")
    ax.figure.canvas.draw_idle()

rng = np.random.default_rng(42)
x = rng.normal(size=50_000)
y = 0.5 * x + rng.normal(scale=0.7, size=x.size)
fig, ax = plt.subplots()
ax.set_xlim(x.min(), x.max())
ax.set_ylim(y.min(), y.max())
adaptive_scatter(ax, x, y)
plt.show()
