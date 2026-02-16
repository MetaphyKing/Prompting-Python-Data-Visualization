import matplotlib.pyplot as plt
import numpy as np

xv = df.index.to_numpy()
y = df["A"].to_numpy()
imax = int(np.argmax(y))

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(xv, y, color="#4C78A8", linewidth=2.2)
ax.scatter([xv[imax]], [y[imax]], s=48, color="#4C78A8")

ax.annotate("Peak of series A",
            xy=(xv[imax], y[imax]), xycoords="data",
            xytext=(8, 10), textcoords="offset points",
            ha="left", va="bottom",
            arrowprops=dict(arrowstyle="-|>", linewidth=1.0, relpos=(0.0, 0.5)),
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#888", alpha=0.85))

ax.set_title("Neat annotation with offset and background", loc="left", fontweight="bold")
ax.set_xlabel("x (rad)")
ax.set_ylabel("value")
ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, df["B"], color="#F58518", linewidth=2.2)
ax.text(0.02, 0.98, "Note: no smoothing applied",
        transform=ax.transAxes, ha="left", va="top",
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#ccc", alpha=0.85))
ax.set_title("Fixed text in axes coordinate system", loc="left")
ax.grid(True, axis="y", alpha=0.25)
plt.tight_layout()
plt.show()



fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, df["C"], color="#54A24B", linewidth=2.2)
ax.set_title(r"Estimates of $\mu$ and $\sigma$ for series C", loc="left")
ax.set_xlabel(r"$x$ (rad)")
ax.set_ylabel(r"$y$")
ax.grid(True, alpha=0.25)
plt.tight_layout()
plt.show()


fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.plot(df.index, df["A"], color="#4C78A8", linewidth=2.2)

ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
ax.xaxis.set_minor_locator(AutoMinorLocator(n=2))
ax.yaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_minor_locator(AutoMinorLocator(n=2))
ax.yaxis.set_major_formatter(StrMethodFormatter("{x:.2f}"))

ax.tick_params(axis="both", which="major", direction="out", length=5)
ax.tick_params(axis="both", which="minor", direction="out", length=3)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

ax.grid(True, which="major", axis="y", alpha=0.25)
ax.set_title("Locators and formatters: moderate number of major ticks", loc="left")
plt.tight_layout()
plt.show()




