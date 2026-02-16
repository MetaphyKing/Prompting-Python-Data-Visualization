import numpy as np, matplotlib.pyplot as plt
import ipywidgets as widgets

x = np.linspace(0, 2*np.pi, 500)
fig, ax = plt.subplots(figsize=(7, 4))
(line,) = ax.plot(x, np.sin(x), lw=2)
ax.set_ylim(-1.2, 1.2); ax.grid(True, alpha=0.25)

play   = widgets.Play(interval=40, value=0, min=0, max=200, step=1)
slider = widgets.IntSlider(min=0, max=200, step=1, description="Frame")
widgets.jslink((play, "value"), (slider, "value"))

def on_frame_change(change):
    i = change["new"]
    phase = i * 0.05
    line.set_ydata(np.sin(x + phase))
    fig.canvas.draw_idle()

slider.observe(on_frame_change, names="value")
display(widgets.HBox([play, slider]))
