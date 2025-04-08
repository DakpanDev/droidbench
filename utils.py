import json
from benchmark import BenchmarkConfig
from measure_performance import MeasureConfig

__arguments = {
    'd': None,                  # Device name
    'p': None,                  # Package
    'n': '1',                   # Iteration amount
    'load_flights': False,      # Do load_flights benchmark
    'open_details': False,      # Do open_details benchmark
    'bookmark_flight': False,   # Do bookmark_flight benchmark
    'load_bookmarks': False,    # Do load_bookmarks benchmark
    'all': False,               # Do all benchmarks
    'cpu': False,               # Measure CPU usage
    'memory': False,            # Measure memory usage
    'battery': False,           # Measure battery drain
    'framerate': False,         # Measure framerate
    'startup': False,           # Measure startup time
    'app_size': False,          # Measure app size
}

def parse_parameters(args: list[str]) -> dict:
    parsed = __arguments
    for index, arg in enumerate(args):
        if arg[0] != '-':
            continue
        if arg[1] == '-':
            parsed[arg[2:]] = True
            continue
        parsed[arg[1:]] = args[index+1]
    return parsed

def get_profile(profiles: list, name: str) -> dict:
    for profile in profiles:
        if profile['name'] == name:
            return profile

def create_benchmark_config(args: dict) -> BenchmarkConfig:
    with open('profiles.json', 'r') as file:
        profiles = json.load(file)['profiles']
        profile = get_profile(profiles, args['d'])

    return BenchmarkConfig(
        package=args['p'], 
        n=int(args['n']),
        profile=profile,
        load_flights=args['load_flights'] or args['all'],
        open_details=args['open_details'] or args['all'],
        bookmark_flight=args['bookmark_flight'] or args['all'],
        load_bookmarks=args['load_bookmarks'] or args['all'],
        measure_startup=args['startup'],
        measure_framerate=args['framerate'],
    )

def create_measure_config(args: dict) -> MeasureConfig:
    return MeasureConfig(
        package=args['p'],
        measure_cpu=args['cpu'],
        measure_memory=args['memory'],
        measure_battery=args['battery'],
        measure_app_size=args['app_size'],
    )
