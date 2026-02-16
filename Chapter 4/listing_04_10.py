for side in ["top", "right"]:
    ax.spines[side].set_visible(False)
ax.tick_params(direction="out")
ax.set_axisbelow(True)  # draw grid beneath data
