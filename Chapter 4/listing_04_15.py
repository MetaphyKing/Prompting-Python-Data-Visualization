

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(9, 6), constrained_layout=True)
gs = fig.add_gridspec(nrows=2, ncols=2, width_ratios=[2, 1], height_ratios=[1, 1])

ax_main = fig.add_subplot(gs[:, 0])   # wide left panel spanning two rows
ax_top  = fig.add_subplot(gs[0, 1])   # top-right
ax_bot  = fig.add_subplot(gs[1, 1])   # bottom-right

x = np.linspace(0, 10, 200)
ax_main.plot(x, np.sin(x), label="sin")
ax_main.plot(x, np.cos(x), label="cos", linestyle="--")
ax_main.set_title("Main plot")
ax_main.legend(frameon=False)
ax_main.grid(True, alpha=0.3)

ax_top.hist(np.random.normal(size=400), bins=25)
ax_top.set_title("Distribution A")
ax_top.grid(True, alpha=0.3)

ax_bot.bar(["A","B","C"], [12, 18, 9])
ax_bot.set_title("Categories")
ax_bot.grid(True, axis="y", alpha=0.3)

fig.suptitle("Asymmetric layout with GridSpec")
plt.show()
