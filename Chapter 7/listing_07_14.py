import ipywidgets as widgets
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 10, 400)
y = x**2 * np.exp(-x)

fig, ax = plt.subplots(figsize=(7, 4))
(line,) = ax.plot(x, y, lw=2)
ax.grid(True, alpha=0.25)
ax.set_title("Style Control Panel")

logy_cb = widgets.Checkbox(False, description="Log Y")

# IMPORTANT: Dropdown options use (label, value), not (value, label).
style_dd = widgets.Dropdown(
    options=[("Solid", "-"), ("Dashed", "--"), ("Dotted", ":")],
    value="-",
    description="Line"
)

color_dd = widgets.Dropdown(
    options=["C0", "C1", "C2", "C3", "C4"],
    value="C0",
    description="Color"
)

def refresh(*_):
    ax.set_yscale("log" if logy_cb.value else "linear")
    line.set_linestyle(style_dd.value)
    line.set_color(color_dd.value)
    fig.canvas.draw_idle()

for w in (logy_cb, style_dd, color_dd):
    w.observe(refresh, names="value")

display(widgets.HBox([logy_cb, style_dd, color_dd]))
