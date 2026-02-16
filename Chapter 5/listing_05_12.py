
from cycler import cycler
import matplotlib as mpl

palette = ["#4C78A8", "#F58518", "#54A24B", "#E45756", "#72B7B2"]
mpl.rcParams["axes.prop_cycle"] = cycler(color=palette)

fig, axes = plt.subplots(1, 2, figsize=(9.0, 3.6), sharex=True)
axes[0].plot(df.index, df["A"], label="A")
axes[0].plot(df.index, df["B"], label="B")
axes[0].set_title("Lines: unified palette", loc="left")
axes[0].legend(ncol=2)

axes[1].bar(["A","B","C"], [df["A"].mean(), df["B"].mean(), df["C"].mean()])
axes[1].set_title("Bars: same palette", loc="left")

for ax in axes:
    ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout(); plt.show()

# base style + local overrides via rc_context
base_styles = ["ggplot"]  
local_overrides = {"lines.linewidth": 2.4, "axes.titleweight": "bold"}

with plt.style.context(base_styles):
    with plt.rc_context(local_overrides):
        fig, ax = plt.subplots(figsize=(6.6, 3.6))
        ax.plot(df.index, df["A"], label="A")
        ax.plot(df.index, df["B"], label="B", linestyle="--")
        ax.set_title("Style composition: base + local tweaks", loc="left")
        ax.legend()
        plt.tight_layout(); plt.show()
