# This is a sample Python script.
from module import LOGGER
from module.data_exploration import *
import module.preprocessing as pr

import pandas as pd
pd.set_option("display.max.columns", None)
# pd.set_option("display.precision", 2)
import os

path = os.getcwd()
os.chdir(path)

# --------------------------------------
path_data = "data/"
filename = "bike-rentals.csv"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    LOGGER.info('Importing data')
    df = pd.read_csv(path_data + filename)
    target = "rentals"
    var = "season"

    LOGGER.info('Exploring dataset')
    data = df.copy()
    data = convert_to_categorical(data, columns_names=['season', 'workingday', 'weathersit', 'holiday'])

    # plot_hist(df[var])
    # plot_heatmap(df)
    # profile = data_visualization(df)
    # print(profile)
    # profile.to_file("your_report.html")
    # plot_boxplot(data, target=target, var=var)
    plot_relationship(data, target=var, kind="bar")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
