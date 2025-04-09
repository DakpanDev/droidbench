import os
from utils import PLATFORM_ANDROID, PLATFORM_IOS

__LAUNCH_STATE_KEY = 'LaunchState'
__LAUCN_STATE_COLD = 'COLD'
__TOTAL_TIME_KEY = 'TotalTime'

__measured_startup_time: dict = { 'value': None }

def __read_time_value(lines: list[str], key: str) -> str | None:
    for line in lines:
        splitted = line.split(': ')
        try:
            if splitted[0] == key:
                return splitted[1]
        except:
            print(f'Could not read value for {key} in line {line}')
            return None

def __measure_startup_time_android(stream: os._wrap_close) -> int | None:
    output = stream.read().split('\n')
    launch_state = __read_time_value(lines=output, key=__LAUNCH_STATE_KEY)
    if launch_state == __LAUCN_STATE_COLD:
        total_time = __read_time_value(lines=output, key=__TOTAL_TIME_KEY)
        return int(total_time) if total_time != None else None
    return None

def __measure_startup_time_ios(time: float) -> int:
    return time * 1000

def measure_startup_time(platform: str, stream: os._wrap_close, time: float | None):
    if platform == PLATFORM_ANDROID: 
        __measured_startup_time['value'] = __measure_startup_time_android(stream)
    if platform == PLATFORM_IOS and time != None:
        __measured_startup_time['value'] = __measure_startup_time_ios(time)

def fetch_startup_time() -> int | None:
    return __measured_startup_time['value']
