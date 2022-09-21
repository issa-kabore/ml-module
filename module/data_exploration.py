"""Exploratory Data Analysis(EDA)"""
import pandas as pd
from matplotlib import pyplot as plt
from pandas_profiling import ProfileReport
import seaborn as sns


# TODO:
#   - Create fct for num var and cat var


def get_numerical_features(dataframe: pd.DataFrame):
    """Return list of all the numeric columns"""
    numerical_features = dataframe.select_dtypes('number').columns.to_list()
    return numerical_features


def get_categorical_features(dataframe: pd.DataFrame):
    """Return list of all the categorical columns"""
    categorical_features = dataframe.select_dtypes(exclude=['number']).columns.to_list()
    return categorical_features


def convert_to_categorical(data: pd.DataFrame, columns_names: list):
    for var in columns_names:
        data[var] = data[var].astype('object')
    return data


# ---------------
# Graph functions
# ---------------
def data_visualization(df, report_title="your_report"):
    """Use on jupyter lab/notebook"""
    profile = ProfileReport(df, title=report_title)
    profile.to_file(report_title+".html")
    return profile


def plot_hist(data_var):
    plt.figure(figsize=(9, 8))
    sns.distplot(data_var, color='g', bins=100, hist_kws={'alpha': 0.4})
    plt.show()


def plot_heatmap(df: pd.DataFrame, pos_min: float = 0.5, neg_min: float = -0.4):
    """
    A function to plot correlation graph. Feature to feature relationship.
    :param df: a dataframe where num variables would be extracted
    :param pos_min: minimum value of correlation to display
    :param neg_min: min of negative correlation value to display
    """
    df_num = df.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(12, 10))
    corr = df_num.corr()
    sns.heatmap(corr[(corr >= pos_min) | (corr <= neg_min)],
                cmap='viridis', vmax=1.0, vmin=-1.0, linewidths=0.1,
                annot=True, annot_kws={"size": 8}, square=True)
    plt.show()


# Plotting cat features
def plot_relationship(data: pd.DataFrame, target: str, kind: str = "bar"):
    """Plotting boxplot: categorical relationship"""
    # check data[target] type: must be category
    if data[target].dtypes.name != "object":
        raise ValueError(f"Variable '{target}' is not 'categorical feature'.")
    categorical_features = get_categorical_features(data)
    features = [x for x in categorical_features if x != target]
    if kind not in ["bar", "boxplot"]:
        raise ValueError(f"Param 'kind :{kind}' must be one of ['bar', 'boxplot']")

    if kind == "bar":
        for feature in features:
            crostab = pd.crosstab(data[feature], data[target])
            crostab.div(crostab.sum(1).astype(float), axis=0).plot(kind="bar", stacked=True)
            plt.show()

    if kind == "boxplot":
        for feature in features:
            plt.figure(figsize=(9, 8))
            # plt.title('{} (box), subplot: {}{}{}'.format(i, a, b, c))
            sns.boxplot(x=feature, y=target, data=data)
            plt.show()
