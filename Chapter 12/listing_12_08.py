from functools import lru_cache
penguins = sns.load_dataset("penguins").dropna()

@lru_cache(maxsize=8)
def vars_by_granularity(gran):
    if gran == "basic":
        return ["bill_length_mm","bill_depth_mm"]
    return ["bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]

def draw_pair(gran="basic", corner=True):
    plt.close("all"); sns.set_theme()
    v = vars_by_granularity(gran)
    g = sns.PairGrid(penguins, vars=v, hue="species", corner=corner)
    g.map_lower(sns.scatterplot, s=16, alpha=0.6)
    g.map_diag(sns.kdeplot, fill=True, alpha=0.6)
    g.add_legend(title="Species")
    g.figure.set_size_inches(8, 7)
    plt.show()

widgets.interact(
    draw_pair,
    gran=widgets.ToggleButtons(options=[("Basic","basic"),("Extended","full")]),
    corner=widgets.Checkbox(value=True, description="corner")
);


def themed(style="whitegrid", context="notebook", palette="deep"):
    plt.close("all")
    sns.set_theme(style=style, context=context, palette=palette)
    sns.displot(tips, x="total_bill", hue="sex", kind="kde", fill=True, height=3.2, aspect=1.2)
    plt.show()

widgets.interact(
    themed,
    style=widgets.Dropdown(options=["whitegrid","ticks","darkgrid","white","dark"]),
    context=widgets.Dropdown(options=["paper","notebook","talk","poster"], value="notebook"),
    palette=widgets.Dropdown(options=["deep","muted","bright","colorblind"])
);
