# 19/08/2024 - Manon ROUSSE
# Define graph classes to handle the plotting

from matplotlib.axes import Axes
import matplotlib.pylab as plt
import pandas as pd
import numpy as np


class Distribution:
    title = ""
    values = []
    ax = None

    def __init__(self, title, ax):
        assert isinstance(title, str), "Try a title as str"
        self.title = title

        assert isinstance(ax, Axes), "Give an ax now"
        self.ax = ax

    def set_values_from_df(self, df, column):
        self.values = df[column].tolist()

    def plot_it(self, bins=list(range(15, 86, 5)), n_column=242):
        self.ax.set_title(self.title)
        self.ax.grid(True, alpha=0.5)
        percents = self.ax.hist(
            self.values,
            weights=100 / n_column * np.ones(len(self.values)),
            bins=bins,
            edgecolor="black",
        )
        plt.show()
        return percents


class Boxplot:
    title = ""
    labels_values = {}
    ax = None

    def __init__(self, title, ax):
        assert isinstance(title, str), "Try a title as str"
        self.title = title

        assert isinstance(ax, Axes), "Give an ax now"
        self.ax = ax

    def set_labels_values_from_df(self, df, column, match_label_val):
        multiple_count = 0
        if column in df.columns:
            # Create counters
            labels_values = {label: 0 for label in match_label_val.values()}

            for element in df[column]:
                if isinstance(element, str) and len(element) > 1:
                    sub_elements = [int(val) for val in element.split(" + ")]
                    for sub_element in sub_elements:
                        labels_values[match_label_val[sub_element]] += 1
                    multiple_count += len(sub_elements) - 1
                elif pd.notna(element):
                    labels_values[match_label_val[element]] += 1
                else:
                    labels_values[match_label_val[-1]] += 1

        # Make it percent
        total = df.shape[0]
        self.labels_values = {
            label: (value / total) * 100
            for label, value in labels_values.items()
            if label
        }
        print(multiple_count / df.shape[0])
        return

    def plot_it(self):
        labels = self.labels_values.keys()
        values = self.labels_values.values()

        self.ax.set_title(self.title)
        self.ax.grid(True, alpha=0.5)
        self.ax.bar(labels, values)
        self.ax.set_xticks(range(len(labels)), labels=labels, rotation=45, ha="right")


class XYplot:
    title = ""
    x_values = []
    y_values = []
    ax = None

    def __init__(self, title, ax):
        assert isinstance(title, str), "Try a title as str"
        self.title = title

        assert isinstance(ax, Axes), "Give an ax now"
        self.ax = ax

    def set_values_from_df(self, df, x_column, y_column):
        self.x_values = df[x_column]
        self.y_values = df[y_column]

    def plot_it(self, match_y_axis={}):
        self.ax.set_title(self.title)
        self.ax.grid(True, alpha=0.5)
        self.ax.scatter(self.x_values, self.y_values, linestyle="", marker="x")
        if match_y_axis:
            plt.yticks(list(match_y_axis.keys()), list(match_y_axis.values()))
