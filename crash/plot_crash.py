from datetime import time
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


if __name__ == "__main__":
    # sns.set_style('whitegrid')
    ax = plt.figure(figsize=(15, 12), dpi=80)
    sns.set_palette('Set2', n_colors=1)
    df = pd.read_csv('crash.csv')
    rows = len(df)

    timestamp = list()
    for i in range(rows):
        timestamp.append(i * 15)

    th = list()
    for val in df["Throughput"]:
        th.append(val / (1024*1024))

    df['Time'] = timestamp
    df['Throughput'] = th
    sns_plot = sns.lineplot(data=df, x="Time", y="Throughput", color='black', linewidth=3)
    sns_plot.set(ylim=(0, 1050))
    sns_plot.set_ylabel('Throughput (MBps)', fontsize=32)
    sns_plot.set_xlabel('Timestamp (s)', fontsize=32)
    sns_plot.tick_params(axis="y", labelsize=32)
    sns_plot.tick_params(axis="x", labelsize=32)
    sns_plot.grid(axis='y')
    plt.savefig('crash.pdf', bbox_inches='tight')
