import os
from utils import PLATFORM_ANDROID, PLATFORM_IOS

__TOP_PACKAGE_LENGTH = 15
__CPU_INDEX = 8
__INCORRECT_LENGTH = 13

def __measure_cpu_usage_android(package: str) -> float | None:
    cpu_package = package[:__TOP_PACKAGE_LENGTH] + '+'
    stream = os.popen(f'adb shell top -n 1 | grep {cpu_package}')
    res_values = stream.read().split(' ')
    res_values = list(filter(lambda x: len(x) > 0, res_values))
    if len(res_values) == __INCORRECT_LENGTH: 
        res_values = res_values[1:]

    return float(res_values[__CPU_INDEX]) if len(res_values) >= __CPU_INDEX + 1 else None

def __measure_cpu_usage_ios(package: str) -> float | None:
    # TODO
    pass

def measure_cpu_usage(platform: str, package: str) -> float | None:
    if platform == PLATFORM_ANDROID: return __measure_cpu_usage_android(package)
    if platform == PLATFORM_IOS: return __measure_cpu_usage_ios(package)
