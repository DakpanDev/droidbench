from metrics.app_size import KEY_APP_SIZE, KEY_DATA_SIZE, KEY_CACHE_SIZE

def log_cpu_usage(cpu_usage: float | None):
    if cpu_usage != None: print(f'CPU Usage: {cpu_usage}%')

def log_memory_usage(memory_usage: int | None):
    if memory_usage != None: print(f'Memory Usage: {memory_usage}kB')

def log_battery_charge(battery_charge: int | None):
    if battery_charge != None: print(f'Battery Charge: {battery_charge}mAh')

def log_framerates(framerates: dict | None):
    if framerates != None: 
        output = ('Overall Framerates:' + 
                  f'\n\t50th Percentile: {framerates['p_50']}ms' + 
                  f'\n\t90th Percentile: {framerates['p_90']}ms' + 
                  f'\n\t95th Percentile: {framerates['p_95']}ms' + 
                  f'\n\t99th Percentile: {framerates['p_99']}ms')
        if len(framerates) == 8:
            output += ('\nGraphical Framerate:' + 
                  f'\n\t50th Percentile: {framerates['p_gpu_50']}ms' + 
                  f'\n\t90th Percentile: {framerates['p_gpu_90']}ms' + 
                  f'\n\t95th Percentile: {framerates['p_gpu_95']}ms' + 
                  f'\n\t99th Percentile: {framerates['p_gpu_99']}ms')
        print(output)

def log_startup_time(startup_time: int | None):
    if startup_time != None: print(f'Startup Time: {startup_time}ms')

def log_app_size(app_size: dict | None):
    if app_size != None:
        print(f'App Size: {app_size[KEY_APP_SIZE]} bytes' + 
              f'\nData Size: {app_size[KEY_DATA_SIZE]} bytes' + 
              f'\nCache Size: {app_size[KEY_CACHE_SIZE]} bytes')
