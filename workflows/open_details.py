import time
from controls import *

def execute(package: str, profile: dict, measure_startup: bool):
    actions = profile['actions']

    # Open app
    start_app(package=package, measure=measure_startup)
    time.sleep(5)

    for n in range(4):
        # Click nth flight
        do_action(actions[f'flight_{n}'])
        time.sleep(0.75)

        # Navigate back
        do_action(actions['details_back'])
        time.sleep(0.75)
