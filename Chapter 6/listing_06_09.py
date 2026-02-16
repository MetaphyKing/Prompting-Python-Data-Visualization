import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

data = np.corrcoef(np.random.randn(80, 8), rowvar=False)

fig = plt.figure(figsize=(8.5, 5.5), constrained_layout=False)
gs = gridspec.GridSpec(
    1, 2, figure=fig,
    width_ratios=[20, 1],  # narrow column for future colorbar
    wspace=0.15
)

ax_heat = fig.add_subplot(gs[0, 0])
ax_cbar = fig.add_subplot(gs[0, 1])

im = ax_heat.imshow(data, origin="lower")
ax_heat.set_title("Correlation matrix")
ax_heat.grid(False)

# Colorbar axis reserved; actual colorbar will be added later
# plt.colorbar(im, cax=ax_cbar)

fig.suptitle("Reserved space for a shared colorbar", y=0.98)
fig.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
