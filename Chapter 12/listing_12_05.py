import seaborn as sns
import matplotlib.pyplot as plt

# Unified theme for all figures and grids
sns.set_theme(
    context="notebook",   # paper | notebook | talk | poster
    style="whitegrid",    # white | dark | whitegrid | darkgrid | ticks
    palette="deep",       # deep | muted | bright | colorblind | ...
    rc={
        "axes.titleweight": "semibold",
        "axes.labelsize": 12,
        "axes.titlesize": 13,
        "legend.title_fontsize": 11,
        "legend.fontsize": 10,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "axes.spines.top": False,
        "axes.spines.right": False
    }
)
