import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
y1, y2 = np.sin(x), np.cos(x)

fig, axs = plt.subplots(2, 2, figsize=(9, 5), sharex=True)

axs[0,0].plot(x, y1); axs[0,0].set_ylabel("Amplitude, units")
axs[0,1].plot(x, y2); axs[0,1].set_ylabel("Amplitude, units")
axs[1,0].plot(x, y1**2); axs[1,0].set_xlabel("Time, s"); axs[1,0].set_ylabel("Amplitude squared")
axs[1,1].plot(x, y2**2); axs[1,1].set_xlabel("Time, s"); axs[1,1].set_ylabel("Amplitude squared")

fig.suptitle("Aligned titles and axis labels", y=0.98)
fig.align_ylabels(axs[:, 0])   # align left column labels
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

