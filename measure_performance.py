import threading
import time
import os
from metrics.cpu_usage import measure_cpu_usage

__STOP = threading.Event()

def measure_performance(package: str):
    while not __STOP.is_set():
        measure_cpu_usage(package)
        time.sleep(1)

def stop_measuring():
    __STOP.set()
