import os

__PERCENTILE = 'percentile'

def __extract_ms(input: str) -> int:
    return int(input.split(': ')[1].replace('ms', ''))

def __calculate_framerate(milliseconds: int) -> float:
    return 1000 / milliseconds

def measure_framerate(package: str):
    stream = os.popen(f'adb shell dumpsys gfxinfo {package} | grep {__PERCENTILE}')
    output = filter(lambda x: len(x) > 0, stream.read().split('\n'))
    milliseconds = map(__extract_ms, output)
    [p_50, p_90, p_95, p_99, p_gpu_50, p_gpu_90, p_gpu_95, p_gpu_99] = map(__calculate_framerate, milliseconds)
    # TODO: Place in CSV
    print('Overall framerate')
    print(f'50th percentile: {p_50} FPS')
    print(f'90th percentile: {p_90} FPS')
    print(f'95th percentile: {p_95} FPS')
    print(f'99th percentile: {p_99} FPS')
    print('\nGraphical framerate')
    print(f'50th percentile: {p_gpu_50} FPS')
    print(f'90th percentile: {p_gpu_90} FPS')
    print(f'95th percentile: {p_gpu_95} FPS')
    print(f'99th percentile: {p_gpu_99} FPS')
