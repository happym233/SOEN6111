import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def boxplot(data, column_name, label, title, xlabel, ylabel):
    fig, ax = plt.subplots()
    categories = data[label].unique()
    values = [data[data[categories] == c][column_name] for c in categories]
    ax.boxplot(values)
    ax.set_xticklabels(categories)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.show()

def plot_data_distribution(data, label, title, xlabel, ylabel):
    counts = data[label].value_counts()

    # create bar chart
    fig, ax = plt.subplots()
    ax.bar(counts.index, counts.values)
    ax.set_title(title)
    ax.set_xlabel(ylabel)
    ax.set_ylabel(xlabel)

def draft():
    data = {'feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            'feature2': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            'label': [0, 0, 1, 0, 0, 1, 1, 1, 0, 0]}

    # create pandas dataframe
    df = pd.DataFrame(data)

    # count number of data points in each class
    counts = df['label'].value_counts()

    # create duplicated data
    duplicated_data = []
    for label in counts.index:
        label_data = df[df['label'] == label]
        n_samples = max(counts) - len(label_data)
        if n_samples > 0:
            for i in range(n_samples):
                duplicated_data.append(label_data.iloc[i % len(label_data)])

    # create noisy data
    noisy_data = []
    for label in counts.index:
        label_data = df[df['label'] == label]
        n_samples = max(counts) - len(label_data)
        if n_samples > 0:
            for i in range(n_samples):
                noise = np.random.normal(0, 0.1, size=len(label_data.columns) - 1)
                noisy_point = label_data.iloc[i % len(label_data)].copy()
                noisy_point.drop('label', inplace=True)
                noisy_point += noise
                noisy_point['label'] = label
                noisy_data.append(noisy_point)

    # combine original data with duplicated and noisy data
    augmented_df = pd.concat([df] + duplicated_data + noisy_data, ignore_index=True)

    # shuffle data
    augmented_df = augmented_df.sample(frac=1)

