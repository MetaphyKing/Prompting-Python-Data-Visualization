import signal

class Timeout:
    def __init__(self, seconds): self.seconds = seconds
    def __enter__(self):
        signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
        signal.alarm(self.seconds)
    def __exit__(self, exc_type, exc, tb):
        signal.alarm(0)

with Timeout(30):
    note = run_chain("Report")


def run_with_retries(fn, attempts=3, delay=5):
    import time
    for i in range(attempts):
        try:
            return fn()
        except Exception as e:
            if i == attempts - 1:
                raise
            time.sleep(delay)
