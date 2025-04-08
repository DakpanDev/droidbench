import os

__CHARGE_COUNTER_KEY = '"Charge counter"'

def measure_battery() -> int | None:
    stream = os.popen(f'adb shell dumpsys battery | grep {__CHARGE_COUNTER_KEY}')
    splitted = stream.read().split(': ')
    return int(splitted[1]) if len(splitted) >= 2 else None
