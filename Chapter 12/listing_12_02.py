import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins").dropna()

g = sns.PairGrid(
    data=penguins,
    vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    hue="species",
    corner=False,          # full matrix (True leaves only the lower triangle)
    diag_sharey=False      # independent scales on the diagonal
)

g.map_upper(sns.scatterplot, alpha=0.6, s=20)
g.map_lower(sns.kdeplot, fill=True, thresh=0.05, levels=6, alpha=0.5)
g.map_diag(sns.histplot, kde=True, element="step", stat="count")
g.add_legend(title="Species")
g.set(title="Penguins: pairwise relationships")
plt.tight_layout()
plt.show()



g = sns.PairGrid(
    penguins,
    vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    hue="species",
    corner=True
)

g.map_lower(
    sns.regplot,
    scatter_kws=dict(s=18, alpha=0.5, linewidth=0),
    line_kws=dict(alpha=0.8)
)
g.map_diag(sns.kdeplot, fill=True, alpha=0.6)
g.add_legend()
for ax in g.axes.flat:
    if ax is not None:
        ax.grid(False)
plt.tight_layout()
plt.show()



