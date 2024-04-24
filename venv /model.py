import numpy as np

from repository import get_weights


def asset_prices_middle(portfolio, begin_date, end_date):
    return portfolio.loc[begin_date:end_date]


def asset_returns(asset_prices):
    return asset_prices.pct_change()


def portfolio_returns(asset_prices, weights):
    return asset_prices.pct_change().dot(weights)


def ann_volatility(port_returns):
    returns_windowed = port_returns.rolling(30)
    annualized_volatility = returns_windowed.std() * np.sqrt(252)
    return annualized_volatility


def ann_cov(asset_ret):
    return asset_ret.cov() * 252


def port_variance(covariance, weights):
    portfolio_variance = np.transpose(weights) @ covariance @ weights
    portfolio_volatility = np.sqrt(portfolio_variance)
    return portfolio_volatility
