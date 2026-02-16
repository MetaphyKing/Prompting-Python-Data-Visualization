import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

rng = np.random.default_rng(0)
A = rng.normal(size=(40, 40))
B = 0.5 + rng.normal(scale=0.8, size=(40, 40))
C = rng.normal(loc=1.0, scale=1.2, size=(40, 40))

vmin, vmax = -2.5, 2.5
norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
cmap = "viridis"

fig, axs = plt.subplots(1, 3, figsize=(10, 3), constrained_layout=False)

ims = []
for ax, M, title in zip(axs, [A, B, C], ["A", "B", "C"]):
    im = ax.imshow(M, origin="lower", cmap=cmap, norm=norm)
    ax.set_title(title); ax.grid(False)
    ims.append(im)

cbar = fig.colorbar(ims[0], ax=axs, orientation="vertical", fraction=0.05, pad=0.02)
cbar.set_label("Value")

fig.suptitle("Shared Normalize and common colorbar", y=0.98)
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fig, ax = plt.subplots(figsize=(4,3))
im = ax.imshow(A, cmap="viridis", norm=norm)
cax = inset_axes(ax, width="3%", height="60%", loc="center right", borderpad=1.2)
plt.colorbar(im, cax=cax)
plt.show()
