import numpy as np
c = np.array([0.1, 0.4, 0.7, 0.9])
sc = ax.scatter(x, y, c=c, cmap="viridis")
cb = fig.colorbar(sc, ax=ax, pad=0.02)
cb.set_label("Intensity")
