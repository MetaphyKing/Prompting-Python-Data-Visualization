import matplotlib.pyplot as plt
import seaborn as sns

def bar_with_zero_baseline(ax: plt.Axes, data, x, y, **kwargs) -> None:
    sns.barplot(data=data, x=x, y=y, ax=ax, **kwargs)
    ymin, ymax = ax.get_ylim()
    ax.set_ylim(bottom=min(0, ymin), top=ymax)  # enforce zero at the bottom

