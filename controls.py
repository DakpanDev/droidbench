import os

def stop_app(package: str):
    os.system(f'adb shell am force-stop {package}')

def start_app(package: str):
    os.system(f'adb shell am start -n "{package}/{package}.MainActivity"')

def tap(coords: dict):
    os.system(f'adb shell input tap {coords['x']} {coords['y']}')

def swipe(coords: dict):
    os.system(f'adb shell input swipe {coords['x1']} {coords['y1']} {coords['x2']} {coords['y2']}')

def do_action(action: dict):
    action_type = action['type']
    if action_type == None: return
    elif action_type == 'swipe': swipe(action)
    elif action_type == 'tap': tap(action)
