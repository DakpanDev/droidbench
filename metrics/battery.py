import os

__CHARGE_COUNTER_KEY = '"Charge counter"'

def measure_battery():
    stream = os.popen(f'adb shell dumpsys battery | grep {__CHARGE_COUNTER_KEY}')
    splitted = stream.read().split(': ')
    if len(splitted) >= 2:
        charge = int(splitted[1])
        # TODO: Place into CSV
        print(f'Battery charge: {charge}mAh')
