import os

__PSS_INDEX = 2

def measure_memory_usage(package: str) -> int | None:
    stream = os.popen(f'adb shell dumpsys meminfo {package} | grep "TOTAL PSS"')
    res_values = stream.read().split(' ')
    res_values = list(filter(lambda x: len(x) > 0, res_values))
    return int(res_values[__PSS_INDEX]) if len(res_values) > __PSS_INDEX + 1 else None
