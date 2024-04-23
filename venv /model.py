import numpy as np

from repository import get_weights


def asset_prices_middle(portfolio, begin_date, end_date):
    return portfolio.loc[begin_date:end_date]


def asset_returns(asset_prices):
    return asset_prices.pct_change()


def portfolio_returns(asset_prices, weights):
    returns = asset_returns(asset_prices)
    return returns.dot(weights)


def annualized_volatility(returns_windowed):
    return returns_windowed.std() * np.sqrt(252)
