import csv
import json
import os

# Path and Filenames
__RESULTS_FOLDER = 'results'
__APP_SIZE_FILENAME = 'app_size.json'
__STARTUP_TIME_FILENAME = 'startup_time.csv'
__CPU_USAGE_FILENAME = 'cpu_usage.csv'
__MEMORY_USAGE_FILENAME = 'memory_usage.csv'
__BATTERY_CHARGE_FILENAME = 'battery_charge.csv'

# Field Names
__STARTUP_TIME_FIELDNAME = 'Time (ms)'
__TIME_OF_MEASURING_FIELDNAME = 'Time of measuring (s)'
__CPU_USAGE_FIELDNAME = 'CPU Usage (%)'
__MEMORY_USAGE_FIELDNAME = 'Memory Usage (kB)'
__BATTERY_CHARGE_FIELDNAME = 'Battery Charge (mAh)'

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
