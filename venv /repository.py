import pandas as pd
import numpy as np


def get_data():
    return pd.read_csv(
        r"../input/crisis_portfolio.csv",
        delimiter=",",
        index_col="Date",
        parse_dates=["Date"],
    )


def get_weight():
    return np.array([0.25, 0.25, 0.25, 0.25])
