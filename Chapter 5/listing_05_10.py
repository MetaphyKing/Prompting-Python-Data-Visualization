from matplotlib.ticker import MaxNLocator, StrMethodFormatter

fig, ax = plt.subplots(figsize=(6.6, 3.6))
ax.plot(df.index, df["A"], color="#4C78A8", linewidth=2.2)

ax.set_title("Publication layout: fonts, annotation, axes", loc="left", fontweight="bold")
ax.set_xlabel("x (rad)")
ax.set_ylabel("value")

ax.xaxis.set_major_locator(MaxNLocator(nbins=6))
ax.yaxis.set_major_formatter(StrMethodFormatter("{x:.2f}"))
ax.grid(True, axis="y", alpha=0.25)
for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)

x0 = df.index.values[20]
y0 = df["A"].iloc[20]
ax.annotate("Key point",
            xy=(x0, y0), xycoords="data",
            xytext=(10, 12), textcoords="offset points",
            ha="left", va="bottom",
            arrowprops=dict(arrowstyle="->", linewidth=1.0),
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#888", alpha=0.85))

plt.tight_layout()
plt.show()
