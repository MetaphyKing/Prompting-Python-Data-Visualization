import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)
fig, axs = plt.subplots(1, 2, figsize=(8, 3), constrained_layout=True)

axs[0].plot(x, np.sqrt(x))
axs[0].set_title("Long title, testing wrapping and spacing")
axs[0].set_ylabel("Very long Y-axis label, mm/s²")

axs[1].plot(x, x**2)
axs[1].set_xlabel("Verbose X-axis label, sec")

plt.show()
