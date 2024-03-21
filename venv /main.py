import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from repository import get_portfolio, get_weights, get_end_date, get_begin_date
from model import asset_prices_middle, portfolio_returns, annualized_volatility
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
    plot_portfolio_returns()

    # Generate the covariance matrix from portfolio asset's returns
    Covariance = port_returns.cov()

    # Annualize the covariance using 252 trading days per year
    Covariance = Covariance * 252

    # Display the covariance matrix => view
    print(f"Covariance={Covariance}")

    portfolio_variance = np.transpose(weights) @ Covariance @ weights
    portfolio_volatility = np.sqrt(portfolio_variance)

    # display => view
    print(f"Portfolio volatility={portfolio_volatility}")

    # Compute the annualized volatility series
    returns_windowed = portfolio_returns.rolling(30)
    volatility_series = annualized_volatility(returns_windowed)

    # Plot the portfolio volatility => view
    plot_volatility(volatility_series)

if __name__ == "__main__":
    main()
