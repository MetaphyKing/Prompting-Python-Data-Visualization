import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins").dropna(
    subset=["bill_length_mm", "bill_depth_mm", "species", "island", "sex"]
)

g = sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm",
    hue="species", style="sex",
    col="island",
    kind="scatter",
    height=3.4, aspect=1.1
)
g.set_axis_labels("Bill length (mm)", "Bill depth (mm)")
g.add_legend()
plt.show()
