ax.plot(x, y)
ax.text(0.02, 0.98, "Panel note", transform=ax.transAxes, va="top")
ax.annotate("Peak", xy=(2, 1), xytext=(2.4, 1.6),
            arrowprops=dict(arrowstyle="->"))
