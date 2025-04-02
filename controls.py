import os
import time
from metrics.startup_time import measure_startup_time

def stop_app(package: str):
    os.popen(f'adb shell am force-stop {package}')
    time.sleep(1)

def start_app(package: str, measure: bool=False):
    stream = os.popen(f'adb shell am start{' -W' if measure else ''} -n {package}/.MainActivity')
    if measure:
        measure_startup_time(stream)

def tap(coords: dict):
    os.popen(f'adb shell input tap {coords['x']} {coords['y']}')

def swipe(coords: dict):
    os.popen(f'adb shell input swipe {coords['x1']} {coords['y1']} {coords['x2']} {coords['y2']}')

def do_action(action: dict):
    action_type = action['type']
    if action_type == None: return
    elif action_type == 'swipe': swipe(action)
    elif action_type == 'tap': tap(action)
