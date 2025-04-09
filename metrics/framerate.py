import os
from utils import PLATFORM_ANDROID, PLATFORM_IOS

FIELD_OVERALL_P50 = 'p_50'
FIELD_OVERALL_P90 = 'p_90'
FIELD_OVERALL_P95 = 'p_95'
FIELD_OVERALL_P99 = 'p_99'

FIELD_GPU_P50 = 'p_gpu_50'
FIELD_GPU_P90 = 'p_gpu_90'
FIELD_GPU_P95 = 'p_gpu_95'
FIELD_GPU_P99 = 'p_gpu_99'

__PERCENTILE = 'percentile'

def __extract_ms(input: str) -> int:
    return int(input.split(': ')[1].replace('ms', ''))

def __measure_framerate_android(package: str) -> dict | None:
    stream = os.popen(f'adb shell dumpsys gfxinfo {package} | grep {__PERCENTILE}')
    output = filter(lambda x: len(x) > 0, stream.read().split('\n'))
    percentiles = list(map(__extract_ms, output))
    if len(percentiles) < 4: 
        print(f'No process found for: {package}')
        return None
    
    framerates = {
        FIELD_OVERALL_P50: percentiles[0],
        FIELD_OVERALL_P90: percentiles[1],
        FIELD_OVERALL_P95: percentiles[2],
        FIELD_OVERALL_P99: percentiles[3],
    }

    if len(percentiles) == 8:
        framerates[FIELD_GPU_P50] = percentiles[4]
        framerates[FIELD_GPU_P90] = percentiles[5]
        framerates[FIELD_GPU_P95] = percentiles[6]
        framerates[FIELD_GPU_P99] = percentiles[7]

    return framerates

def __measure_framerate_ios(package: str) -> dict | None:
    # TODO
    pass

def measure_framerate(platform: str, package: str) -> dict | None:
    if platform == PLATFORM_ANDROID: return __measure_framerate_android(package)
    if platform == PLATFORM_IOS: return __measure_framerate_ios(package)
