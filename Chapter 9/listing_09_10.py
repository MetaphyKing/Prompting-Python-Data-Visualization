import seaborn as sns
sns.set_theme(context="notebook")  # sensible default for interactive work



import seaborn as sns
import matplotlib.pyplot as plt

with sns.plotting_context("talk", font_scale=1.1):
    ax = sns.lineplot(x=[0,1,2,3], y=[1,2,1.5,3])
    ax.set_title("Demo in talk context")
    plt.show()
