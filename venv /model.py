import numpy as np

from repository import get_weights


def asset_prices_middle(portfolio, begin_date, end_date):
    return portfolio.loc[begin_date:end_date]


def portfolio_returns(asset_prices, weights):
    asset_returns = asset_prices.pct_change()
    return asset_returns.dot(weights)


def annualized_volatility(returns_windowed):
    return returns_windowed.std() * np.sqrt(252)
