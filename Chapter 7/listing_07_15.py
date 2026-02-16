import numpy as np, matplotlib.pyplot as plt
import ipywidgets as widgets

x = np.linspace(0, 6*np.pi, 800)
fig, ax = plt.subplots(figsize=(7, 4))
(line,) = ax.plot(x, np.sin(x), lw=2)
ax.grid(True, alpha=0.25)

amp   = widgets.FloatSlider(1.0, min=0.1, max=3.0, step=0.1, description="Amplitude")
freq  = widgets.FloatSlider(1.0, min=0.2, max=3.0, step=0.1, description="Frequency")
phase = widgets.FloatSlider(0.0, min=-np.pi, max=np.pi, step=0.1, description="Phase")

out = widgets.interactive_output(
    lambda amplitude, frequency, phase_: (
        line.set_ydata(amplitude * np.sin(frequency * x + phase_)),
        fig.canvas.draw_idle()
    ),
    {"amplitude": amp, "frequency": freq, "phase_": phase}
)

display(widgets.VBox([widgets.HBox([amp, freq, phase]), out]))
