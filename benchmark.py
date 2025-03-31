from benchmarks.load_flights import execute as load_flights
from benchmarks.open_details import execute as open_details
from benchmarks.bookmark_flight import execute as bookmark_flight
from benchmarks.load_bookmarks import execute as load_bookmarks
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

def __open_details(n: int):
    open_details()

def __bookmark_flight(n: int):
    bookmark_flight()

def __load_bookmarks(n: int):
    load_bookmarks()

def run_benchmark(config: BenchmarkConfig):
    if config.load_flights: __load_flights(config)
    if config.open_details: __open_details(n=config.n)
    if config.bookmark_flight: __bookmark_flight(n=config.n)
    if config.load_bookmarks: __load_bookmarks(n=config.n)
