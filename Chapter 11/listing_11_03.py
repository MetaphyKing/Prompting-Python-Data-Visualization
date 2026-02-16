import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins").dropna()

g = sns.pairplot(
    data=penguins,
    vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
    hue="species",
    corner=True,            # only show the lower triangle
    diag_kind="kde",        # smooth densities on the diagonal
    plot_kws={"alpha": 0.6, "s": 30}
)
g.fig.suptitle("Pairwise relationships and distributions in penguins", y=1.02)
plt.show()


g = sns.pairplot(
    penguins,
    vars=["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"],
    hue="species", hue_order=["Adelie","Chinstrap","Gentoo"],
    corner=True,
    diag_kind="hist",
    plot_kws={"alpha": 0.5}
)
for ax in g.axes.flat:
    if ax is not None:
        ax.label_outer()   # remove duplicate labels



g = sns.pairplot(
    penguins,
    vars=["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"],
    hue="species",
    diag_kind="kde"
)

g = sns.PairGrid(
    data=penguins,
    vars=["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"],
    hue="species",
    corner=True
)
g.map_diag(sns.kdeplot, fill=True, alpha=0.6)
g.map_lower(sns.scatterplot, alpha=0.5, s=25)
g.map_lower(sns.regplot, scatter=False, truncate=False)  # add trend lines
g.add_legend()

