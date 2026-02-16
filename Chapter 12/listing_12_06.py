import seaborn as sns
import matplotlib.pyplot as plt
import ipywidgets as widgets

tips = sns.load_dataset("tips")

def draw(kind="scatter", hue="sex", col="day", wrap=0, alpha=0.7):
    plt.close("all")                  # avoid duplicate outputs in the notebook
    sns.set_theme(style="whitegrid")  # reset style each time

    if kind == "scatter":
        g = sns.relplot(
            data=tips, x="total_bill", y="tip",
            hue=(hue if hue != "None" else None),
            col=(col if col != "None" else None),
            col_wrap=(wrap or None),
            kind="scatter", height=3.2, aspect=1.1, alpha=alpha
        )
    elif kind == "reg":
        g = sns.lmplot(
            data=tips, x="total_bill", y="tip",
            hue=(hue if hue != "None" else None),
            col=(col if col != "None" else None),
            col_wrap=(wrap or None),
            height=3.2, aspect=1.1,
            scatter_kws=dict(alpha=alpha, s=20)
        )
    else:  # distributions
        g = sns.displot(
            data=tips, x="total_bill",
            hue=(hue if hue != "None" else None),
            col=(col if col != "None" else None),
            col_wrap=(wrap or None),
            kind="hist", bins=20, height=3.2, aspect=1.1
        )
    g.set_xlabels("Total bill")
    g.set_ylabels("Tip" if kind in ("scatter","reg") else "Count")
    plt.show()

widgets.interact(
    draw,
    kind=widgets.ToggleButtons(options=[("Scatter","scatter"),("Regress","reg"),("Histogram","hist")]),
    hue=widgets.Dropdown(options=["None","sex","smoker","time"], value="sex", description="Hue"),
    col=widgets.Dropdown(options=["None","day","time","smoker"], value="day", description="Cols"),
    wrap=widgets.IntSlider(min=0, max=4, step=1, value=2, description="col_wrap"),
    alpha=widgets.FloatSlider(min=0.2, max=1.0, step=0.1, value=0.7, description="alpha")
);
