import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(context="notebook", style="whitegrid")
penguins = sns.load_dataset("penguins").dropna(
    subset=["species","sex","body_mass_g","flipper_length_mm"]
)
tips = sns.load_dataset("tips").dropna(
    subset=["total_bill","tip","day","time","sex","smoker","size"]
)

ax = sns.histplot(penguins, x="body_mass_g", bins=30, stat="density")
ax.set(xlabel="Body mass (g)", ylabel="Density")
ax.set_xlim(2500, 6500)          # fix comparable limits
# ax.set_xscale("log")           # log-scale for long tails
plt.show()


sns.set_theme(style="whitegrid")
ax = sns.scatterplot(
    data=penguins,
    x="flipper_length_mm", y="body_mass_g",
    hue="species", alpha=0.85, s=70
)
sns.despine()        # softer visuals, no top/right spines
plt.tight_layout()
plt.show()

ax = sns.scatterplot(
    data=penguins,
    x="flipper_length_mm", y="body_mass_g",
    hue="species", hue_order=["Adelie","Chinstrap","Gentoo"],
    palette="Set2", alpha=0.85, s=70
)
ax.legend(title="Species", frameon=True)
plt.show()


ax = sns.boxplot(data=tips, x="day", y="total_bill", width=0.6)
ax.set(title="Total Bill by Day of Week", xlabel="Day of Week", ylabel="Bill ($)")
ax.ticklabel_format(style="plain", axis="y")   # avoid scientific notation
plt.tight_layout(); plt.show()


ax = sns.kdeplot(data=penguins, x="body_mass_g", fill=True, alpha=0.4)
med = penguins["body_mass_g"].median()
ax.axvline(med, linestyle="--")
ax.text(med, ax.get_ylim()[1]*0.9, f"Median ≈ {med:.0f} g", ha="center", va="top")
ax.set(title="Mass Density with Median Marked", xlabel="Body mass (g)", ylabel="Density")
plt.show()


ax = sns.lineplot(
    data=tips, x="size", y="total_bill",
    estimator="mean", errorbar=("ci", 95)
)
ax.set(title="Average Bill by Party Size (95% CI)",
       xlabel="Party Size", ylabel="Bill ($)")
plt.show()


g = sns.relplot(
    data=penguins,
    x="flipper_length_mm", y="body_mass_g",
    col="species", hue="sex",
    kind="scatter", col_wrap=3, s=60, alpha=0.85
)
g.set_axis_labels("Flipper length (mm)", "Body mass (g)")
g.set(xlim=(170, 235), ylim=(2500, 6500))
g.set_titles("{col_name}")
g._legend.set_title("Sex")
plt.show()



ax = sns.histplot(
    data=tips, x="total_bill", y="tip",
    bins=30, pmax=0.98, cbar=True
)
ax.set(title="2D Histogram: Bill vs Tip", xlabel="Bill ($)", ylabel="Tip ($)")
plt.show()




fig = plt.gcf()
fig.set_size_inches(6, 4)
plt.tight_layout()
plt.savefig("eda_penguins_mass.pdf")     # vector for reports
plt.savefig("eda_penguins_mass.png", dpi=300)
