import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

custom = ["#264653", "#2a9d8f", "#e9c46a", "#f4a261", "#e76f51"]
sns.catplot(
    data=tips, x="day", y="total_bill",
    kind="bar",
    palette=custom
)
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

fmri = sns.load_dataset("fmri")
cmap = sns.cubehelix_palette(as_cmap=True, rot=.3, gamma=.8)

sns.relplot(
    data=fmri, x="timepoint", y="signal",
    kind="line",
    hue="timepoint", palette=cmap,  # gradient over time
    col="region", col_wrap=2
)
plt.show()
