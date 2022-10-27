# Your code to create majestic plots goes in here!
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():
    # create data frame of our data
    iris_df = pd.read_csv('iris.data', sep=',', header=None)

    iris_df.columns = ['sepal_width', 'sepal_length', 'petal_width',
                       'petal_length', 'species']

    # create boxplot
    plt.boxplot([iris_df['sepal_length'], iris_df["sepal_width"],
                 iris_df["petal_length"], iris_df["petal_width"]],
                labels=['sepal length', 'sepal width',
                        'petal_length', 'petal_width'])

    plt.ylabel("cm", fontsize=14)

    plt.savefig('iris_boxplot.png')

    # create scatter plot
    plt.figure(figsize=(10, 8))
    handles = []
    colors = ['mediumorchid', 'mediumspringgreen', 'gold']
    i = 0
    for species in iris_df['species'].unique():

        handles.append(species)
        df = iris_df[iris_df['species'] == species]
        plt.scatter(df['petal_width'], df['petal_length'], color=colors[i])
        i += 1

    plt.xlabel('Petal Width (cm)', fontsize=14)
    plt.ylabel('Petal Length (cm)', fontsize=14)
    plt.legend(handles)
    plt.title("Petal Width vs. Petal Length", fontsize=18)
    plt.savefig('petal_width_v_length_scatter.png')

    # multi-panel plot
    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches((12, 6))

    axes[0].boxplot([iris_df['sepal_length'], iris_df["sepal_width"],
                     iris_df["petal_length"], iris_df["petal_width"]],
                    labels=['sepal length', 'sepal width',
                            'petal_length', 'petal_width'])
    axes[0].set_ylabel("cm", fontsize=14)
    axes[0].spines.right.set_visible(False)
    axes[0].spines.top.set_visible(False)

    i = 0
    for species in iris_df['species'].unique():

        handles.append(species)
        df = iris_df[iris_df['species'] == species]
        axes[1].scatter(df['petal_length'], df['petal_width'],
                        color=colors[i], s=20)
        i += 1

    axes[1].set_xlabel('Petal Length (cm)', fontsize=14)
    axes[1].set_ylabel('Petal Width (cm)', fontsize=14)
    axes[1].legend(handles)
    axes[1].spines.right.set_visible(False)
    axes[1].spines.top.set_visible(False)

    plt.savefig('multi_panel_figure.png')


if __name__ == '__main__':
    main()
