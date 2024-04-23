# working directory
import os
path = "/Users/bouaklinecelia/PycharmProjects/quantitative_risk_management1/"
os.chdir(path)

import numpy as np


from repository import get_portfolio, get_weights, get_end_date, get_begin_date
from model import asset_prices_middle, portfolio_returns, asset_returns, annualized_volatility
from view import plot_volatility, plot_asset_prices, plot_portfolio_returns


def main():
    portfolio = get_portfolio()
    begin_date = get_begin_date()
    end_date = get_end_date()
    weights = get_weights()

    # Select portfolio asset prices for the middle of the crisis, 2008-2009
    asset_prices = asset_prices_middle(portfolio, begin_date, end_date)

    # Plot portfolio's asset prices during this time
    plot_asset_prices(asset_prices)

    # Calculate portfolio returns
    port_returns = portfolio_returns(asset_prices, weights)

    # Plot portfolio returns
    plot_portfolio_returns(port_returns)

    # Generate the covariance matrix from portfolio asset's returns
    covariance = asset_returns.cov()

    # Annualize the covariance using 252 trading days per year
    covariance = covariance * 252

    # Display the covariance matrix => view
    print(f"covariance={covariance}")

    portfolio_variance = np.transpose(weights) @ covariance @ weights
    portfolio_volatility = np.sqrt(portfolio_variance)

    # display => view
    print(f"Portfolio volatility={portfolio_volatility}")

    # Compute the annualized volatility series
    returns_windowed = port_returns.rolling(30)
    volatility_series = annualized_volatility(returns_windowed)

    # Plot the portfolio volatility => view
    plot_volatility(volatility_series)


if __name__ == "__main__":
    print(dir())
    main()

