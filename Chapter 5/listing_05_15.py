# reporting.mplstyle  -  style for reports/publications
figure.dpi: 110
savefig.dpi: 160

font.size: 10
axes.titlesize: 13
axes.titleweight: bold
axes.labelsize: 11
xtick.labelsize: 9
ytick.labelsize: 9

axes.grid: True
axes.grid.axis: y
grid.alpha: 0.25

axes.spines.top: False
axes.spines.right: False

lines.linewidth: 2.2
legend.fontsize: 9
legend.frameon: True
legend.framealpha: 0.90
legend.title_fontsize: 10

# Unified categorical palette (contrasting, colorblind-friendly)
axes.prop_cycle: cycler('color', ['#4C78A8', '#F58518', '#54A24B', '#E45756', '#72B7B2'])


# slides.mplstyle  -  style for presentations/projectors
figure.dpi: 120
savefig.dpi: 180


font.size: 12
axes.titlesize: 15
axes.titleweight: bold
axes.labelsize: 12
xtick.labelsize: 10
ytick.labelsize: 10

axes.grid: True
axes.grid.axis: y
grid.alpha: 0.30

axes.spines.top: False
axes.spines.right: False

lines.linewidth: 2.6
legend.fontsize: 11
legend.frameon: True
legend.framealpha: 0.95

axes.prop_cycle: cycler('color', ['#4C78A8', '#F58518', '#54A24B', '#E45756', '#72B7B2'])




import matplotlib.pyplot as plt

plt.style.use("reporting.mplstyle")  # local file next to script/notebook

fig, ax = plt.subplots(figsize=(6.4, 3.6))
for c in ["A", "B", "C"]:
    ax.plot(df.index, df[c], label=c)
ax.set_title("Report style from .mplstyle file", loc="left")
ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, 1.12))
plt.tight_layout(); plt.show()
