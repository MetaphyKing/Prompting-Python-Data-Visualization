import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

x = np.linspace(0, 10, 800)
y = np.sin(x) + 0.2*np.sin(7*x)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, lw=1.6)
ax.grid(True, alpha=0.25)

# NOTE: Inset axes can easily obscure important regions (especially on dense plots).
# If key features are covered, change loc/size or move the inset elsewhere.
# Prefer a transparent background and a light frame so the inset does not dominate.
axins = inset_axes(ax, width="35%", height="55%", loc="upper right")
axins.set_facecolor("none")  # transparent background

axins.plot(x, y, lw=1.2)
axins.set_xlim(4, 6)
mask = (x >= 4) & (x <= 6)
axins.set_ylim(y[mask].min(), y[mask].max())
axins.grid(True, alpha=0.2)

# Connector lines and a light rectangle outline
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.tight_layout()
plt.show()
