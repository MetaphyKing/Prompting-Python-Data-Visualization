fig, ax = plt.subplots(figsize=(8, 4))
(line,) = ax.plot([], [], lw=1.8, animated=True)
ax.set_ylim(-1.2, 1.2)
ax.grid(True, alpha=0.2)

t = np.linspace(0, 40, 800)
y = np.sin(t) + 0.2*np.sin(5*t)
window = 10

def init():
    line.set_data([], [])
    ax.set_xlim(0, window)
    return (line,)

def update(i):
    left = max(0, t[i] - window)
    right = left + window
    mask = (t >= left) & (t <= right)
    line.set_data(t[mask], y[mask])
    ax.set_xlim(left, right)  # move window (changes axis limits)
    return (line,)

# NOTE: Because x-limits change every frame, Matplotlib must redraw the axes,
# ticks, and grid, which effectively disables most blitting optimizations.
# Therefore, blit=False is intentional here to avoid artifacts and keep behavior stable.
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=False, interval=20)
plt.show()
