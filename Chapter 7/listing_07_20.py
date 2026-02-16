import threading, time, queue
import numpy as np, matplotlib.pyplot as plt
from collections import deque

q = queue.Queue(maxsize=1000)

def producer():
    t = 0.0
    while True:
        time.sleep(0.02)  # ~50 Hz
        t += 0.02
        val = np.sin(2*np.pi*0.5*t) + 0.1*np.random.randn()
        try:
            q.put_nowait((t, val))
        except queue.Full:
            pass

threading.Thread(target=producer, daemon=True).start()

fig, ax = plt.subplots(figsize=(8, 4))
(line,) = ax.plot([], [], lw=1.8)
ax.grid(True, alpha=0.25)
ax.set_title("Streaming via queue (thread-safe)")

tx, ty = deque(maxlen=500), deque(maxlen=500)
timer = fig.canvas.new_timer(interval=30)

def on_timer(_):
    while True:
        try:
            t, v = q.get_nowait()
            tx.append(t); ty.append(v)
        except queue.Empty:
            break
    if tx:
        left = tx[-1] - 10.0
        xs = np.array(tx) - max(0.0, left)
        line.set_data(xs, np.array(ty))
        ax.set_xlim(0, 10.0)
        fig.canvas.draw_idle()

timer.add_callback(on_timer, None)
timer.start()
plt.show()
