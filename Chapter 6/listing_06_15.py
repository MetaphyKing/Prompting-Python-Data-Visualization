import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 200)
fig, axs = plt.subplots(2, 3, figsize=(10, 5), sharex=True)

for ax in axs.ravel():
    ax.plot(x, np.sin(x) + 0.1*np.random.randn(len(x)))
    ax.grid(True, alpha=0.25)

fig.subplots_adjust(wspace=0.25, hspace=0.35)  # fine-tune spacing

fig.suptitle("Controlling wspace/hspace and figure margins", y=0.98)
fig.tight_layout(rect=[0, 0.06, 1, 0.96])  # reserve 6% at the bottom
plt.show()
