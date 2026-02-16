import numpy as np, matplotlib.pyplot as plt

np.random.seed(0)
x = np.linspace(0, 10, 200)
y = np.sin(x) + 0.15*np.random.randn(len(x))

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(x, y, lw=1.5)
(marker,) = ax.plot([np.nan], [np.nan], "o", ms=8)
label = ax.text(0, 0, "", va="bottom", ha="left",
                bbox=dict(fc="white", ec="0.7", alpha=0.85))
ax.grid(True, alpha=0.25)
ax.set_title("Hover: highlight nearest point")

def on_move(event):
    if event.inaxes != ax:
        return
    pts = ax.transData.transform(np.column_stack([x, y]))
    mx, my = event.x, event.y
    d2 = (pts[:,0]-mx)**2 + (pts[:,1]-my)**2
    j = np.argmin(d2)
    if d2[j] < 20**2:  # 20-pixel threshold
        marker.set_data([x[j]], [y[j]])
        label.set_text(f"({x[j]:.2f}, {y[j]:.2f})")
        label.set_position((x[j], y[j]))
    else:
        marker.set_data([np.nan], [np.nan])
        label.set_text("")
    fig.canvas.draw_idle()

cid_move = fig.canvas.mpl_connect("motion_notify_event", on_move)
plt.show()

