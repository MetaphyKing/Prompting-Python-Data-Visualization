import matplotlib.colors as mcolors
import matplotlib.cm as cm

values = df["A"].to_numpy()
norm = mcolors.Normalize(vmin=values.min(), vmax=values.max())
cmap = cm.get_cmap("viridis")
colors = cmap(norm(values))

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.scatter(df.index, values, c=colors, s=36, edgecolor="none")
ax.grid(True, alpha=0.3)
ax.set_title("Continuous colormap for series A (viridis)")
plt.show()


fig, ax = plt.subplots(figsize=(6.4, 3.6))
y = df["C"].to_numpy()
xv = df.index.to_numpy()
imax = int(np.argmax(y))
ax.plot(xv, y, color="#9467bd", linewidth=2.2)
ax.plot([xv[imax]], [y[imax]], marker="o", markersize=6, color="#9467bd")
ax.annotate("local maximum", xy=(xv[imax], y[imax]), xytext=(xv[imax]+0.35, y[imax]+0.2),
            arrowprops=dict(arrowstyle="->", linewidth=1),
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#888", alpha=0.85))
ax.grid(True, alpha=0.3)
ax.set_title("Highlighting a key event")
plt.show()


# Default version
fig, ax = plt.subplots(figsize=(6.0, 3.2))
for c in df.columns:
    ax.plot(df.index, df[c], label=c)
ax.legend()
ax.set_title("Default settings")
ax.grid(True, alpha=0.2)
plt.show()

# Improved version
from cycler import cycler
import matplotlib as mpl
mpl.rcParams['axes.prop_cycle'] = cycler(color=["#4C78A8", "#F58518", "#54A24B"])

fig, ax = plt.subplots(figsize=(6.0, 3.2))
ax.plot(df.index, df["A"], linewidth=2.6, label="A (primary)")
ax.plot(df.index, df["B"], linewidth=2.0, linestyle="--", alpha=0.9, label="B")
ax.plot(df.index, df["C"], linewidth=2.0, linestyle="-.", alpha=0.9, label="C")
ax.grid(True, axis="y", alpha=0.25)
ax.set_title("Three adjustments: palette, thickness, external legend")
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), borderaxespad=0.)
plt.tight_layout()
plt.show()
