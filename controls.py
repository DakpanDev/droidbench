import os
import time
from metrics.startup_time import measure_startup_time
from utils import PLATFORM_ANDROID, PLATFORM_IOS

def stop_app(platform: str, package: str):
    if platform == PLATFORM_ANDROID: os.popen(f'adb shell am force-stop {package}')
    if platform == PLATFORM_IOS: pass # TODO
    time.sleep(1)

def __start_app_android(package: str, measure: bool) -> os._wrap_close:
    return os.popen(f'adb shell am start{' -W' if measure else ''} -n {package}/.MainActivity')

def __start_app_ios(package: str,) -> float:
    start_time = time.time()
    # TODO
    end_time = time.time()
    return end_time - start_time

def start_app(package: str, platform: str, measure: bool=False):
    stream = None
    start_time = None
    if platform == PLATFORM_ANDROID: stream = __start_app_android(package, measure)
    if platform == PLATFORM_IOS: start_time = __start_app_ios(package)
    if measure: measure_startup_time(platform, stream, start_time)

def __tap(coords: dict, platform: str):
    if platform == PLATFORM_ANDROID: os.popen(f'adb shell input tap {coords['x']} {coords['y']}')
    if platform == PLATFORM_IOS: pass # TODO

def __swipe(coords: dict, platform: str):
    if platform == PLATFORM_ANDROID: 
        os.popen(f'adb shell input swipe {coords['x1']} {coords['y1']} {coords['x2']} {coords['y2']}')
    if platform == PLATFORM_IOS: 
        # TODO
        pass

def do_action(action: dict, platform: str):
    action_type = action['type']
    if action_type == None: return
    elif action_type == 'swipe': __swipe(action, platform)
    elif action_type == 'tap': __tap(action, platform)
