import time
from controls import *

def execute(package: str, profile: dict, measure_startup: bool):
    actions = profile['actions']

    # Open app
    start_app(package=package, measure=measure_startup)
    time.sleep(5)

    # Open bookmarks
    do_action(actions['bottombar_bookmarks'])
    time.sleep(2.5)

    stop_app(package)
