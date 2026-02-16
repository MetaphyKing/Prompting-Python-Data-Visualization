import seaborn as sns


import seaborn as sns
import matplotlib.pyplot as plt

with sns.axes_style("ticks"):
    ax = sns.scatterplot(x=[1,2,3], y=[3,2,4])
    sns.despine()  # remove top and right spines
    plt.show()


import seaborn as sns
import matplotlib.pyplot as plt

ax = sns.boxplot(x=["A","B","C","D"], y=[1,2,1.5,2.2])
sns.despine(offset=3, trim=True)  # small offset, trimmed spines
plt.show()



import seaborn as sns
sns.set_theme(
    context="notebook",
    style="whitegrid",
    palette="colorblind"
)





import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(context="notebook", style="whitegrid")

with sns.plotting_context("paper", font_scale=0.95), sns.axes_style("white"):
    ax = sns.histplot([1,1,2,2,2,3,3,4], bins=4)
    sns.despine()
    plt.show()
