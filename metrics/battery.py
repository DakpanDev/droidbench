import os
from utils import PLATFORM_ANDROID, PLATFORM_IOS

__CHARGE_COUNTER_KEY = '"Charge counter"'

def __measure_battery_android() -> int | None:
    stream = os.popen(f'adb shell dumpsys battery | grep {__CHARGE_COUNTER_KEY}')
    splitted = stream.read().split(': ')
    return int(splitted[1]) if len(splitted) >= 2 else None

def __measure_battery_ios() -> int | None:
    # TODO
    pass

def measure_battery(platform: str) -> int | None:
    if platform == PLATFORM_ANDROID: return __measure_battery_android()
    if platform == PLATFORM_IOS: return __measure_battery_ios()
