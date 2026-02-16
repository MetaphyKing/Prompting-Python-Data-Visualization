import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "DejaVu Sans",   # replace with corporate font if needed
    "font.size": 10,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "legend.fontsize": 9,
    "figure.dpi": 110,
    "savefig.dpi": 150,
})
from matplotlib import font_manager
# font_manager.fontManager.addfont("path/to/YourFont-Regular.ttf")
# mpl.rcParams["font.family"] = "YourFont"

