import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(5.5, 3.5))
ax.plot(x, y)

ax.set_title("Controlling local padding", pad=10)
ax.set_xlabel("Time, s", labelpad=6)
ax.set_ylabel("Amplitude", labelpad=6)
ax.margins(x=0.03, y=0.1)       # breathing room around data
ax.tick_params(axis="x", pad=4) # spacing between ticks and axis
ax.grid(True, alpha=0.3)

fig.tight_layout()
plt.show()
