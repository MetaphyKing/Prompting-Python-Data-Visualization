
import matplotlib as mpl
import matplotlib.pyplot as plt

report_rc = {
    "figure.dpi": 110, "savefig.dpi": 160,
    "font.family": "DejaVu Sans", "font.size": 10,
    "axes.titlesize": 13, "axes.titleweight": "bold", "axes.labelsize": 11,
    "axes.grid": True, "axes.grid.axis": "y", "grid.alpha": 0.25,
    "lines.linewidth": 2.2,
    "legend.frameon": True, "legend.framealpha": 0.9, "legend.fontsize": 9,
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.labelsize": 9, "ytick.labelsize": 9,
}

slides_rc = {
    "figure.dpi": 120, "savefig.dpi": 180,
    "font.family": "DejaVu Sans", "font.size": 12,
    "axes.titlesize": 15, "axes.titleweight": "bold", "axes.labelsize": 12,
    "axes.grid": True, "axes.grid.axis": "y", "grid.alpha": 0.3,
    "lines.linewidth": 2.6,
    "legend.frameon": True, "legend.framealpha": 0.95, "legend.fontsize": 11,
    "axes.spines.top": False, "axes.spines.right": False,
    "xtick.labelsize": 10, "ytick.labelsize": 10,
}



with plt.rc_context(report_rc):
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for c in ["A", "B", "C"]:
        ax.plot(df.index, df[c], label=c)
    ax.set_title("Unified report style (report context)", loc="left")
    ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.12))
    plt.tight_layout(); plt.show()

with plt.rc_context(slides_rc):
    fig, ax = plt.subplots(figsize=(7.6, 4.2))
    for c in ["A", "B", "C"]:
        ax.plot(df.index, df[c], label=c)
    ax.set_title("Unified slide style (slides context)", loc="left")
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0))
    plt.tight_layout(); plt.show()
