import time
from controls import *

def execute(package: str, profile: dict):
    actions = profile['actions']

    # Open app
    start_app(package)
    time.sleep(5)

    # Open bookmarks
    do_action(actions['bottombar_bookmarks'])
    time.sleep(2.5)

    stop_app(package)
