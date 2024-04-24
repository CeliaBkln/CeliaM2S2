import numpy as np


def asset_prices_middle(portfolio, begin_date, end_date):
    """
    Select portfolio asset prices for a specified time period.
    :param portfolio: DataFrame containing asset prices with dates as index
    :param begin_date: Start date of the time period (e.g., "2008-01-01")
    :param end_date: End date of the time period (e.g., "2009-12-31")
    :return: DataFrame containing asset prices for the specified time period
    """
    return portfolio.loc[begin_date:end_date]


def asset_returns(asset_prices):
    """
    Calculate asset returns based on asset prices.
    :param asset_prices: DataFrame containing asset prices with dates as index
    :return: DataFrame containing asset returns
    """
    return asset_prices.pct_change()


def portfolio_returns(asset_prices, weights):
    """
    Calculate expected portfolio performance
    The sum of the weights must be 1
    :param weights: weights as a vector -> np.array([0.25, 0.25, 0.25, 0.25])
    :param data_portfolio: asset prices
    :return: the portfolio return
    """
    return asset_prices.pct_change().dot(weights)


def ann_volatility(port_returns):
    """
    Calculate annualized volatility of portfolio returns.
    :param port_returns: Series containing portfolio returns
    :return: Series containing annualized volatility
    """
    returns_windowed = port_returns.rolling(30)
    annualized_volatility = returns_windowed.std() * np.sqrt(252)
    return annualized_volatility


def ann_cov(asset_ret):
    """
    Calculate annualized covariance matrix of asset returns.
    :param asset_ret: DataFrame containing asset returns
    :return: DataFrame containing annualized covariance matrix
    """
    return asset_ret.cov() * 252


def port_variance(covariance, weights):
    """
    Calculate portfolio variance based on covariance matrix and weights.
    :param covariance: DataFrame containing covariance matrix
    :param weights: Array of weights assigned to each asset in the portfolio
    :return: Portfolio volatility (float)
    """
    portfolio_variance = np.transpose(weights) @ covariance @ weights
    portfolio_volatility = np.sqrt(portfolio_variance)
    return portfolio_volatility
