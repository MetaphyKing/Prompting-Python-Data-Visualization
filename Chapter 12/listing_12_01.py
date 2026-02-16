import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

g = sns.FacetGrid(
    data=tips,
    col="sex",
    row="time"
)
g.map(sns.histplot, "total_bill")

plt.show()


g = sns.FacetGrid(tips, col="day", col_wrap=2, height=4)
g.map_dataframe(
    sns.scatterplot,
    x="total_bill", y="tip", hue="sex", alpha=0.7
)
g.add_legend()
plt.show()

g = sns.FacetGrid(
    tips,
    col="day",
    hue="sex",
    col_wrap=3,
    height=3,
    aspect=1.2,
    sharex=True,
    sharey=True,
    margin_titles=True
)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip")
g.add_legend()
g.despine()
plt.tight_layout()
plt.show()


g = sns.FacetGrid(
    tips,
    col="day",
    col_order=["Thur", "Fri", "Sat", "Sun"],
    hue="sex",
    height=3
)
g.map_dataframe(sns.kdeplot, x="total_bill", fill=True, alpha=0.4)
g.add_legend(title="Guest")
g.set_axis_labels("Total bill", "Density")
g.set_titles(col_template="{col_name}: {col_var}")
plt.show()



g = sns.FacetGrid(tips, col="smoker", row="time", height=3)
g.map_dataframe(sns.regplot, x="total_bill", y="tip", scatter_kws=dict(s=20, alpha=0.5))
g.set_axis_labels("Total bill", "Tip")
g.set(xlim=(0, tips["total_bill"].max()), ylim=(0, tips["tip"].max()))
g.set_titles(row_template="Time = {row_var}", col_template="Smoker = {col_var}")
g.fig.suptitle("Tips vs Total Bill across smoking status and time", y=1.02)
plt.tight_layout()
plt.show()

g = sns.FacetGrid(tips, col="day", hue="sex", height=3, sharex=True, sharey=True)
g.map_dataframe(sns.scatterplot, x="total_bill", y="tip", s=18, alpha=0.6)
g.add_legend()
g.figure.set_size_inches(10, 6)
g.figure.savefig("facetgrid_tips.png", dpi=200, bbox_inches="tight")







