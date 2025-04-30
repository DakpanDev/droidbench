import sys
from plotting.graphs import *
from save_results import *
from utils import parse_parameters

__REGULAR_PACKAGE = 'com.moveagency.myterminal'
__SHARED_PACKAGE = 'com.moveagency.shared.myterminal'
__REGULAR_VERSION = 'Regular Version'
__SHARED_VERSION = 'KMP Version'

class GraphingConfig:
    def __init__(self, cpu: bool, memory: bool, battery: bool, 
                 framerate: bool, startup: bool, app_size: bool):
        self.cpu = cpu
        self.memory = memory
        self.battery = battery
        self.framerate = framerate
        self.startup = startup
        self.app_size = app_size

def __read_line(path: str, filename: str, y_field: str, title: str) -> LinePlot | None:
    try:
        with open(f'{path}/{filename}', mode='r') as file:
            reader = csv.DictReader(file)
            time_axis = []
            y_axis = []
            for row in reader:
                time_axis.append(float(row[TIME_OF_MEASURING_FIELDNAME]))
                y_axis.append(float(row[y_field]))
            return LinePlot(
                x_axis=time_axis, 
                y_axis=y_axis,
                x_label=TIME_OF_MEASURING_FIELDNAME,
                y_label=y_field,
                title=title,
            )
    except:
        return None

def __plot_cpu():
    regular_path = create_path(__REGULAR_PACKAGE)
    shared_path = create_path(__SHARED_PACKAGE)
    regular_line = __read_line(regular_path, CPU_USAGE_FILENAME, CPU_USAGE_FIELDNAME, __REGULAR_VERSION)
    shared_line = __read_line(shared_path, CPU_USAGE_FILENAME, CPU_USAGE_FIELDNAME, __SHARED_VERSION)
    plots = list(filter(lambda x: x != None, [regular_line, shared_line]))
    plot_against_time(plots, 'CPU Usage over Time')

def __plot_memory():
    regular_path = create_path(__REGULAR_PACKAGE)
    shared_path = create_path(__SHARED_PACKAGE)
    regular_line = __read_line(regular_path, MEMORY_USAGE_FILENAME, MEMORY_USAGE_FIELDNAME, __REGULAR_VERSION)
    shared_line = __read_line(shared_path, MEMORY_USAGE_FILENAME, MEMORY_USAGE_FIELDNAME, __SHARED_VERSION)
    plots = list(filter(lambda x: x != None, [regular_line, shared_line]))
    plot_against_time(plots, 'Memory Usage over Time')

def __plot_battery():
    regular_path = create_path(__REGULAR_PACKAGE)
    shared_path = create_path(__SHARED_PACKAGE)
    regular_line = __read_line(regular_path, BATTERY_CHARGE_FILENAME, BATTERY_CHARGE_FIELDNAME, __REGULAR_VERSION)
    shared_line = __read_line(shared_path, BATTERY_CHARGE_FILENAME, BATTERY_CHARGE_FIELDNAME, __SHARED_VERSION)
    plots = list(filter(lambda x: x != None, [regular_line, shared_line]))
    plot_against_time(plots, 'Battery Charge over Time')

def __read_framerate(path: str, label: str) -> tuple[Percentiles, Percentiles | None] | None:
    try:
        with open(f'{path}/{FRAMERATE_FILENAME}', mode='r') as file:
            reader = csv.DictReader(file)
            p50, p90, p95, p99 = [], [], [], []
            p_gpu_50, p_gpu_90, p_gpu_95, p_gpu_99 = [], [], [], []
            for row in reader:
                p50.append(float(row[FIELD_OVERALL_P50_FIELDNAME]))
                p90.append(float(row[FIELD_OVERALL_P90_FIELDNAME]))
                p95.append(float(row[FIELD_OVERALL_P95_FIELDNAME]))
                p99.append(float(row[FIELD_OVERALL_P99_FIELDNAME]))
                try:
                    p_gpu_50.append(float(row[FIELD_GPU_P50_FIELDNAME]))
                    p_gpu_90.append(float(row[FIELD_GPU_P90_FIELDNAME]))
                    p_gpu_95.append(float(row[FIELD_GPU_P95_FIELDNAME]))
                    p_gpu_99.append(float(row[FIELD_GPU_P99_FIELDNAME]))
                except: pass
            overall_percentiles = Percentiles(
                p50=float(np.mean(p50, dtype=float)),
                p90=float(np.mean(p90, dtype=float)),
                p95=float(np.mean(p95, dtype=float)),
                p99=float(np.mean(p99, dtype=float)),
                label=label,
            )
            gpu_percentiles = Percentiles(
                p50=float(np.mean(p_gpu_50, dtype=float)),
                p90=float(np.mean(p_gpu_90, dtype=float)),
                p95=float(np.mean(p_gpu_95, dtype=float)),
                p99=float(np.mean(p_gpu_99, dtype=float)),
                label=label,
            ) if len(p_gpu_50) > 0 else None

            return (overall_percentiles, gpu_percentiles)
    except:
        return None

def __plot_framerate():
    regular_path = create_path(__REGULAR_PACKAGE)
    shared_path = create_path(__SHARED_PACKAGE)
    regular_overall_percentiles, regular_gpu_percentiles = __read_framerate(regular_path, __REGULAR_VERSION)
    shared_overall_percentiles, shared_gpu_percentiles = __read_framerate(shared_path, __SHARED_VERSION)
    plot_percentile_barchart([regular_overall_percentiles, shared_overall_percentiles], 'Overall Framerate (ms)')
    plot_percentile_barchart([regular_gpu_percentiles, shared_gpu_percentiles], 'GPU Framerate (ms)')

def __read_boxplot(path: str, filename: str, fieldname: str, title: str) -> list[int] | None:
    try:
        with open(f'{path}/{filename}', mode='r') as file:
            reader = csv.DictReader(file)
            return BoxPlot(
                values=[int(row[fieldname]) for row in reader],
                title=title,
            )
    except:
        return None

def __plot_startup():
    regular_path = create_path(__REGULAR_PACKAGE)
    shared_path = create_path(__SHARED_PACKAGE)
    regular_plot = __read_boxplot(regular_path, STARTUP_TIME_FILENAME, STARTUP_TIME_FIELDNAME, __REGULAR_VERSION)
    shared_plot = __read_boxplot(shared_path, STARTUP_TIME_FILENAME, STARTUP_TIME_FIELDNAME, __SHARED_VERSION)
    plots = list(filter(lambda x: x != None, [regular_plot, shared_plot]))
    plot_regular_boxplot(plots, STARTUP_TIME_FIELDNAME)

def __read_sizes_pie(path: str, filename: str, title: str) -> PieChart | None:
    try:
        with open(f'{path}/{filename}', mode='r') as file:
            data: dict = json.load(file)
            labels = list(data.keys())
            sizes = list(data.values())
            sizes_mb = [size/(1024*1024) for size in sizes]
            return PieChart(
                values=sizes_mb,
                labels=labels,
                title=title,
            )
    except:
        return None

def __plot_app_size():
    regular_path = create_path(__REGULAR_PACKAGE)
    shared_path = create_path(__SHARED_PACKAGE)
    regular_pie = __read_sizes_pie(regular_path, APP_SIZE_FILENAME, __REGULAR_VERSION)
    shared_pie = __read_sizes_pie(shared_path, APP_SIZE_FILENAME, __SHARED_VERSION)
    plots = list(filter(lambda x: x != None, [regular_pie, shared_pie]))
    plot_piechart(plots)

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
