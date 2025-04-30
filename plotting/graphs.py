import csv
import json
import matplotlib.pyplot as plt
import numpy as np
from save_results import FRAMERATE_OVERALL_FIELDNAMES

class LinePlot:
    def __init__(self, x_axis: list, y_axis: list, x_label: str, y_label: str, title: str):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.x_label = x_label
        self.y_label = y_label
        self.title = title

def plot_against_time(plots: list[LinePlot], title: str):
    start = min([int(np.floor(min(plot.x_axis))) for plot in plots])
    end = max([int(np.ceil(max(plot.x_axis))) for plot in plots])
    step_size = int(end / 15)

    for plot in plots:
        plt.plot(plot.x_axis, plot.y_axis, markersize=2, label=plot.title)
    plt.xticks(np.arange(start, end + 1, step_size))
    plt.xlabel('Time (s)')
    plt.ylabel(plots[0].y_label)
    plt.title(title)
    plt.grid(True)
    plt.legend()
    plt.show()

class PieChart:
    def __init__(self, values: list, labels: str, title: str):
        self.values = values
        self.labels = labels
        self.title = title

def plot_piechart(pies: list[PieChart]):
    _, axes = plt.subplots(1, 2)
    for index, pie in enumerate(pies):
        wedges, _ = axes[index].pie(pie.values)
        axes[index].set_title(f'{pie.title}\n({sum(pie.values):.3F}MB)')
        legend_labels = [f'{label}: {size:.2f}MB' for label, size in zip(pie.labels, pie.values)]
        axes[index].legend(wedges, legend_labels, loc='lower left')
    plt.tight_layout()
    plt.show()

class BoxPlot:
    def __init__(self, values: list, title: str):
        self.values = values
        self.title = title

def plot_regular_boxplot(plots: list[BoxPlot], y_label: str):
    values = [plot.values for plot in plots]
    labels = [plot.title for plot in plots]
    plt.boxplot(values, vert=True, patch_artist=True, labels=labels)
    plt.title(y_label)
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
