import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

g = sns.catplot(
    data=tips,
    x="day", y="total_bill",
    hue="sex",
    kind="bar",
    height=3.4, aspect=1.3
)
g.set_axis_labels("Day of week", "Total bill (USD)")
g.add_legend()
plt.show()


g = sns.catplot(
    data=tips,
    x="day", y="total_bill",
    hue="smoker",
    kind="box",
    height=3.4, aspect=1.3
)
g.set_axis_labels("Day of week", "Total bill (USD)")
g.add_legend(title="Smoker")
plt.show()


g = sns.catplot(
    data=tips,
    x="day",
    hue="time",    # Lunch / Dinner
    kind="count",
    height=3.2, aspect=1.4
)
g.set_axis_labels("Day of week", "Count")
g.add_legend(title="Time")
plt.show()
