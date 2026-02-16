ax.plot(x, y, zorder=3)
ax.scatter(x, y, s=50, zorder=4)  # points above the line
ax.grid(True, zorder=0)

ax.set_xlim(-0.2, 3.2)
ax.margins(x=0.02, y=0.05)

ax.legend(loc="upper left", frameon=False)
# place the legend outside the panel
ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1.0), borderaxespad=0.)
