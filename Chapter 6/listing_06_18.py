import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
fig, ax = plt.subplots(figsize=(5.5, 3.2))
ax.plot(x, np.sin(x))
ax.set_title("Export with clean margins")
ax.set_xlabel("Time, s"); ax.set_ylabel("Amplitude")
fig.tight_layout()

# Raster for reports and presentations
fig.savefig("figure_6_17.png", dpi=300, bbox_inches="tight", pad_inches=0.02)

# Vector for articles or typesetting
fig.savefig("figure_6_17.pdf", bbox_inches="tight", pad_inches=0.02)
plt.show()
