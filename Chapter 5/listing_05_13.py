
import seaborn as sns

sns.set_theme(style="whitegrid", context="notebook",
              rc={"axes.spines.top": False, "axes.spines.right": False, "grid.alpha": 0.25})

fig, ax = plt.subplots(figsize=(6.6, 3.6))
ax.plot(df.index, df["A"], label="A", linewidth=2.3)
ax.plot(df.index, df["B"], label="B", linewidth=2.0, linestyle="--")
ax.set_title("Seaborn as theme, Matplotlib for plotting", loc="left")
ax.legend(ncol=2, frameon=True, framealpha=0.9)
plt.tight_layout(); plt.show()

def fig_size(kind="report-single"):
    if kind == "report-single":   # narrow column (mm → inches: ÷ 25.4)
        return (3.35, 2.2)        # ~85 mm × 56 mm
    if kind == "report-double":   # wide column
        return (7.1, 3.8)         # ~180 mm × 96 mm
    if kind == "slide-16x9":      # slides
        return (8.0, 4.5)         # 16:9
    return (6.4, 3.6)

fig, ax = plt.subplots(figsize=fig_size("report-single"))
ax.plot(df.index, df["A"], linewidth=2.2)
ax.set_title("Consistent figure sizes", loc="left")
ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout(); plt.show()
