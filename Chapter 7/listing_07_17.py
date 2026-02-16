import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 500)
y = np.sin(x) + 0.2*np.cos(3*x)

fig, ax = plt.subplots(figsize=(8, 4))
(line,) = ax.plot(x, y, lw=2)
ax.grid(True, alpha=0.25)
ax.set_title("Click: add/remove marker")

vlines, labels = [], []

def on_click(event):
    if event.inaxes != ax:
        return
    # Left button → add marker
    if event.button == 1:
        xv = event.xdata
        i = np.searchsorted(x, xv)
        i = np.clip(i, 1, len(x)-1)
        ii = i if abs(x[i]-xv) < abs(x[i-1]-xv) else i-1
        xv, yv = x[ii], y[ii]

        v = ax.axvline(xv, ls="--", alpha=0.6)
        t = ax.text(xv, yv, f"x={xv:.2f}\ny={yv:.2f}",
                    ha="left", va="bottom", fontsize=9,
                    bbox=dict(fc="white", ec="0.7", alpha=0.8))
        vlines.append(v); labels.append(t)
        fig.canvas.draw_idle()
    # Right button → remove last marker
    elif event.button == 3 and vlines:
        vlines.pop().remove()
        labels.pop().remove()
        fig.canvas.draw_idle()

cid_click = fig.canvas.mpl_connect("button_press_event", on_click)
plt.show()
