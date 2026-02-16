import seaborn as sns
import matplotlib.pyplot as plt

palette_map = {
    "Adelie":  "#4C72B0",
    "Chinstrap": "#55A868",
    "Gentoo":   "#C44E52",
}

penguins = sns.load_dataset("penguins").dropna(
    subset=["bill_length_mm", "bill_depth_mm", "species"]
)

sns.scatterplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm",
    hue="species",
    palette=palette_map
)
plt.show()
