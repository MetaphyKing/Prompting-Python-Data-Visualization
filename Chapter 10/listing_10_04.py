import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins").dropna(
    subset=["species", "sex", "flipper_length_mm", "body_mass_g"]
)

ax = sns.scatterplot(
    data=penguins,
    x="flipper_length_mm", y="body_mass_g",
    hue="species",        # color = species
    style="sex",          # marker shape = sex
    s=70, alpha=0.8
)
ax.set(
    title="Penguins: Body Mass vs Flipper Length (color=species, shape=sex)",
    xlabel="Flipper length (mm)", ylabel="Body mass (g)"
)
plt.show()


ax = sns.scatterplot(
    data=penguins,
    x="flipper_length_mm", y="body_mass_g",
    hue="species", style="sex",
    size="flipper_length_mm", sizes=(30, 120),
    alpha=0.7
)
ax.legend(title="Species / Sex / Flipper Length")
ax.set(title="Three-channel encoding: color + shape + size")
plt.show()


g = sns.relplot(
    data=penguins,
    x="flipper_length_mm", y="body_mass_g",
    hue="sex",
    col="species", col_wrap=3,
    kind="scatter", s=60, alpha=0.8
)
g.set_axis_labels("Flipper length (mm)", "Body mass (g)")
g.set_titles("Species: {col_name}")
g.figure.suptitle("Small multiples: comparing sexes within species", y=1.02)
plt.show()



ax = sns.scatterplot(
    data=penguins,
    x="flipper_length_mm", y="body_mass_g",
    hue="species", hue_order=["Adelie", "Chinstrap", "Gentoo"],
    palette="Set2",
    s=70
)
ax.legend(title="Species (fixed order)")
plt.show()


tips = sns.load_dataset("tips").dropna(
    subset=["total_bill", "size", "smoker", "day", "time"]
)

g = sns.relplot(
    data=tips,
    x="size", y="total_bill",
    col="day", hue="smoker", style="time",
    kind="scatter", col_wrap=2, s=60, alpha=0.8
)
g.set_axis_labels("Party size", "Bill ($)")
g.set_titles("{col_name}")
plt.show()
ax = sns.lineplot(
    data=tips, x="size", y="total_bill",
    hue="time", style="smoker",
    estimator="median", errorbar=None
)
ax.legend(title="Time / Smoking", loc="best", frameon=True)
ax.set(title="Median Bill by Party Size", xlabel="Party Size", ylabel="Bill ($)")
plt.show()

g = sns.relplot(
    data=penguins, x="flipper_length_mm", y="body_mass_g",
    hue="sex", col="species", kind="scatter", s=60
)
g._legend.set_title("Sex")  
g.set_titles("{col_name}")
plt.show()


