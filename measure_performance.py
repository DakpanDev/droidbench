import threading
import time
from metrics.cpu_usage import measure_cpu_usage
from metrics.memory_usage import measure_memory_usage

class MeasureConfig:
    def __init__(self, package: str, measure_cpu: bool, measure_memory: bool, 
                 measure_battery: bool, measure_framerate: bool):
        self.package = package
        self.measure_cpu = measure_cpu
        self.measure_memory = measure_memory
        self.measure_battery = measure_battery
        self.measure_framerate = measure_framerate

__STOP = threading.Event()

def measure_performance(config: MeasureConfig):
    while not __STOP.is_set():
        if config.measure_cpu: measure_cpu_usage(config.package)
        if config.measure_memory: measure_memory_usage(config.package)
        time.sleep(1)

def stop_measuring():
    __STOP.set()
