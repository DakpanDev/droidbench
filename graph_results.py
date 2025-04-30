import sys
from plotting.graphs import *
from save_results import *
from utils import parse_parameters

__REGULAR_PACKAGE = 'com.moveagency.myterminal'
__SHARED_PACKAGE = 'com.moveagency.shared.myterminal'

class GraphingConfig:
    def __init__(self, cpu: bool, memory: bool, battery: bool, 
                 framerate: bool, startup: bool, app_size: bool):
        self.cpu = cpu
        self.memory = memory
        self.battery = battery
        self.framerate = framerate
        self.startup = startup
        self.app_size = app_size

def __plot_cpu():
    path = create_path(__REGULAR_PACKAGE)
    plot_against_time(path, CPU_USAGE_FILENAME, CPU_USAGE_FIELDNAME, 'CPU Usage over Time')

def __plot_memory():
    path = create_path(__REGULAR_PACKAGE)
    plot_against_time(path, MEMORY_USAGE_FILENAME, MEMORY_USAGE_FIELDNAME, 'Memory Usage over Time')

def __plot_battery():
    path = create_path(__REGULAR_PACKAGE)
    plot_against_time(path, BATTERY_CHARGE_FILENAME, BATTERY_CHARGE_FIELDNAME, 'Battery Charge over Time')

def __read_framerate(path: str, label: str) -> Percentiles | None:
    try:
        with open(f'{path}/{FRAMERATE_FILENAME}', mode='r') as file:
            reader = csv.DictReader(file)
            p50, p90, p95, p99 = [], [], [], []
            for row in reader:
                p50.append(float(row[FIELD_OVERALL_P50_FIELDNAME]))
                p90.append(float(row[FIELD_OVERALL_P90_FIELDNAME]))
                p95.append(float(row[FIELD_OVERALL_P95_FIELDNAME]))
                p99.append(float(row[FIELD_OVERALL_P99_FIELDNAME]))
            return Percentiles(
                p50=float(np.mean(p50, dtype=float)),
                p90=float(np.mean(p90, dtype=float)),
                p95=float(np.mean(p95, dtype=float)),
                p99=float(np.mean(p99, dtype=float)),
                label=label,
            )
    except:
        return None

def __plot_framerate():
    regular_path = create_path(__REGULAR_PACKAGE)
    shared_path = create_path(__SHARED_PACKAGE)
    regular_overall_percentiles = __read_framerate(regular_path, 'Regular Version')
    shared_overall_percentiles = __read_framerate(shared_path, 'KMP Version')
    plot_percentile_barchart([regular_overall_percentiles, shared_overall_percentiles], 'Overall Framerate (ms)')

def __plot_startup():
    path = create_path(__REGULAR_PACKAGE)
    plot_regular_boxplot(path, STARTUP_TIME_FILENAME, STARTUP_TIME_FIELDNAME)

def __plot_app_size():
    path = create_path(__REGULAR_PACKAGE)
    plot_piechart(path, APP_SIZE_FILENAME)

def main(config: GraphingConfig):
    if config.cpu: __plot_cpu()
    if config.memory: __plot_memory()
    if config.battery: __plot_battery()
    if config.framerate: __plot_framerate()
    if config.startup: __plot_startup()
    if config.app_size: __plot_app_size()

if __name__ == '__main__':
    args = parse_parameters(sys.argv)
    config = GraphingConfig(
        cpu=args['cpu'],
        memory=args['memory'],
        battery=args['battery'],
        framerate=args['framerate'],
        startup=args['startup'],
        app_size=args['app_size'],
    )
    main(config)
