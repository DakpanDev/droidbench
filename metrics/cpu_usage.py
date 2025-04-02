import os

__TOP_PACKAGE_LENGTH = 15
__CPU_INDEX = 8
__INCORRECT_LENGTH = 13

def measure_cpu_usage(package: str):
    cpu_package = package[:__TOP_PACKAGE_LENGTH] + '+'
    stream = os.popen(f'adb shell top -n 1 | grep {cpu_package}')
    res_values = stream.read().split(' ')
    res_values = list(filter(lambda x: len(x) > 0, res_values))
    if len(res_values) == __INCORRECT_LENGTH: 
        res_values = res_values[1:]

    if len(res_values) >= __CPU_INDEX + 1:
        # TODO: place into CSV
        print(f'CPU Usage (%): {res_values[__CPU_INDEX]}')
