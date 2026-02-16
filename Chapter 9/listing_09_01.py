import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins").dropna(subset=["bill_length_mm", "bill_depth_mm", "species"])

fig, ax = plt.subplots()
for species, sub in penguins.groupby("species"):
    ax.scatter(sub["bill_length_mm"], sub["bill_depth_mm"], label=species, alpha=0.8)
ax.set_xlabel("Bill length (mm)")
ax.set_ylabel("Bill depth (mm)")
ax.legend(title="Species")
ax.grid(True)
plt.show()




import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset("penguins").dropna(subset=["bill_length_mm", "bill_depth_mm", "species"])

sns.scatterplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm",
    hue="species", alpha=0.8
)
plt.xlabel("Bill length (mm)")
plt.ylabel("Bill depth (mm)")
plt.grid(True)
plt.show()
