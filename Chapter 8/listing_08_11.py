import matplotlib as mpl
mpl.rcParams.update({
    "path.simplify": True,
    "path.simplify_threshold": 0.5,
    "agg.path.chunksize": 10000,
})


segs = [np.column_stack([x, y_i]) for y_i in Ys]
lc = LineCollection(segs, linewidths=1.2)
ax.add_collection(lc)


import matplotlib
matplotlib.use("Agg")  # before importing pyplot
import matplotlib.pyplot as plt
plt.ioff()


fig, ax = plt.subplots(...)
# build plot
fig.savefig(...)
plt.close(fig)
