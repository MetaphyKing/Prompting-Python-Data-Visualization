
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 13)
y = np.array([12, 14, 13, 15, 16, 18, 17, 19, 21, 22, 23, 25])

fig, ax = plt.subplots(figsize=(8, 4.5), dpi=120)
ax.plot(x, y, marker="o", linewidth=2)

ax.set_title("Monthly metric trend")
ax.set_xlabel("Month")
ax.set_ylabel("Value, units")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
