# In Jupyter:


import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

x = np.linspace(0, 2*np.pi, 500)
fig, ax = plt.subplots(figsize=(7, 4))
(line,) = ax.plot(x, np.sin(x), lw=2)
ax.set_ylim(-1.2, 1.2)
ax.grid(True, alpha=0.25)
ax.set_title("Sine with Interactive Parameters")

def update(freq=1.0, phase=0.0):
    line.set_ydata(np.sin(freq * x + phase))
    fig.canvas.draw_idle()  # redraw only

interact(
    update,
    freq=FloatSlider(value=1.0, min=0.2, max=5.0, step=0.1, description="Frequency"),
    phase=FloatSlider(value=0.0, min=-np.pi, max=np.pi, step=0.1, description="Phase"),
)
