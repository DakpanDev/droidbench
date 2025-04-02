import os

__PSS_INDEX = 2

def measure_memory_usage(package: str):
    stream = os.popen(f'adb shell dumpsys meminfo {package} | grep "TOTAL PSS"')
    res_values = stream.read().split(' ')
    res_values = list(filter(lambda x: len(x) > 0, res_values))
    if len(res_values) > __PSS_INDEX + 1:
        # TODO: place into CSV
        print(f'Memory Usage: {res_values[__PSS_INDEX]}kB')
