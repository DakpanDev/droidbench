import csv
import json
import matplotlib.pyplot as plt
import numpy as np
from save_results import TIME_OF_MEASURING_FIELDNAME, FRAMERATE_OVERALL_FIELDNAMES


def plot_against_time(path: str, filename: str, y_field: str, title: str):
    with open(f'{path}/{filename}', mode='r') as file:
        reader = csv.DictReader(file)
        time_axis = []
        y_axis = []
        for row in reader:
            time_axis.append(float(row[TIME_OF_MEASURING_FIELDNAME]))
            y_axis.append(float(row[y_field]))

        start = int(np.floor(min(time_axis)))
        end = int(np.ceil(max(time_axis)))
        step_size = int(end / 15)

        plt.plot(time_axis, y_axis, markersize=2)
        plt.xticks(np.arange(start, end + 1, step_size))
        plt.xlabel('Time (s)')
        plt.ylabel(y_field)
        plt.title(title)
        plt.grid(True)
        plt.show()

def plot_piechart(path: str, filename: str):
    with open(f'{path}/{filename}', mode='r') as file:
        data: dict = json.load(file)
        labels = list(data.keys())
        sizes = list(data.values())
        sizes_mb = [size/(1024*1024) for size in sizes]

        legend_labels = [f'{label}: {size:.2f}MB' for label, size in zip(labels, sizes_mb)]

        wedges, _, _ = plt.pie(
            sizes_mb,
            labels=labels,
            autopct='%1.1f%%',
        )
        plt.title('Occupied Storage')
        plt.legend(wedges, legend_labels, title='Legend', loc='lower left')
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

def plot_regular_boxplot(path: str, filename: str, fieldname: str):
    with open(f'{path}/{filename}', mode='r') as file:
        reader = csv.DictReader(file)
        values = [int(row[fieldname]) for row in reader]
        plt.boxplot(values, vert=True, patch_artist=True)
        plt.title(fieldname)
        plt.grid(True)
        plt.tight_layout()
        plt.show()

class Percentiles:
    def __init__(self, p50: float, p90: float, p95: float, p99: float, label: str):
        self.p50 = p50
        self.p90 = p90
        self.p95 = p95
        self.p99 = p99
        self.label = label

def plot_percentile_barchart(percentiles: list[Percentiles], title: str):
    index = np.arange(4)
    chart_count = len(percentiles)
    _, ax = plt.subplots()
    bar_width = chart_count / 2 / 2 / 2
    total_width = chart_count * bar_width
    min_offset = total_width / -2 + bar_width / 2
    for i, item in enumerate(percentiles):
        values = [item.p50, item.p90, item.p95, item.p99]
        offset = min_offset + i * bar_width
        ax.bar(index + offset, values, bar_width, label=item.label)
    ax.set_xticks(index)
    ax.set_xticklabels(fieldname.replace(' (ms)', '') for fieldname in FRAMERATE_OVERALL_FIELDNAMES)
    ax.set_title(title)
    ax.legend()
    plt.tight_layout()
    plt.show()
