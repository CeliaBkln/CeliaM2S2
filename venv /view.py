import matplotlib.pyplot as plt
import seaborn as sns


def plot_asset_prices(asset_prices):
    asset_prices.plot().set_ylabel('Closing Prices, USD')
    plt.show()


def plot_portfolio_returns(portfolio_returns):
    portfolio_returns.plot().set_ylabel("Daily Return, %")
    plt.show()


def plot_volatility(volatility_series):
    volatility_series.plot().set_ylabel("Annualized Volatility, 30-day Window")
    plt.show()


def cov_matrix(covariance):
    sns.heatmap(covariance, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matrice de covariance')
    plt.show()