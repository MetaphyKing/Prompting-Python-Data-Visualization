
import numpy as np
import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
means = np.array([10.5, 12.2, 9.8, 11.9])
errs  = np.array([0.6, 0.8, 0.4, 0.7])

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.bar(labels, means, yerr=errs, capsize=4)

ax.set_title("Means with error bars")
ax.set_ylabel("Value, units")
ax.grid(True, axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
