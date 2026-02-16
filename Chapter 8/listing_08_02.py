
import matplotlib.pyplot as plt
import numpy as np
from production_style import use_production_style

use_production_style()

x = np.linspace(0, 10, 201)
y = np.log1p(x) + 0.15*np.sin(4*x)

fig, ax = plt.subplots(figsize=(4.75, 3.0))
ax.plot(x, y, label="log1p(x) + noise")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Key point
xm = 6
ym = np.log1p(xm) + 0.15*np.sin(4*xm)
ax.scatter([xm], [ym], zorder=3)
ax.annotate("local maximum\n(relevant for discussion)",
            xy=(xm, ym), xytext=(xm+1.0, ym+0.25),
            arrowprops=dict(arrowstyle="->"))

ax.legend()
plt.show()
