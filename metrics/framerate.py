import os

__PERCENTILE = 'percentile'

def __extract_ms(input: str) -> int:
    return int(input.split(': ')[1].replace('ms', ''))

def __calculate_framerate(milliseconds: int) -> float:
    return 1000 / milliseconds

def measure_framerate(package: str) -> dict | None:
    stream = os.popen(f'adb shell dumpsys gfxinfo {package} | grep {__PERCENTILE}')
    output = filter(lambda x: len(x) > 0, stream.read().split('\n'))
    milliseconds = map(__extract_ms, output)
    percentiles = list(map(__calculate_framerate, milliseconds))
    if len(percentiles) < 4: 
        print(f'No process found for: {package}')
        return None
    
    framerates = {
        'p_50': percentiles[0],
        'p_90': percentiles[1],
        'p_95': percentiles[2],
        'p_99': percentiles[3],
    }

    if len(percentiles) == 8:
        framerates['p_gpu_50'] = percentiles[4]
        framerates['p_gpu_90'] = percentiles[5]
        framerates['p_gpu_95'] = percentiles[6]
        framerates['p_gpu_99'] = percentiles[7]

    return framerates
