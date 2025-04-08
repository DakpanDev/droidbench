import sys
import threading
from benchmark import run_benchmark
from measure_performance import measure_performance, finish, complete_measuring
from utils import parse_parameters, create_benchmark_config, create_measure_config

def main(args: dict):
    benchmark_config = create_benchmark_config(args)
    measure_config = create_measure_config(args)
    bench_process = threading.Thread(target=run_benchmark, args=(benchmark_config,))
    measure_process = threading.Thread(target=measure_performance, args=(measure_config,))

    complete_measuring()
    measure_process.start()
    bench_process.start()

    bench_process.join()
    finish()
    measure_process.join()

if __name__ == '__main__':
    args = parse_parameters(sys.argv)
    if args['d'] != None and args['p'] != None:
        main(args)
    else:
        print('Both device name and app package need to be provided')
