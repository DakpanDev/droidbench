import csv
import json
import os
from metrics.framerate import FIELD_OVERALL_P50, FIELD_OVERALL_P90, FIELD_OVERALL_P95, FIELD_OVERALL_P99, FIELD_GPU_P50, FIELD_GPU_P90, FIELD_GPU_P95, FIELD_GPU_P99

# Path and Filenames
RESULTS_FOLDER = 'results'
APP_SIZE_FILENAME = 'app_size.json'
STARTUP_TIME_FILENAME = 'startup_time.csv'
CPU_USAGE_FILENAME = 'cpu_usage.csv'
MEMORY_USAGE_FILENAME = 'memory_usage.csv'
BATTERY_CHARGE_FILENAME = 'battery_charge.csv'
FRAMERATE_FILENAME = 'framerate.csv'

# Field Names
STARTUP_TIME_FIELDNAME = 'Startup Time (ms)'
TIME_OF_MEASURING_FIELDNAME = 'Time of measuring (s)'
CPU_USAGE_FIELDNAME = 'CPU Usage (%)'
MEMORY_USAGE_FIELDNAME = 'Memory Usage (kB)'
BATTERY_CHARGE_FIELDNAME = 'Battery Charge (mAh)'
FIELD_OVERALL_P50_FIELDNAME = '50th Percentile (ms)'
FIELD_OVERALL_P90_FIELDNAME = '90th Percentile (ms)'
FIELD_OVERALL_P95_FIELDNAME = '95th Percentile (ms)'
FIELD_OVERALL_P99_FIELDNAME = '99th Percentile (ms)'
FIELD_GPU_P50_FIELDNAME = 'GPU 50th Percentile (ms)'
FIELD_GPU_P90_FIELDNAME = 'GPU 90th Percentile (ms)'
FIELD_GPU_P95_FIELDNAME = 'GPU 95th Percentile (ms)'
FIELD_GPU_P99_FIELDNAME = 'GPU 99th Percentile (ms)'
FRAMERATE_OVERALL_FIELDNAMES = [FIELD_OVERALL_P50_FIELDNAME, FIELD_OVERALL_P90_FIELDNAME, 
                                FIELD_OVERALL_P95_FIELDNAME, FIELD_OVERALL_P99_FIELDNAME]
FRAMERATE_GPU_FIELDNAMES = [FIELD_GPU_P50_FIELDNAME, FIELD_GPU_P90_FIELDNAME, FIELD_GPU_P95_FIELDNAME, 
                            FIELD_GPU_P99_FIELDNAME]

def create_path(package: str) -> str:
    path = f'{RESULTS_FOLDER}/{package.replace('.', '_')}'
    if not os.path.exists(path): os.makedirs(path)
    return path

def __save_app_size(path: str, app_size: dict):
    with open(f'{path}/{APP_SIZE_FILENAME}', 'w') as file:
        json.dump(app_size, file)

def __save_startup_measurements(path: str, startup_measurements: list[int]):
    with open(f'{path}/{STARTUP_TIME_FILENAME}', 'w') as file:
        fieldnames = [STARTUP_TIME_FIELDNAME]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        for measurement in startup_measurements:
            writer.writerow([measurement])

def __save_cpu_measurements(path: str, cpu_measurements: list[tuple[float, float]]):
    with open(f'{path}/{CPU_USAGE_FILENAME}', 'w') as file:
        fieldnames = [TIME_OF_MEASURING_FIELDNAME, CPU_USAGE_FIELDNAME]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        writer.writerows(cpu_measurements)

def __save_memory_measurements(path: str, memory_measurements: list[tuple[float, int]]):
    with open(f'{path}/{MEMORY_USAGE_FILENAME}', 'w') as file: 
        fieldnames = [TIME_OF_MEASURING_FIELDNAME, MEMORY_USAGE_FIELDNAME]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        writer.writerows(memory_measurements)

def __save_battery_measurements(path: str, battery_measurements: list[tuple[float, int]]):
    with open(f'{path}/{BATTERY_CHARGE_FILENAME}', 'w') as file:
        fieldnames = [TIME_OF_MEASURING_FIELDNAME, BATTERY_CHARGE_FIELDNAME]
        writer = csv.writer(file)
        writer.writerow(fieldnames)
        writer.writerows(battery_measurements)

def __map_framerates(results: dict, has_gpu_fields: bool) -> dict:
    mapped = {
        FIELD_OVERALL_P50_FIELDNAME: results[FIELD_OVERALL_P50],
        FIELD_OVERALL_P90_FIELDNAME: results[FIELD_OVERALL_P90],
        FIELD_OVERALL_P95_FIELDNAME: results[FIELD_OVERALL_P95],
        FIELD_OVERALL_P99_FIELDNAME: results[FIELD_OVERALL_P99],
    }
    if has_gpu_fields:
        mapped[FIELD_GPU_P50_FIELDNAME] = results[FIELD_GPU_P50]
        mapped[FIELD_GPU_P90_FIELDNAME] = results[FIELD_GPU_P90]
        mapped[FIELD_GPU_P95_FIELDNAME] = results[FIELD_GPU_P95]
        mapped[FIELD_GPU_P99_FIELDNAME] = results[FIELD_GPU_P99]
    return mapped

def __save_framerates(path: str, framerates: list[dict]):
    with open(f'{path}/{FRAMERATE_FILENAME}', 'w') as file:
        fieldnames = FRAMERATE_OVERALL_FIELDNAMES
        has_gpu_fields = len(framerates) > 0 and len(framerates[0]) == 8
        if has_gpu_fields:
            fieldnames += FRAMERATE_GPU_FIELDNAMES
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        mapped = [__map_framerates(results, has_gpu_fields) for results in framerates]
        writer.writerows(mapped)

def save_benchmark_results(package: str, app_size: dict, startup_measurements: list[int], 
                           cpu_measurements: list[tuple[float, float]], 
                           memory_measurements: list[tuple[float, int]],  
                           battery_measurements: list[tuple[float, int]],  framerates: list[dict]):
    path = create_path(package)
    __save_app_size(path, app_size)
    __save_startup_measurements(path, startup_measurements)
    __save_cpu_measurements(path, cpu_measurements)
    __save_memory_measurements(path, memory_measurements)
    __save_battery_measurements(path, battery_measurements)
    __save_framerates(path, framerates)
