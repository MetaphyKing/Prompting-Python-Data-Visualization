import matplotlib.ticker as mtick

# major ticks at integers, minor ticks at halves
ax.xaxis.set_major_locator(mtick.MultipleLocator(1))
ax.xaxis.set_minor_locator(mtick.MultipleLocator(0.5))

# percentage format on the y-axis
ax.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))
ax.tick_params(axis="both", which="major", labelsize=10, direction="out", length=6)
ax.tick_params(axis="both", which="minor", length=3)

