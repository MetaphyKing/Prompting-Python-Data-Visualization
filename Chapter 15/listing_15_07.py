# file: on_new_file.py
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep
from run_visuals import main as run_main

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".csv"):
            run_main()

obs = Observer()
obs.schedule(Handler(), path="data/", recursive=False)
obs.start()
try:
    while True:
        sleep(1)
finally:
    obs.stop(); obs.join()
