import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins").dropna(
    subset=["bill_length_mm", "bill_depth_mm", "species"]
)

sns.scatterplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm",
    hue="species",
    palette="colorblind",  # distinguishable and color-blind friendly
    alpha=0.85
)
plt.xlabel("Bill length (mm)")
plt.ylabel("Bill depth (mm)")
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins").dropna(
    subset=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"]
)

cmap = sns.color_palette("mako", as_cmap=True)  # continuous colormap
sns.scatterplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm",
    hue="flipper_length_mm",
    palette=cmap
)
plt.xlabel("Bill length (mm)")
plt.ylabel("Bill depth (mm)")
plt.show()


from matplotlib.colors import CenteredNorm
sns.scatterplot(..., hue="value", palette="coolwarm", hue_norm=CenteredNorm())



import seaborn as sns
sns.set_theme(palette="deep")
