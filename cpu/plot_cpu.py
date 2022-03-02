from os import makedirs
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def stack_dataframe(df):
    df = df[[f"node{i}" for i in range(4, 20)]]
    print(df)
    col_list = [x for x in range(5, 20)]
    for i, _ in df.iterrows():
        for col in col_list:
            df.loc[i, f"node{col}"] = df.loc[i, f"node{col}"] + df.loc[i, f"node{col - 1}"]
    return df


if __name__ == "__main__":
    fig, axs = plt.subplots(1, 2, figsize=(18, 7.5), gridspec_kw={'hspace': 0.1, 'wspace': 0.1}, sharey=True)
    sns.despine(top=True, right=True)
    sns.set_palette('Set2', n_colors=2)
    
    # with skyhook
    # client
    df_skyhook_client = pd.read_csv('skyhook-client.csv')
    rows = len(df_skyhook_client)

    timestamp = list()
    for i in range(rows):
        timestamp.append(i * 15)

    df_skyhook_client['Time'] = timestamp
    sns_plot = sns.lineplot(data=df_skyhook_client, x="Time", y="Usage", ax=axs[1], linewidth=5, linestyle='-.')
    sns_plot.set(ylim=(0, 100))
    sns_plot.set(xlim=(0, 400))

    sns_plot.set_title("With Skyhook", fontdict= { 'fontsize': 26})
    sns_plot.set_ylabel('CPU Usage (%)', fontsize=24)
    sns_plot.set_xlabel('Timestamp (s)', fontsize=24)
    sns_plot.tick_params(axis="y", labelsize=24)
    sns_plot.tick_params(axis="x", labelsize=22)

    df_wskyhook_client = pd.read_csv('without-skyhook-client.csv')
    rows = len(df_wskyhook_client)

    # server
    df_skyhook_storage = pd.read_csv('skyhook-storage.csv')
    df_skyhook_storage = stack_dataframe(df_skyhook_storage)

    for i in range(4, 19):
        rows = len(df_skyhook_storage)

        timestamp = list()
        for j in range(rows):
            timestamp.append(j * 15)

        df_skyhook_storage['Time'] = timestamp
        sns_plot = sns.lineplot(data=df_skyhook_storage, x="Time", y="node{}".format(i), linewidth=2, ax=axs[1], linestyle='--')
        sns_plot.set(ylim=(0, 160))
        sns_plot.set(xlim=(0, 400))

        sns_plot.set_title("With Skyhook", fontdict= { 'fontsize': 26})
        sns_plot.set_ylabel('CPU Usage (%)', fontsize=24)
        sns_plot.set_xlabel('Timestamp (s)', fontsize=24)
        sns_plot.tick_params(axis="y", labelsize=24)
        sns_plot.tick_params(axis="x", labelsize=22)
    
    sns_plot.grid(axis='y')
    # without skyhook
    # client
    df_wskyhook_client = pd.read_csv('without-skyhook-client.csv')
    rows = len(df_wskyhook_client)

    timestamp = list()
    for i in range(rows):
        timestamp.append(i * 15)
    
    df_wskyhook_client['Time'] = timestamp

    sns_plot = sns.lineplot(data=df_wskyhook_client, x="Time", y="Usage", ax=axs[0], linewidth=5, linestyle='-.')
    sns_plot.set(ylim=(0, 100))
    sns_plot.set(xlim=(0, 400))

    sns_plot.set_title("Without Skyhook", fontdict= { 'fontsize': 26})
    sns_plot.set_ylabel('CPU Usage (%)', fontsize=24)
    sns_plot.set_xlabel('Timestamp (s)', fontsize=24)
    sns_plot.tick_params(axis="y", labelsize=24)
    sns_plot.tick_params(axis="x", labelsize=22)

    # server
    df_wskyhook_storage = pd.read_csv('without-skyhook-storage.csv')
    df_wskyhook_storage = stack_dataframe(df_wskyhook_storage)
    
    for i in range(4, 19):
        rows = len(df_wskyhook_storage)

        timestamp = list()
        for j in range(rows):
            timestamp.append(j * 15)

        df_wskyhook_storage['Time'] = timestamp
        sns_plot = sns.lineplot(data=df_wskyhook_storage, x="Time", y="node{}".format(i), linewidth=2, ax=axs[0], linestyle='--')
        sns_plot.set(ylim=(0, 160))
        sns_plot.set(xlim=(0, 400))

        sns_plot.set_title("Without Skyhook", fontdict= { 'fontsize': 26})
        sns_plot.set_ylabel('CPU Usage (%)', fontsize=24)
        sns_plot.set_xlabel('Timestamp (s)', fontsize=24)
        sns_plot.tick_params(axis="y", labelsize=24)
        sns_plot.tick_params(axis="x", labelsize=22)

    sns_plot.grid(axis='y')
    fig.savefig('cpu.pdf', bbox_inches='tight')
