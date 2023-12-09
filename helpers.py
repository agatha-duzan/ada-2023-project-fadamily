import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def restrict_time_period(df, start_date='2010', end_date='2019-09-29'):
    return df[(df.index >= pd.to_datetime(start_date)) & (df.index < pd.to_datetime(end_date))]

def get_linear_fit(series: pd.Series) -> np.ndarray:
    x = np.arange(len(series))
    y = series.values.tolist()
    coefficients = np.polyfit(x, y, 1)
    linear_fit = np.poly1d(coefficients)
    x_fit = np.linspace(x.min(), x.max(), len(series))
    y_fit = linear_fit(x_fit)
    return y_fit

def plot_evolution(category, nb_videos_cat_df, climate_videos_df):
    df = nb_videos_cat_df[nb_videos_cat_df['category']==category].copy()
    df.drop('category', axis=1, inplace=True)
    df['nb_videos_cc'] = pd.Series(climate_videos_df[climate_videos_df['category']==category].index.value_counts())
    df['nb_videos_cc'].fillna(0, inplace=True)

    # monthly averages
    percentage = 100* df['nb_videos_cc'].resample('M').sum() / df['nb_videos'].resample('M').sum()

    # plot
    fig, ax = plt.subplots(figsize=(20, 5))
    ax.plot(percentage.index, percentage.values, label='Proportion of climate change videos')
    ax.plot(percentage.index, get_linear_fit(percentage), label='Linear regression')
    ax.set_title(f'Evolution of the proportion of climate change videos in the category {category} (monthly)')
    ax.set_ylabel('Percentage of videos that are about climate change (%)')
    plt.legend()
    plt.show()

