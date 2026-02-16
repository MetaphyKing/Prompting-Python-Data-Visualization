import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(context="notebook", style="whitegrid")
tips = sns.load_dataset("tips").dropna(subset=["total_bill", "sex", "smoker", "day", "time"])
penguins = sns.load_dataset("penguins").dropna(subset=["species", "sex", "body_mass_g"])


ax = sns.boxplot(
    data=tips, x="day", y="total_bill",
    hue="time", dodge=True
)
ax.set(title="Boxplot: Total Bill by Day and Time",
       xlabel="Day of Week", ylabel="Bill ($)")
plt.show()


ax = sns.violinplot(
    data=penguins, x="species", y="body_mass_g",
    inner="quartile", cut=0
)
ax.set(title="Violinplot: Body Mass by Penguin Species",
       xlabel="Species", ylabel="Mass (g)")
plt.show()



ax = sns.violinplot(
    data=penguins, x="species", y="body_mass_g",
    hue="sex", split=True, inner="quartile", cut=0
)
ax.set(title="Violinplot (split): Body Mass by Species and Sex",
       xlabel="Species", ylabel="Mass (g)")
plt.show()



ax = sns.stripplot(
    data=tips, x="day", y="total_bill",
    hue="smoker", dodge=True, jitter=True, alpha=0.6
)
ax.set(title="Stripplot: Total Bill by Day (Smokers/Non-smokers)",
       xlabel="Day of Week", ylabel="Bill ($)")
plt.show()




ax = sns.boxplot(data=tips, x="day", y="total_bill", color=None)
sns.stripplot(
    data=tips, x="day", y="total_bill",
    color="black", alpha=0.4, jitter=True, ax=ax
)
ax.set(title="Box + Strip: Summary and Raw Points",
       xlabel="Day of Week", ylabel="Bill ($)")
plt.show()

ax = sns.boxplot(
    data=tips, x="day", y="total_bill",
    hue="smoker", dodge=True, width=0.6
)
ax.set(title="Total Bill by Day and Smoking Status", xlabel="Day", ylabel="Bill ($)")
plt.show()


ax = sns.violinplot(
    data=tips, x="day", y="total_bill",
    hue="smoker", split=True, inner="quartile", scale="width", cut=0
)
ax.set(title="Violinplot: Bill by Day (Smokers/Non-smokers)", xlabel="Day", ylabel="Bill ($)")
plt.show()


ax = sns.violinplot(
    data=tips, x="day", y="total_bill",
    inner=None, color=None, linewidth=0.5, cut=0
)
sns.stripplot(
    data=tips, x="day", y="total_bill",
    hue="smoker", dodge=True, jitter=True, alpha=0.5, size=3
)
ax.set(title="Violin + Strip: Shape and Raw Observations", xlabel="Day", ylabel="Bill ($)")
plt.show()

