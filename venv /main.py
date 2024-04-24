# working directory
import os

path = "/Users/bouaklinecelia/PycharmProjects/quantitative_risk_management1/"
os.chdir(path)

from repository import get_portfolio, get_weights, get_end_date, get_begin_date
from model import (
    asset_prices_middle,
    portfolio_returns,
    ann_volatility,
    asset_returns,
    ann_cov,
    port_variance,
)
from view import plot_volatility, plot_asset_prices, plot_portfolio_returns, cov_matrix


def main():
    portfolio = get_portfolio()
    begin_date = get_begin_date()
    end_date = get_end_date()
    weights = get_weights()

    # Select portfolio asset prices for the middle of the crisis, 2008-2009
    asset_prices = asset_prices_middle(portfolio, begin_date, end_date)
    asset_ret = asset_returns(asset_prices)

    # Plot portfolio's asset prices during this time
    plot_asset_prices(asset_prices)

    # Calculate portfolio returns
    port_returns = portfolio_returns(asset_prices, weights)

    # Plot portfolio returns
    plot_portfolio_returns(port_returns)

    # Generate the covariance matrix from portfolio asset's returns and annualize it
    covariance = ann_cov(asset_ret)
    cov_matrix(covariance)

    # Display the covariance matrix => view
    print(f"covariance={covariance}")

    # Calculate portfolio volatility
    portfolio_volatility = port_variance(covariance, weights)

    # display => view
    print(f"Portfolio volatility={portfolio_volatility}")

    # Compute the annualized volatility series
    annualized_volatility = ann_volatility(port_returns)

    # Plot the portfolio volatility => view
    plot_volatility(annualized_volatility)

    # Display results


if __name__ == "__main__":
    print(dir())
    main()
