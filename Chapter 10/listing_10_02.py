ax = sns.histplot(
    data=penguins,
    x="body_mass_g",
    bins=30,
    stat="density"
)
ax.set(title="Distribution of Penguin Body Mass", xlabel="Mass (g)", ylabel="Density")
plt.show()


ax = sns.histplot(
    data=penguins,
    x="body_mass_g",
    hue="species",
    element="step",
    stat="density",
    common_norm=False,
    bins=25
)
ax.set(title="Histograms by Species", xlabel="Mass (g)", ylabel="Density")
plt.show()



ax = sns.kdeplot(data=penguins, x="body_mass_g", fill=True, bw_adjust=1.0, alpha=0.5)
sns.kdeplot(data=penguins, x="body_mass_g", fill=False, bw_adjust=0.6, linestyle="--", ax=ax)
ax.set(title="KDE with Different Smoothing Levels", xlabel="Mass (g)", ylabel="Density")
plt.show()




ax = sns.kdeplot(
    data=penguins, x="body_mass_g",
    hue="species", fill=True, common_norm=False, alpha=0.5
)
ax.set(title="Body Mass Density by Species", xlabel="Mass (g)", ylabel="Density")
plt.show()





ax = sns.ecdfplot(
    data=tips,
    x="total_bill",
    hue="time",   # Lunch vs Dinner
    stat="proportion"
)
ax.set(title="ECDF: Total Bill by Time of Day", xlabel="Bill ($)", ylabel="Proportion ≤ x")
plt.show()



