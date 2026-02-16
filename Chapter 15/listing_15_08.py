# file: lock.py
import os, time
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def file_lock(path="artifacts/.lock", timeout=10):
    lock = Path(path)
    t0 = time.time()
    while lock.exists():
        if time.time() - t0 > timeout:
            raise TimeoutError("Unable to acquire lock")
        time.sleep(0.2)
    try:
        lock.write_text(str(os.getpid()))
        yield
    finally:
        if lock.exists():
            lock.unlink()


from lock import file_lock
with file_lock():
    return_code = main()
