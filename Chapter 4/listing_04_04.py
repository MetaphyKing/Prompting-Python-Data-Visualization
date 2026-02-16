import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

x = np.arange(1, 12 + 1)
growth = np.array([0.02, 0.03, 0.01, 0.00, 0.04, 0.05, 0.02, 0.01, 0.03, 0.02, 0.01, 0.00])

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, growth, marker="o")

ax.set_title("Monthly growth, %")
ax.set_xlabel("Month")
ax.set_ylabel("Growth")
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
