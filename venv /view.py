import matplotlib.pyplot as plt
import seaborn as sns
from repository import get_config

# Charger la configuration
config = get_config()


def plot_asset_prices(asset_prices):
    asset_prices.plot(color=config['chart']['color']).set_ylabel('Closing Prices, USD')
    plt.title(config['view']['closing'])
    plt.show()


def plot_portfolio_returns(portfolio_returns):
    portfolio_returns.plot(color=config['chart']['color']).set_ylabel("Daily Return, %")
    plt.title(config['view']['returns'])
    plt.show()


def plot_volatility(volatility_series):
    volatility_series.plot(color=config['chart']['color']).set_ylabel("Annualized Volatility, 30-day Window")
    plt.title(config['view']['volatility'])
    plt.show()


def cov_matrix(covariance):
    sns.heatmap(covariance, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title(config['view']['covariance'])
    plt.show()
