from config.benchmark_config import BenchmarkConfig
from workflows.load_flights import execute as load_flights
from workflows.open_details import execute as open_details
from workflows.bookmark_flight import execute as bookmark_flight
from workflows.load_bookmarks import execute as load_bookmarks
from controls import *
from measure_performance import complete_measuring, start_measuring, trigger_framerate_measure, trigger_startup_measure

def __load_flights(config: BenchmarkConfig):
    print('--------LOAD FLIGHTS--------')
    for iteration in range(config.n):
        print(f'Iteration {iteration}:')
        start_measuring()
        load_flights(config)
        if config.measure_framerate: trigger_framerate_measure()
        if config.measure_startup: trigger_startup_measure()
        complete_measuring()
        time.sleep(1)
        stop_app(config.platform, config.package)
        print()

def __open_details(config: BenchmarkConfig):
    print('--------OPEN DETAILS--------')
    for iteration in range(config.n):
        print(f'Iteration {iteration}:')
        start_measuring()
        open_details(config)
        if config.measure_framerate: trigger_framerate_measure()
        if config.measure_startup: trigger_startup_measure()
        complete_measuring()
        time.sleep(1)
        stop_app(config.platform, config.package)
        print()

def __bookmark_flight(config: BenchmarkConfig):
    print('--------BOOKMARK FLIGHT--------')
    for iteration in range(config.n):
        print(f'Iteration {iteration}:')
        start_measuring()
        bookmark_flight(config)
        if config.measure_framerate: trigger_framerate_measure()
        if config.measure_startup: trigger_startup_measure()
        complete_measuring()
        time.sleep(1)
        stop_app(config.platform, config.package)
        print()

def __load_bookmarks(config: BenchmarkConfig):
    print('--------LOAD BOOKMARKS--------')
    for iteration in range(config.n):
        print(f'Iteration {iteration}:')
        start_measuring()
        load_bookmarks(config)
        if config.measure_framerate: trigger_framerate_measure()
        if config.measure_startup: trigger_startup_measure()
        complete_measuring()
        time.sleep(1)
        stop_app(config.platform, config.package)
        print()

def run_benchmark(config: BenchmarkConfig):
    stop_app(config.platform, config.package)
    if config.load_flights: __load_flights(config)
    if config.open_details: __open_details(config)
    if config.bookmark_flight: __bookmark_flight(config)
    if config.load_bookmarks: __load_bookmarks(config)
