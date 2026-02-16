fig, ax = plt.subplots(figsize=(7, 4))
ax.plot([1, 2, 3, 4], [2, 3, 2.5, 3.5], marker="o")

ax.set_title("Indicator dynamics", loc="left")
ax.set_xlabel("Quarter")
ax.set_ylabel("Value, units")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.tick_params(direction="out")
ax.grid(True, alpha=0.25)
plt.tight_layout()
plt.show()


fig.savefig("figure_4_2.png", dpi=300, bbox_inches="tight")
fig.savefig("figure_4_2.svg", bbox_inches="tight")


