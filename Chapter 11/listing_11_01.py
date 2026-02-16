import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Scatter plot with linear regression line and 95% confidence interval
ax = sns.regplot(
    data=tips, x="total_bill", y="tip",
    scatter_kws={"alpha": 0.6, "s": 40},
    line_kws={"linewidth": 2}
)
ax.set_title("Relationship between tips and bill amount: regression line with confidence interval")
plt.show()



g = sns.lmplot(
    data=tips, x="total_bill", y="tip",
    hue="sex", col="day",
    scatter_kws={"alpha": 0.6, "s": 35},
    line_kws={"linewidth": 2}
)
g.fig.suptitle("Comparing slopes by day and gender", y=1.02)


sns.regplot(
    data=tips, x="total_bill", y="tip",
    lowess=True,
    scatter_kws={"alpha": 0.5}
)
