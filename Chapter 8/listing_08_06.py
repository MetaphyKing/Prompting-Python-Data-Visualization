import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(3.54, 2.20), constrained_layout=True)  # ~90 mm × 56 mm
ax.set_title("Demonstration plot")
ax.set_xlabel("x")
ax.set_ylabel("y")
plt.savefig("demo.pdf", bbox_inches="tight", pad_inches=0.02)


import matplotlib as mpl
mpl.rcParams.update({
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "lines.linewidth": 1.2,
    "lines.markersize": 4.5,
})
