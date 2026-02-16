import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

ax = sns.regplot(
    data=tips, x="total_bill", y="tip",
    lowess=True,
    scatter_kws={"alpha": 0.5, "s": 35},
    line_kws={"linewidth": 2}
)
ax.set_title("Tip trends with increasing bill size (LOWESS)")
plt.show()
