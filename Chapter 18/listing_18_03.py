import threading, queue, time, numpy as np

q_in, q_out = queue.Queue(), queue.Queue()

def worker():
    batch = []
    while True:
        try:
            x = q_in.get(timeout=0.1)
            batch.append(x)
            if len(batch) >= 256:
                arr = np.array(batch); batch.clear()
                q_out.put((arr.mean(), arr.std()))
        except queue.Empty:
            if batch:
                arr = np.array(batch); batch.clear()
                q_out.put((arr.mean(), arr.std()))

threading.Thread(target=worker, daemon=True).start()
