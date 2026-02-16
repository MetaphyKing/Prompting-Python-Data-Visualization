

import numpy as np, matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, NullFormatter

x = np.logspace(-2, 3, 400)
y = 1/(1 + (x/10)**2)

fig, axs = plt.subplots(1, 2, figsize=(10, 4))

# Log scale on X
ax = axs[0]
ax.plot(x, y)
ax.set_xscale("log")
ax.xaxis.set_minor_locator(LogLocator(subs=range(2,10)))
ax.xaxis.set_minor_formatter(NullFormatter())
ax.set_title("log X")

# Symmetric log scale on Y
t = np.linspace(-50, 50, 501)
ax = axs[1]
ax.plot(t, np.sinh(t/10))
ax.set_yscale("symlog", linthresh=1.0, linscale=1.0)
ax.set_title("symlog Y (linthresh=1.0)")

for ax in axs: ax.grid(True, which="both", alpha=0.25)
plt.tight_layout(); plt.show()
