from workflows.load_flights import execute as load_flights
from workflows.open_details import execute as open_details
from workflows.bookmark_flight import execute as bookmark_flight
from workflows.load_bookmarks import execute as load_bookmarks
from controls import *

class BenchmarkConfig:
    def __init__(self, package: str, n: int, profile: dict, load_flights: bool, 
                 open_details: bool, bookmark_flight: bool, load_bookmarks: bool):
        self.package = package
        self.n = n
        self.profile = profile
        self.load_flights = load_flights
        self.open_details = open_details
        self.bookmark_flight = bookmark_flight
        self.load_bookmarks = load_bookmarks

def __load_flights(config: BenchmarkConfig):
    for _ in range(config.n):
        load_flights(package=config.package, profile=config.profile)

def __open_details(config: BenchmarkConfig):
    for _ in range(config.n):
        open_details(package=config.package, profile=config.profile)

def __bookmark_flight(config: BenchmarkConfig):
    for _ in range(config.n):
        bookmark_flight(package=config.package, profile=config.profile)

def __load_bookmarks(config: BenchmarkConfig):
    for _ in range(config.n):
        load_bookmarks(package=config.package, profile=config.profile)

def run_benchmark(config: BenchmarkConfig):
    stop_app(config.package)
    if config.load_flights: __load_flights(config)
    if config.open_details: __open_details(config)
    if config.bookmark_flight: __bookmark_flight(config)
    if config.load_bookmarks: __load_bookmarks(config)
