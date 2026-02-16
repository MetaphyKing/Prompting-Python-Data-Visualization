penguins = sns.load_dataset("penguins").dropna(subset=["flipper_length_mm", "species"])

g = sns.displot(
    data=penguins,
    x="flipper_length_mm",
    hue="species",
    kind="hist",
    bins=20,
    multiple="stack",
    height=3.4, aspect=1.3
)
g.set_axis_labels("Flipper length (mm)", "Count")
plt.show()


g = sns.displot(
    data=penguins,
    x="flipper_length_mm",
    hue="species",
    kind="kde",
    fill=True,
    common_norm=False,
    height=3.4, aspect=1.3
)
g.set_axis_labels("Flipper length (mm)", "Density")
plt.show()


g = sns.displot(
    data=penguins,
    x="flipper_length_mm",
    hue="species",
    kind="ecdf",
    height=3.2, aspect=1.4
)
g.set_axis_labels("Flipper length (mm)", "ECDF")
plt.show()


g = sns.displot(
    data=penguins,
    x="bill_depth_mm",
    col="species",
    kind="hist",
    bins=16,
    height=2.8, aspect=1.0
)
g.set_axis_labels("Bill depth (mm)", "Count")
plt.show()




