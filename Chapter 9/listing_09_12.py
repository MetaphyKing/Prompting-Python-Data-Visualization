import seaborn as sns

sns.set_theme(
    context="paper",
    style="white",
    rc={
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "grid.linestyle": "--",
        "grid.linewidth": 0.6,
    }
)
import matplotlib.pyplot as plt
plt.rcParams["savefig.bbox"] = "tight"
plt.rcParams["legend.frameon"] = False
