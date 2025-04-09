import time
from config.benchmark_config import BenchmarkConfig
from controls import *

def execute(config: BenchmarkConfig):
    actions = config.profile['actions']

    # Open app
    start_app(package=config.package, platform=config.platform, measure=config.measure_startup)
    time.sleep(5)

    # Click first flight
    do_action(actions['flight_0'], platform=config.platform)
    time.sleep(0.75)

    for _ in range(10):
        do_action(actions['details_bookmark'], platform=config.platform)
        time.sleep(0.1)
