import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates  # will be useful later
from matplotlib.animation import FuncAnimation
from IPython.display import HTML  # recommended for Colab/Jupyter display

# Example data: sine wave on a uniform grid
x = np.linspace(0, 2*np.pi, 256)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(8, 4))
(line,) = ax.plot([], [], lw=2, animated=True)  # pre-create artist

ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.2, 1.2)
ax.set_title("Line being drawn point by point")
ax.grid(True, alpha=0.2)

def init():
    # Reset before start
    line.set_data([], [])
    return (line,)

def update(frame):
    # frame = number of points to display
    line.set_data(x[:frame], y[:frame])
    return (line,)

ani = FuncAnimation(
    fig, update, frames=len(x), init_func=init,
    blit=True, interval=20, repeat=True
)

# Display (recommended, works well in Colab)
HTML(ani.to_jshtml())

# In some environments this may also work:
# plt.show()
