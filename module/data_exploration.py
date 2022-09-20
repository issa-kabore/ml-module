"""Exploratory Data Analysis(EDA)"""
from matplotlib import pyplot as plt
from pandas_profiling import ProfileReport
import seaborn as sns


# TODO:
#   - Create fct for num var and cat var

def data_visualization(df, report_title="Report"):
    """Use on jupyter lab/notebook"""
    profile = ProfileReport(df, title=report_title)
    return profile


def plot_hist(data_var):
    plt.figure(figsize=(9, 8))
    sns.distplot(data_var, color='g', bins=100, hist_kws={'alpha': 0.4})
    plt.show()
