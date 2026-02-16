
import numpy as np, pandas as pd, matplotlib.pyplot as plt
import ipywidgets as widgets
from ipywidgets import SelectionRangeSlider

dates = pd.date_range("2024-01-01", "2024-06-30", freq="D")
y = pd.Series(100 + np.cumsum(np.random.normal(0, 1.0, len(dates))), index=dates)

fig, ax = plt.subplots(figsize=(8, 4))
(line,) = ax.plot(y.index, y.values, lw=1.8)
ax.grid(True, alpha=0.25)
ax.set_title("Selecting Interval on a Time Series")

rng = SelectionRangeSlider(
    options=[(d.strftime("%Y-%m-%d"), d) for d in dates],
    index=(0, len(dates) - 1),
    description="Period",
    layout={"width": "800px"}
)

def on_range_change(change):
    left, right = change["new"]

    # Safety: clamp the selected range to the available data index
    idx_min, idx_max = y.index.min(), y.index.max()
    left = max(left, idx_min)
    right = min(right, idx_max)

    # Guard against invalid ranges
    if left >= right:
        return

    mask = (y.index >= left) & (y.index <= right)

    # Guard: if no points fall inside the range, do not redraw to a blank plot
    if not mask.any():
        return

    line.set_data(y.index[mask], y.values[mask])
    ax.set_xlim(left, right)

    ymin, ymax = y.values[mask].min(), y.values[mask].max()
    pad = 0.05 * (ymax - ymin if ymax > ymin else 1.0)
    ax.set_ylim(ymin - pad, ymax + pad)

    fig.canvas.draw_idle()
