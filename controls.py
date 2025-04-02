import os

__STARTUP_TIME_INDEX = 1

def stop_app(package: str):
    os.popen(f'adb shell am force-stop {package}')

def start_app(package: str, measure: bool=False):
    stream = os.popen(f'adb shell am start {'-W' if measure else ''} -n' +
                      f'{package}/.MainActivity {'| grep TotalTime' if measure else ''}')
    if measure:
        output = stream.read().split(': ')
        if len(output) >= __STARTUP_TIME_INDEX + 1:
            startup_time = output[1].replace('\n', '')
            # TODO: place into CSV
            print(f'Startup Time: {startup_time}ms')

def tap(coords: dict):
    os.popen(f'adb shell input tap {coords['x']} {coords['y']}')

def swipe(coords: dict):
    os.popen(f'adb shell input swipe {coords['x1']} {coords['y1']} {coords['x2']} {coords['y2']}')

def do_action(action: dict):
    action_type = action['type']
    if action_type == None: return
    elif action_type == 'swipe': swipe(action)
    elif action_type == 'tap': tap(action)
