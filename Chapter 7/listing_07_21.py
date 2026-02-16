import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MaxNLocator, MultipleLocator, FixedLocator)

x = np.linspace(0, 23, 240)
y = 2*np.sin(x/3) + 0.2*np.random.randn(len(x))

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, lw=1.8)

ax.xaxis.set_major_locator(MaxNLocator(nbins=6))         # keep ~6 ticks
ax.xaxis.set_minor_locator(MultipleLocator(base=1.0))    # minor ticks every 1.0
ax.xaxis.set_ticks([0, 6, 12, 18, 24])                   # fixed control points

ax.grid(True, which="major", alpha=0.25)
ax.grid(True, which="minor", alpha=0.12)
ax.set_xlabel("Time, hours")
ax.set_ylabel("Value")
plt.tight_layout(); plt.show()
