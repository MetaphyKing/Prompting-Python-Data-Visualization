import pandas as pd
unique_days = ["Thur","Fri","Sat","Sun"]

def draw_slice(day=unique_days, smokers="both"):
    plt.close("all")
    df = tips.copy()
    if day:
        df = df[df["day"].isin(day)]
    if smokers != "both":
        df = df.query("smoker == @smokers")
    g = sns.catplot(
        data=df, x="day", y="tip", hue="sex",
        kind="violin", inner="quartile", height=3.4, aspect=1.2
    )
    g.set_axis_labels("Day", "Tip")
    g.add_legend()
    plt.show()

widgets.interact(
    draw_slice,
    day=widgets.SelectMultiple(options=unique_days, value=tuple(unique_days)),
    smokers=widgets.ToggleButtons(options=[("Both","both"),("Smokers","Yes"),("Non-smokers","No")])
);
kind_w = widgets.Dropdown(options=["scatter","reg","hist"], value="scatter", description="Kind")
hue_w  = widgets.Dropdown(options=["None","sex","smoker","time"], value="sex", description="Hue")
col_w  = widgets.Dropdown(options=["None","day","time"], value="day", description="Cols")
wrap_w = widgets.IntSlider(min=0, max=4, value=2, description="col_wrap")

out = widgets.interactive_output(
    draw, {"kind": kind_w, "hue": hue_w, "col": col_w, "wrap": wrap_w}
)

ui = widgets.VBox([
    widgets.HBox([kind_w, hue_w]),
    widgets.HBox([col_w, wrap_w])
])
display(ui, out)

