import sys
from benchmark import run_benchmark
from utils import parse_parameters, create_config

def main(args: dict):
    config = create_config(args)
    run_benchmark(config)

if __name__ == '__main__':
    args = parse_parameters(sys.argv)
    if args['d'] != None and args['p'] != None:
        main(args)
    else:
        print('Both device name and app package need to be provided')
