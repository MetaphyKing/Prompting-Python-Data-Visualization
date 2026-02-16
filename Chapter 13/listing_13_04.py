import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

tips = sns.load_dataset("tips").copy()

order = ["Thur", "Fri", "Sat", "Sun"]
agg = (tips
       .loc[tips["day"].isin(order), ["day", "tip"]]
       .assign(day=pd.Categorical(tips["day"], categories=order, ordered=True))
       .groupby("day", observed=True, as_index=False)
       .agg(mean_tip=("tip", "mean")))

plt.figure(figsize=(9, 5))
bars = plt.bar(agg["day"], agg["mean_tip"])

for rect, val in zip(bars, agg["mean_tip"]):
    plt.annotate(f"{val:.2f}",
                 xy=(rect.get_x() + rect.get_width()/2, val),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha="center", va="bottom")

plt.title("Средние чаевые по дням недели")
plt.xlabel("День недели")
plt.ylabel("Чаевые, $")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:,.2f}".replace(",", " ")))
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("figures/tips_manual_bar.png", dpi=140)
plt.show()




import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
order = ["Thur", "Fri", "Sat", "Sun"]

plt.figure(figsize=(9, 5))
ax = sns.barplot(
    data=tips, x="day", y="tip",
    order=order, errorbar=("ci", 95)
)
ax.set_title("Средний размер чаевых по дням недели")
ax.set_xlabel("День недели")
ax.set_ylabel("Чаевые, $")
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("figures/tips_ai_bar.png", dpi=120)
plt.show()
