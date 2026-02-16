import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

x = np.linspace(0, 10, 300)
y = np.sin(x) + 0.2*np.cos(3*x)

fig = plt.figure(figsize=(10, 6), constrained_layout=False)

# Grid 3×4: left half = hero, right side = three narrow panels
gs = gridspec.GridSpec(
    nrows=3, ncols=4, figure=fig,
    width_ratios=[1.2, 1.2, 0.8, 0.8],   # left side wider
    height_ratios=[1, 1, 1],             # equal rows
    wspace=0.35, hspace=0.35
)

ax_main = fig.add_subplot(gs[:, :2])     # hero spans all 3 rows and 2 columns
ax_r1   = fig.add_subplot(gs[0, 2:])
ax_r2   = fig.add_subplot(gs[1, 2:])
ax_r3   = fig.add_subplot(gs[2, 2:])

ax_main.plot(x, y, label="Signal")
ax_main.set_title("Main plot"); ax_main.grid(True, alpha=0.3)
ax_main.legend(loc="upper right")

ax_r1.hist(np.diff(y), bins=30); ax_r1.set_title("Δ signal"); ax_r1.grid(True, alpha=0.2)
ax_r2.plot(x, np.abs(y));        ax_r2.set_title("|y|");     ax_r2.grid(True, alpha=0.2)
ax_r3.plot(x, y.cumsum());       ax_r3.set_title("Cumulative"); ax_r3.grid(True, alpha=0.2)

fig.suptitle("GridSpec with merged cells and sidebar", y=0.98)
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

