import sys
from utils import parse_parameters

def main(args: dict):
    print(args)

if __name__ == '__main__':
    args = parse_parameters(sys.argv)
    main(args)
