import csv
import json
import os
from metrics.framerate import FIELD_OVERALL_P50, FIELD_OVERALL_P90, FIELD_OVERALL_P95, FIELD_OVERALL_P99, FIELD_GPU_P50, FIELD_GPU_P90, FIELD_GPU_P95, FIELD_GPU_P99

# Path and Filenames
__RESULTS_FOLDER = 'results'
__APP_SIZE_FILENAME = 'app_size.json'
__STARTUP_TIME_FILENAME = 'startup_time.csv'
__CPU_USAGE_FILENAME = 'cpu_usage.csv'
__MEMORY_USAGE_FILENAME = 'memory_usage.csv'
__BATTERY_CHARGE_FILENAME = 'battery_charge.csv'
__FRAMERATE_FILENAME = 'framerate.csv'

# Field Names
__STARTUP_TIME_FIELDNAME = 'Time (ms)'
__TIME_OF_MEASURING_FIELDNAME = 'Time of measuring (s)'
__CPU_USAGE_FIELDNAME = 'CPU Usage (%)'
__MEMORY_USAGE_FIELDNAME = 'Memory Usage (kB)'
__BATTERY_CHARGE_FIELDNAME = 'Battery Charge (mAh)'
__FIELD_OVERALL_P50_FIELDNAME = '50th Percentile (ms)'
__FIELD_OVERALL_P90_FIELDNAME = '90th Percentile (ms)'
__FIELD_OVERALL_P95_FIELDNAME = '95th Percentile (ms)'
__FIELD_OVERALL_P99_FIELDNAME = '99th Percentile (ms)'
__FIELD_GPU_P50_FIELDNAME = 'GPU 50th Percentile (ms)'
__FIELD_GPU_P90_FIELDNAME = 'GPU 90th Percentile (ms)'
__FIELD_GPU_P95_FIELDNAME = 'GPU 95th Percentile (ms)'
__FIELD_GPU_P99_FIELDNAME = 'GPU 99th Percentile (ms)'
__FRAMERATE_OVERALL_FIELDNAMES = [__FIELD_OVERALL_P50_FIELDNAME, __FIELD_OVERALL_P90_FIELDNAME, 
                                  __FIELD_OVERALL_P95_FIELDNAME, __FIELD_OVERALL_P99_FIELDNAME]
__FRAMERATE_GPU_FIELDNAMES = [__FIELD_GPU_P50_FIELDNAME, __FIELD_GPU_P90_FIELDNAME, __FIELD_GPU_P95_FIELDNAME, 
                              __FIELD_GPU_P99_FIELDNAME]

def __create_path(package: str) -> str:
    path = f'{__RESULTS_FOLDER}/{package.replace('.', '_')}'
    if not os.path.exists(path): os.makedirs(path)
    return path

def __save_app_size(path: str, app_size: dict):
    with open(f'{path}/{__APP_SIZE_FILENAME}', 'w') as file:
        json.dump(app_size, file)

def __save_startup_measurements(path: str, startup_measurements: list[int]):
    with open(f'{path}/{__STARTUP_TIME_FILENAME}', 'w') as file:
        fieldnames = [__STARTUP_TIME_FIELDNAME]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        for measurement in startup_measurements:
            writer.writerow([measurement])

def __save_cpu_measurements(path: str, cpu_measurements: list[tuple[float, float]]):
    with open(f'{path}/{__CPU_USAGE_FILENAME}', 'w') as file:
        fieldnames = [__TIME_OF_MEASURING_FIELDNAME, __CPU_USAGE_FIELDNAME]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        writer.writerows(cpu_measurements)

def __save_memory_measurements(path: str, memory_measurements: list[tuple[float, int]]):
    with open(f'{path}/{__MEMORY_USAGE_FILENAME}', 'w') as file:
        fieldnames = [__TIME_OF_MEASURING_FIELDNAME, __MEMORY_USAGE_FIELDNAME]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        writer.writerows(memory_measurements)

def __save_battery_measurements(path: str, battery_measurements: list[tuple[float, int]]):
    with open(f'{path}/{__BATTERY_CHARGE_FILENAME}', 'w') as file:
        fieldnames = [__TIME_OF_MEASURING_FIELDNAME, __BATTERY_CHARGE_FIELDNAME]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        writer.writerows(battery_measurements)

def __map_framerates(results: dict, has_gpu_fields: bool) -> dict:
    mapped = {
        __FIELD_OVERALL_P50_FIELDNAME: results[FIELD_OVERALL_P50],
        __FIELD_OVERALL_P90_FIELDNAME: results[FIELD_OVERALL_P90],
        __FIELD_OVERALL_P95_FIELDNAME: results[FIELD_OVERALL_P95],
        __FIELD_OVERALL_P99_FIELDNAME: results[FIELD_OVERALL_P99],
    }
    if has_gpu_fields:
        mapped[__FIELD_GPU_P50_FIELDNAME] = results[FIELD_GPU_P50]
        mapped[__FIELD_GPU_P90_FIELDNAME] = results[FIELD_GPU_P90]
        mapped[__FIELD_GPU_P95_FIELDNAME] = results[FIELD_GPU_P95]
        mapped[__FIELD_GPU_P99_FIELDNAME] = results[FIELD_GPU_P99]
    return mapped

def __save_framerates(path: str, framerates: list[dict]):
    with open(f'{path}/{__FRAMERATE_FILENAME}', 'w') as file:
        fieldnames = __FRAMERATE_OVERALL_FIELDNAMES
        has_gpu_fields = len(framerates) > 0 and len(framerates[0]) == 8
        if has_gpu_fields:
            fieldnames += __FRAMERATE_GPU_FIELDNAMES
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        mapped = [__map_framerates(results, has_gpu_fields) for results in framerates]
        writer.writerows(mapped)

def save_benchmark_results(package: str, app_size: dict, startup_measurements: list[int], 
                           cpu_measurements: list[tuple[float, float]], 
                           memory_measurements: list[tuple[float, int]],  
                           battery_measurements: list[tuple[float, int]],  framerates: list[dict]):
    path = __create_path(package)
    __save_app_size(path, app_size)
    __save_startup_measurements(path, startup_measurements)
    __save_cpu_measurements(path, cpu_measurements)
    __save_memory_measurements(path, memory_measurements)
    __save_battery_measurements(path, battery_measurements)
    __save_framerates(path, framerates)
