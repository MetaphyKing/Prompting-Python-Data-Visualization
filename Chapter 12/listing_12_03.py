import numpy as np

vars_ = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
g = sns.PairGrid(penguins, vars=vars_, hue="species", corner=False)
g.map_lower(sns.scatterplot, s=18, alpha=0.5)
g.map_diag(sns.histplot, kde=True, element="step")

def corr_annot(x, y, **kws):
    r = np.corrcoef(x, y)[0, 1]
    ax = plt.gca()
    ax.text(
        0.5, 0.5, f"r = {r:.2f}",
        transform=ax.transAxes,
        ha="center", va="center", fontsize=10
    )

g.map_upper(corr_annot)
g.add_legend()
plt.tight_layout()
plt.show()


def hexbinplot(x, y, **kws):
    ax = plt.gca()
    ax.hexbin(x, y, gridsize=25, mincnt=1)

g = sns.PairGrid(penguins, vars=vars_, corner=True)
g.map_lower(hexbinplot)
g.map_diag(sns.kdeplot, fill=True)
plt.tight_layout()
plt.show()



sns.set_theme()
g = sns.PairGrid(penguins, vars=vars_, hue="species", corner=True)
g.map_lower(sns.scatterplot, s=16, alpha=0.6)
g.map_diag(sns.histplot, kde=True, element="poly")
g.add_legend()
g.figure.set_size_inches(9, 8)
g.figure.savefig("pairgrid_penguins.png", dpi=200, bbox_inches="tight")







