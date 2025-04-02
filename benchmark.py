from workflows.load_flights import execute as load_flights
from workflows.open_details import execute as open_details
from workflows.bookmark_flight import execute as bookmark_flight
from workflows.load_bookmarks import execute as load_bookmarks
from metrics.framerate import measure_framerate
from controls import *

class BenchmarkConfig:
    def __init__(self, package: str, n: int, profile: dict, load_flights: bool, 
                 open_details: bool, bookmark_flight: bool, load_bookmarks: bool, 
                 measure_startup: bool, measure_framerate: bool):
        self.package = package
        self.n = n
        self.profile = profile
        self.load_flights = load_flights
        self.open_details = open_details
        self.bookmark_flight = bookmark_flight
        self.load_bookmarks = load_bookmarks
        self.measure_startup = measure_startup
        self.measure_framerate = measure_framerate

def __load_flights(config: BenchmarkConfig):
    print('--------LOAD FLIGHTS--------')
    for iteration in range(config.n):
        print(f'Iteration {iteration}:')
        load_flights(package=config.package, profile=config.profile, measure_startup=config.measure_startup)
        if config.measure_framerate: measure_framerate(config.package)
        stop_app(config.package)
        print()

def __open_details(config: BenchmarkConfig):
    print('--------OPEN DETAILS--------')
    for iteration in range(config.n):
        print(f'Iteration {iteration}:')
        open_details(package=config.package, profile=config.profile, measure_startup=config.measure_startup)
        if config.measure_framerate: measure_framerate(config.package)
        stop_app(config.package)
        print()

def __bookmark_flight(config: BenchmarkConfig):
    print('--------BOOKMARK FLIGHT--------')
    for iteration in range(config.n):
        print(f'Iteration {iteration}:')
        bookmark_flight(package=config.package, profile=config.profile, measure_startup=config.measure_startup)
        if config.measure_framerate: measure_framerate(config.package)
        stop_app(config.package)
        print()

def __load_bookmarks(config: BenchmarkConfig):
    print('--------LOAD BOOKMARKS--------')
    for iteration in range(config.n):
        print(f'Iteration {iteration}:')
        load_bookmarks(package=config.package, profile=config.profile, measure_startup=config.measure_startup)
        if config.measure_framerate: measure_framerate(config.package)
        stop_app(config.package)
        print()

def run_benchmark(config: BenchmarkConfig):
    stop_app(config.package)
    if config.load_flights: __load_flights(config)
    if config.open_details: __open_details(config)
    if config.bookmark_flight: __bookmark_flight(config)
    if config.load_bookmarks: __load_bookmarks(config)
