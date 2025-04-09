import time
from config.benchmark_config import BenchmarkConfig
from controls import *

def execute(config: BenchmarkConfig):
    actions = config.profile['actions']

    # Open app
    start_app(package=config.package, platform=config.platform, measure=config.measure_startup)
    time.sleep(5)

    # Open bookmarks
    do_action(actions['bottombar_bookmarks'])
    time.sleep(2.5)
