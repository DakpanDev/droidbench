import threading
import time
from metrics.app_size import measure_app_size
from metrics.battery import measure_battery
from metrics.cpu_usage import measure_cpu_usage
from metrics.framerate import measure_framerate
from metrics.logging import *
from metrics.memory_usage import measure_memory_usage
from metrics.startup_time import fetch_startup_time
from save_results import save_benchmark_results

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
    start_measure_time = time.time()
    cpu_measurements = []
    memory_measurements = []
    battery_measurements = []
    framerate_measurements = []
    startup_measurements = []
    last_measure_time = time.time()
    while not __finished.is_set():
        if __measure.is_set():
            if time.time() - last_measure_time < 2: continue
            time_of_measure = time.time() - start_measure_time
            if config.measure_cpu: 
                cpu_usage = measure_cpu_usage(config.package)
                if cpu_usage != None:
                    cpu_measurements.append((time_of_measure, cpu_usage))
                log_cpu_usage(cpu_usage)
            if config.measure_memory: 
                memory_usage = measure_memory_usage(config.package)
                if memory_measurements != None: 
                    memory_measurements.append((time_of_measure, memory_usage))
                log_memory_usage(memory_usage)
            if config.measure_battery: 
                battery_charge = measure_battery()
                if battery_charge != None: 
                    battery_measurements.append((time_of_measure, battery_charge))
                log_battery_charge(battery_charge)
            last_measure_time = time.time()
        else:
            if __trigger_framerate_measure.is_set():
                __trigger_framerate_measure.clear()
                framerates = measure_framerate(config.package)
                if framerates != None: framerate_measurements.append(framerates)
                log_framerates(framerates)
            if __trigger_startup_measure.is_set():
                __trigger_startup_measure.clear()
                startup_time = fetch_startup_time()
                if startup_time != None: startup_measurements.append(startup_time)
                log_startup_time(startup_time)
    app_size = measure_app_size(config.package)
    log_app_size(app_size)
    save_benchmark_results(config.package, app_size, startup_measurements, cpu_measurements,
                           memory_measurements, battery_measurements, framerate_measurements)

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
