import time
from config.benchmark_config import BenchmarkConfig
from controls import *

def execute(config: BenchmarkConfig):
    actions = config.profile['actions']

    # Open app
    start_app(package=config.package, platform=config.platform, measure=config.measure_startup)
    time.sleep(5)

    # Scroll down (6x)
    for _ in range(6): 
        do_action(actions['scroll_down'])
        time.sleep(1)

    # Select random day
    do_action(actions['calendar'])
    time.sleep(0.5)
    do_action(actions['calendar_random_day'])
    time.sleep(0.5)
    do_action(actions['calendar_confirm'])
    time.sleep(0.5)

    # Scroll down (6x)
    for _ in range(6): 
        do_action(actions['scroll_down'])
        time.sleep(1)
