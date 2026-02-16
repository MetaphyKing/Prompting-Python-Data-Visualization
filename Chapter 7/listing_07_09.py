import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(8, 4))

# IMPORTANT: When using blit=True, the animated=True flag is required for artists
# that you want Matplotlib to blit efficiently. If you forget it, Matplotlib may
# silently redraw the entire figure on each frame (much slower).
(line,) = ax.plot([], [], lw=2, animated=True)
(point,) = ax.plot([], [], "o", ms=6, animated=True)

ax.set_xlim(0, 10)
ax.set_ylim(-1.5, 1.5)
ax.grid(True, alpha=0.2)

t = np.linspace(0, 10, 300)
y = np.sin(2*np.pi*0.5*t)

def init():
    line.set_data([], [])
    point.set_data([], [])
    return (line, point)

def update(frame):
    line.set_data(t[:frame], y[:frame])     # history
    point.set_data(t[frame-1], y[frame-1])  # current point
    return (line, point)

ani = FuncAnimation(fig, update, frames=len(t),
                    init_func=init, blit=True, interval=15)

plt.show()
