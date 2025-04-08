import os

__OUTPUT_PACKAGE_NAMES = '"Package Names"'
__OUTPUT_APP_SIZES = '"App Sizes"'
__OUTPUT_DATA_SIZES = '"App Data Sizes"'
__OUTPUT_CACHE_SIZES = '"Cache Sizes"'

KEY_APP_SIZE = 'app_size'
KEY_DATA_SIZE = 'data_size'
KEY_CACHE_SIZE = 'cache_size'

def __diskstats_to_dict(stats: str, package: str) -> dict | None:
    lists_as_strings = [x.split(': ')[1] for x in stats]
    actual_lists = [x.replace('[', '').replace(']', '').split(',') for x in lists_as_strings]
    if len(actual_lists) == 4:
        package_index = actual_lists[0].index(f'"{package}"')
        return {
            KEY_APP_SIZE: int(actual_lists[1][package_index]),
            KEY_DATA_SIZE: int(actual_lists[2][package_index]),
            KEY_CACHE_SIZE: int(actual_lists[3][package_index]),
        }
    else:
        return None

def measure_app_size(package: str) -> dict:
    stream = os.popen(f'adb shell dumpsys diskstats | grep -e {__OUTPUT_PACKAGE_NAMES} ' +
                      f'-e {__OUTPUT_APP_SIZES} -e {__OUTPUT_DATA_SIZES} -e {__OUTPUT_CACHE_SIZES}')
    output = stream.read().splitlines()
    return __diskstats_to_dict(stats=output, package=package)
