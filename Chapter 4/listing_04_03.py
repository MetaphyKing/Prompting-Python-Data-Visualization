import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)
y1 = np.sin(x)
y2 = np.cos(x)
z  = np.random.normal(size=300)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(9, 6), sharex=False)
ax11, ax12, ax21, ax22 = axes.ravel()

ax11.plot(x, y1, label="sin")
ax11.set_title("Sine")
ax11.grid(True, alpha=0.3)
ax11.legend()

ax12.plot(x, y2, label="cos", linestyle="--")
ax12.set_title("Cosine")
ax12.grid(True, alpha=0.3)
ax12.legend()

ax21.hist(z, bins=25)
ax21.set_title("Noise histogram")
ax21.grid(True, alpha=0.3)

cats = ["A","B","C","D"]
vals = [12, 18, 9, 15]
ax22.bar(cats, vals)
ax22.set_title("Categories")
ax22.grid(True, axis="y", alpha=0.3)

fig.suptitle("2×2 panel: different plot types", y=1.02)
plt.tight_layout()
plt.show()
