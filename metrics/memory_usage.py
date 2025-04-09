import os
from utils import PLATFORM_ANDROID, PLATFORM_IOS

__PSS_INDEX = 2

def __measure_memory_usage_android(package: str) -> int | None:
    stream = os.popen(f'adb shell dumpsys meminfo {package} | grep "TOTAL PSS"')
    res_values = stream.read().split(' ')
    res_values = list(filter(lambda x: len(x) > 0, res_values))
    return int(res_values[__PSS_INDEX]) if len(res_values) > __PSS_INDEX + 1 else None

def __measure_memory_usage_ios(package: str) -> int | None:
    # TODO
    pass

def measure_memory_usage(platform: str, package: str) -> int | None:
    if platform == PLATFORM_ANDROID: return __measure_memory_usage_android(package)
    if platform == PLATFORM_IOS: return __measure_memory_usage_ios(package)
