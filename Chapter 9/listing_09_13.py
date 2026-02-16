import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks", palette="deep")
with sns.plotting_context("talk", font_scale=1.05):
    g = sns.relplot(
        data=sns.load_dataset("fmri"),
        x="timepoint", y="signal",
        hue="event", style="region",
        kind="line", col="region", col_wrap=2,
        height=3.0, aspect=1.2
    )
    g.set_axis_labels("Time (scan)", "Signal (a.u.)")
    g.add_legend()
    g.set_titles("{col_name}")  # concise titles
    for ax in g.axes.flat:
        sns.despine(ax=ax, trim=True)
    plt.show()


plt.savefig("figure.pdf", bbox_inches="tight")


plt.savefig("figure.png", dpi=150, bbox_inches="tight")

