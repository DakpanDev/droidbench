import os

__PERCENTILE = 'percentile'

def __extract_ms(input: str) -> int:
    return input.split(': ')[1].replace('ms', '')

def measure_framerate(package: str):
    stream = os.popen(f'adb shell dumpsys gfxinfo {package} | grep {__PERCENTILE}')
    output = list(filter(lambda x: len(x) > 0, stream.read().split('\n')))
    [p_55, p_90, p_95, p_99, p_gpu_50, p_gpu_90, p_gpu_95, p_gpu_99] = map(__extract_ms, output)
    # TODO: Place in CSV
    print('To be implemented')
