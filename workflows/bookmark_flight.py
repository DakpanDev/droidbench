import time
from controls import *

def execute(package: str, profile: dict, measure_startup: bool):
    actions = profile['actions']

    # Open app
    start_app(package=package, measure=measure_startup)
    time.sleep(5)

    # Click first flight
    do_action(actions['flight_0'])
    time.sleep(0.75)

    for _ in range(10):
        do_action(actions['details_bookmark'])
        time.sleep(0.1)

    stop_app(package)
