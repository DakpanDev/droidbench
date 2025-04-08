import os

__PERCENTILE = 'percentile'

def __extract_ms(input: str) -> int:
    return int(input.split(': ')[1].replace('ms', ''))

def __calculate_framerate(milliseconds: int) -> float:
    return 1000 / milliseconds

def measure_framerate(package: str) -> list[float | None]:
    stream = os.popen(f'adb shell dumpsys gfxinfo {package} | grep {__PERCENTILE}')
    output = filter(lambda x: len(x) > 0, stream.read().split('\n'))
    milliseconds = map(__extract_ms, output)
    framerates = list(map(__calculate_framerate, milliseconds))
    if len(framerates) < 8: 
        print(f'No process found for: {package}')
        return None
    return framerates
