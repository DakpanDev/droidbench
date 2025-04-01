import sys
import threading
from benchmark import run_benchmark
from measure_performance import measure_performance, stop_measuring
from utils import parse_parameters, create_config

def main(args: dict):
    config = create_config(args)
    measure_process = threading.Thread(target=measure_performance, args=(config.package,))
    bench_process = threading.Thread(target=run_benchmark, args=(config,))

    measure_process.start()
    bench_process.start()

    bench_process.join()
    stop_measuring()
    measure_process.join()

if __name__ == '__main__':
    args = parse_parameters(sys.argv)
    if args['d'] != None and args['p'] != None:
        main(args)
    else:
        print('Both device name and app package need to be provided')
