import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.linspace(0, 2*np.pi, 200)
series = {
    "sin(x)": np.sin(x),
    "cos(x)": np.cos(x),
    "sin(2x)": np.sin(2*x),
    "cos(2x)": np.cos(2*x),
}

# 2×2 grid; shared axes simplify comparison of amplitudes and phases
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 6), sharex=True, sharey=True)

# axs is a 2D array of axes
for ax, (name, y) in zip(axs.ravel(), series.items()):
    ax.plot(x, y)
    ax.set_title(name)
    ax.grid(True, alpha=0.3)

fig.suptitle("Comparison of harmonics", y=1.02)
fig.tight_layout()
plt.show()
