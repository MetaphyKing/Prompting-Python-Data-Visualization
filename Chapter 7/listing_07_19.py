import numpy as np, matplotlib.pyplot as plt
from collections import deque

fig, ax = plt.subplots(figsize=(8, 4))
ax.grid(True, alpha=0.25)
ax.set_title("Real-time: pause/resume with spacebar")

window = 10.0    # seconds
fps = 25
maxlen = int(window * fps)
tx, ty = deque(maxlen=maxlen), deque(maxlen=maxlen)

(line,) = ax.plot([], [], lw=1.8)
ax.set_xlim(0, window)
ax.set_ylim(-2, 2)

running, t = True, 0.0
timer = fig.canvas.new_timer(interval=int(1000/fps))

def on_timer(_):
    global t
    if not running:
        return
    t += 1.0/fps
    val = np.sin(2*np.pi*0.5*t) + 0.2*np.random.randn()
    tx.append(t); ty.append(val)
    left = max(0, t - window)
    line.set_data(np.array(tx) - left, np.array(ty))
    ax.set_xlim(0, window)
    if len(ty) % (fps//2) == 0:
        ymin, ymax = min(ty), max(ty)
        pad = 0.1*(ymax - ymin if ymax > ymin else 1.0)
        ax.set_ylim(ymin - pad, ymax + pad)
    fig.canvas.draw_idle()

timer.add_callback(on_timer, None)
timer.start()

def on_key(event):
    global running, t
    if event.key == " ":
        running = not running
    elif event.key == "r":
        tx.clear(); ty.clear()
        t = 0.0
        line.set_data([], [])
        fig.canvas.draw_idle()



cid_key = fig.canvas.mpl_connect("key_press_event", on_key)
plt.show()
