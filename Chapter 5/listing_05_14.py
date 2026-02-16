
from matplotlib.ticker import MaxNLocator, StrMethodFormatter

def polish_axes(ax, title=None, legend_out=False):
    ax.grid(True, axis="y", alpha=0.25)
    for spine in ("top", "right"):
        ax.spines[spine].set_visible(False)
    ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
    ax.yaxis.set_major_formatter(StrMethodFormatter("{x:.2f}"))
    if title:
        ax.set_title(title, loc="left", fontweight="bold")
    if legend_out:
        ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), frameon=True, framealpha=0.9)

fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), sharex=True)
axes[0].plot(df.index, df["A"], label="A"); axes[0].plot(df.index, df["B"], label="B", linestyle="--")
axes[1].plot(df.index, df["C"], label="C", color="#54A24B")
polish_axes(axes[0], title="Formatting pattern", legend_out=True)
polish_axes(axes[1], title="Same pattern on second panel")
plt.tight_layout(); plt.show()
