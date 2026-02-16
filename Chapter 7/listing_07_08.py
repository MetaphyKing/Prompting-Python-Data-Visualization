import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(0)
n = 200
x = np.random.randn(n).cumsum()
y = np.random.randn(n).cumsum()

fig, ax = plt.subplots(figsize=(6, 6))
sc = ax.scatter([], [], s=20, alpha=0.8, animated=True)

ax.set_xlim(x.min()-1, x.max()+1)
ax.set_ylim(y.min()-1, y.max()+1)
ax.set_title("Growing scatter")
ax.grid(True, alpha=0.2)

def init():
    sc.set_offsets(np.empty((0, 2)))
    return (sc,)

def update(frame):
    points = np.column_stack([x[:frame], y[:frame]])
    sc.set_offsets(points)
    return (sc,)

ani = FuncAnimation(fig, update, frames=n, init_func=init, blit=True, interval=25)
plt.show()
