import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\nahiy\OneDrive\Documents\Testting project 103"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"hey, {event.src.path}, has been created")

    def on_deleted(self, event):
        print(f"Oops, someone deleted {event.src.path}")

# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running... ")
except:
    KeyboardInterrupt
    print("stopped")
    Observer.stop()
           
          
