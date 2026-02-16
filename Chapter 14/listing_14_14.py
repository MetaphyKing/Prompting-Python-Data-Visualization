import matplotlib.dates as mdates

def format_time_axis(ax: plt.Axes, month_interval: int = 2, fmt: str = "%b %Y") -> None:
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=month_interval))
    ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))
    for label in ax.get_xticklabels():
        label.set_rotation(0)

def add_vline(ax: plt.Axes, when, label: str, y_pos: float = 0.95) -> None:
    ax.axvline(when, linestyle="--", linewidth=1)
    ymax = ax.get_ylim()[1]
    ax.text(when, ymax * y_pos, label, va="top", ha="left")
