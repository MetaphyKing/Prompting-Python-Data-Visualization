import seaborn as sns
g = sns.FacetGrid(data=monthly_long, col="metric", sharey=False, height=3, aspect=1.6)
g.map_dataframe(sns.lineplot, x="month", y="value")
g.add_legend()
