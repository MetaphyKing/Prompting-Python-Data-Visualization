
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
x = rng.normal(50, 10, size=400)
y = 0.8 * x + rng.normal(0, 5, size=400)

fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.scatter(x, y, s=20, alpha=0.6)

ax.set_title("Relationship between two measures")
ax.set_xlabel("X, units")
ax.set_ylabel("Y, units")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
x = rng.normal(50, 10, size=400)
y = 0.8 * x + rng.normal(0, 5, size=400)

fig, ax = plt.subplots(figsize=(7.5, 4.5))
ax.scatter(x, y, s=20, alpha=0.6)

ax.set_title("Relationship between two measures")
ax.set_xlabel("X, units")
ax.set_ylabel("Y, units")
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
