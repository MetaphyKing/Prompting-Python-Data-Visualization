from cycler import cycler
import matplotlib as mpl

mpl.rcParams['axes.prop_cycle'] = cycler(color=["#4C78A8", "#F58518", "#54A24B", "#E45756", "#72B7B2"])
fig, ax = plt.subplots(figsize=(6.4, 3.6))
for col in df.columns:
    ax.plot(df.index, df[col], linewidth=2.2, label=col)
ax.legend(ncol=3, frameon=True, framealpha=0.9)
ax.grid(True, alpha=0.25)
ax.set_title("Consistent color cycle via rcParams")
plt.show()
