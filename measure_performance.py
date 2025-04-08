import threading
import time
from metrics.app_size import measure_app_size
from metrics.battery import measure_battery
from metrics.cpu_usage import measure_cpu_usage
from metrics.framerate import measure_framerate
from metrics.memory_usage import measure_memory_usage
from metrics.startup_time import fetch_startup_time

__finished = threading.Event()
__measure = threading.Event()
__trigger_framerate_measure = threading.Event()
__trigger_startup_measure = threading.Event()

class MeasureConfig:
    def __init__(self, package: str, measure_cpu: bool, measure_memory: bool, 
                 measure_battery: bool, measure_app_size: bool):
        self.package = package
        self.measure_cpu = measure_cpu
        self.measure_memory = measure_memory
        self.measure_battery = measure_battery
        self.measure_app_size = measure_app_size

def measure_performance(config: MeasureConfig):
    last_measure_time = time.time()
    while not __finished.is_set():
        if __measure.is_set():
            if time.time() - last_measure_time < 2: continue
            if config.measure_cpu: 
                cpu_usage = measure_cpu_usage(config.package)
            if config.measure_memory: 
                memory_usage = measure_memory_usage(config.package)
            if config.measure_battery: 
                battery_charge = measure_battery()
            last_measure_time = time.time()
        else:
            if __trigger_framerate_measure.is_set():
                __trigger_framerate_measure.clear()
                p_50, p_90, p_95, p_99, p_gpu_50, p_gpu_90, p_gpu_95, p_gpu_99 = measure_framerate(config.package)
            if __trigger_startup_measure.is_set():
                __trigger_startup_measure.clear()
                startup_time = fetch_startup_time()
    app_size = measure_app_size(config.package)

def finish():
    __finished.set()

def start_measuring():
    __measure.set()

def complete_measuring():
    __measure.clear()

def trigger_framerate_measure():
    __trigger_framerate_measure.set()

def trigger_startup_measure():
    __trigger_startup_measure.set()
