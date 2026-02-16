
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(0)
data = rng.normal(0, 1, size=1000)

fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.hist(data, bins=30)

ax.set_title("Distribution of the metric")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
