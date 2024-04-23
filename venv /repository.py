import pandas as pd


def get_portfolio():
    return pd.read_csv(
        r"input/crisis_portfolio.csv",
        delimiter=",",
        index_col="Date",
        parse_dates=["Date"],
    )


def get_begin_date():
    return "2008-01-01"


def get_end_date():
    return "2009-12-31"


def get_weights():
    return [0.25, 0.25, 0.25, 0.25]
