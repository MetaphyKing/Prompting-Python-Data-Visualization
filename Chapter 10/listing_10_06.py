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

ax = sns.histplot(penguins, x="body_mass_g", bins=25, stat="density")
sns.kdeplot(penguins, x="body_mass_g", bw_adjust=1.0, ax=ax)
ax.set(title="Continuous variable: histogram + KDE", xlabel="Mass (g)", ylabel="Density")
plt.show()

ax = sns.ecdfplot(penguins, x="body_mass_g")
ax.set(title="ECDF: quantile perspective", xlabel="Mass (g)", ylabel="Proportion ≤ x")
plt.show()


ax = sns.histplot(tips, x="size", discrete=True, stat="probability")
ax.set(title="Discrete metric: party size", xlabel="Party size", ylabel="Proportion")
plt.show()

ax = sns.ecdfplot(tips, x="size", stat="proportion")
ax.set(title="ECDF for discrete variable", xlabel="Party size", ylabel="Proportion ≤ x")
plt.show()

ax = sns.histplot(
    data=penguins, x="body_mass_g",
    hue="species", element="step",
    stat="density", common_norm=False, bins=25
)
ax.set(title="Distribution shapes by species", xlabel="Mass (g)", ylabel="Density")
plt.show()

ax = sns.ecdfplot(
    data=penguins, x="body_mass_g",
    hue="species", stat="proportion"
)
ax.set(title="ECDF by species: quantile comparison", xlabel="Mass (g)", ylabel="Proportion ≤ x")
plt.show()



ax = sns.boxplot(tips, x="day", y="total_bill", width=0.6)
ax.set(title="Bill by day: center and spread", xlabel="Day", ylabel="Bill ($)")
plt.show()


ax = sns.violinplot(tips, x="day", y="total_bill", inner="quartile", scale="width", cut=0)
ax.set(title="Bill by day: distribution shape", xlabel="Day", ylabel="Bill ($)")
plt.show()

ax = sns.boxplot(tips, x="day", y="total_bill", width=0.6, showcaps=True, showfliers=False, zorder=1)
sns.stripplot(tips, x="day", y="total_bill", jitter=True, alpha=0.5, size=3, color="black", zorder=2)
ax.set(title="Boxplot + Stripplot: summary and points", xlabel="Day", ylabel="Bill ($)")
plt.show()



order = ["Thur","Fri","Sat","Sun"]
ax = sns.boxplot(tips, x="day", y="total_bill", order=order)
ax.set(title="Category order shapes interpretation", xlabel="Day", ylabel="Bill ($)")
plt.show()



ax = sns.scatterplot(
    data=penguins,
    x="flipper_length_mm", y="body_mass_g",
    hue="species", style="sex", s=70, alpha=0.85
)
ax.set(title="Body mass vs Flipper length", xlabel="Flipper length (mm)", ylabel="Mass (g)")
plt.show()

ax = sns.histplot(
    data=tips, x="total_bill", y="tip",
    bins=30, pmax=0.98, cbar=True
)
ax.set(title="2D Histogram: Bill vs Tip", xlabel="Bill ($)", ylabel="Tip ($)")
plt.show()


ax = sns.lineplot(
    data=tips, x="size", y="total_bill",
    estimator="mean", errorbar=("ci", 95)
)
ax.set(title="Smoothed trend of mean bill", xlabel="Party size", ylabel="Bill ($)")
plt.show()
