import matplotlib as plt
import pandas as pd


def read_events(data: pd.DataFrame, file_path: str = 'data/climate_events.csv') -> pd.DataFrame:
    df = pd.read_csv(file_path, index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df = df.loc[data.index[0]:data.index[-1]]
    return df


def plot_events(ax, df: pd.DataFrame):
    # PLot red vertical lines for each event
    for date in df.index:
        ax.axvline(x=date, alpha=0.5)


def read_and_plot_events(data: pd.DataFrame, ax, file_path: str = 'data/climate_events_v2.csv'):
    df = read_events(data, file_path)
    plot_events(ax, df)



if __name__ == '__main__':
    df = read_events('../../data/climate_events.csv')
    print(df.head())
