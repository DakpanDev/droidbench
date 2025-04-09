import time
from config.benchmark_config import BenchmarkConfig
from controls import *

def execute(config: BenchmarkConfig):
    actions = config.profile['actions']

    # Open app
    start_app(package=config.package, platform=config.platform, measure=config.measure_startup)
    time.sleep(5)

    for n in range(4):
        # Click nth flight
        do_action(actions[f'flight_{n}'])
        time.sleep(0.75)

        # Navigate back
        do_action(actions['details_back'])
        time.sleep(0.75)
