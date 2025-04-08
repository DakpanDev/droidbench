import os

__LAUNCH_STATE_KEY = 'LaunchState'
__LAUCN_STATE_COLD = 'COLD'
__TOTAL_TIME_KEY = 'TotalTime'

__measured_startup_time: dict = { 'value': None }

def __read_time_value(lines: list[str], key: str) -> str | None:
    for line in lines:
        splitted = line.split(': ')
        try:
            if splitted[0] == key:
                return splitted[1]
        except:
            print(f'Could not read value for {key} in line {line}')
            return None
        
def measure_startup_time(stream: os._wrap_close):
    output = stream.read().split('\n')
    launch_state = __read_time_value(lines=output, key=__LAUNCH_STATE_KEY)
    if launch_state == __LAUCN_STATE_COLD:
        total_time = __read_time_value(lines=output, key=__TOTAL_TIME_KEY)
        if total_time != None:
            __measured_startup_time['value'] = int(total_time)

def fetch_startup_time() -> int | None:
    return __measured_startup_time['value']
