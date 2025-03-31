import sys
import time
import os
from utils import parse_parameters

def main(args: dict):
    os.system('adb shell am stop-app "com.moveagency.myterminal"')
    os.system('adb shell am start -n "com.moveagency.myterminal/com.moveagency.myterminal.MainActivity"')
    time.sleep(5)
    for _ in range(6):
        os.system('adb shell input swipe 550 2146 550 338')
        time.sleep(0.5)

if __name__ == '__main__':
    args = parse_parameters(sys.argv)
    main(args)
