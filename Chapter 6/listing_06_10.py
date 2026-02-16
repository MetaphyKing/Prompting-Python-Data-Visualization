import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FuncFormatter

x = np.linspace(0, 10, 300)
y = {
    "A": np.sin(x),
    "B": 1.3*np.sin(x + 0.5),
    "C": 0.7*np.sin(x - 0.8),
}

fig, axs = plt.subplots(1, 3, figsize=(10, 3), sharex=True, sharey=True)

for ax, (name, s) in zip(axs, y.items()):
    ax.plot(x, s, label=name)
    ax.grid(True, alpha=0.3)
    ax.set_title(f"Series {name}")

# Apply unified tick locators and formatters
for ax in axs:
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, pos: f"{v:,.1f}"))

axs[0].set_ylabel("Amplitude")
fig.suptitle("Shared axes with synchronized ticks", y=0.98)
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
