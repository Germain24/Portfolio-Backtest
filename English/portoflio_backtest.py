# Import libraries
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Define tickers and weights of the portfolio
tickers = ['AAPL', 'MSFT']
weights = [0.25, 0.25]

# Define start and end date
start_date = '2018-02-16'
end_date = '2023-02-16'

# Normalize weights
weights = [x / sum(weights) for x in weights]


def get_portfolio_value(start_date, end_date):
    df0 = pd.DataFrame(index=pd.date_range(start=start_date, end=end_date, freq='D'), columns=['changement']).fillna(value=0)
    for i, ticker in enumerate(tickers):
        url = f'https://financialmodelingprep.com/api/v3/historical-price-full/{ticker}?from={start_date}&to={end_date}&apikey=ce82b6a14287d6b24fdcaf5468401b12'
        data = requests.get(url).json()['historical']
        df = pd.DataFrame(data)
        df.set_index(pd.to_datetime(df['date'], format='%Y-%m-%d'), inplace=True)
        df["changement"] = weights[i] * (df['close'] / df['close'][-1])
        df.drop(['close', 'date',"open","high","low","label","changeOverTime","adjClose","volume","vwap","unadjustedVolume","change","changePercent"], axis=1, inplace=True)

        df = df.reindex(pd.date_range(start=start_date, end=end_date), fill_value=np.nan)
        df.fillna(method='bfill', inplace=True)
        df.fillna(method='ffill', inplace=True)

        df0['changement'] = df0['changement']+df['changement']

    return df0.replace(0, np.nan).dropna()


def plot_portfolio_value(portfolio_value):
    portfolio_value.plot(figsize=(10, 6))
    plt.title('Évolution du rendement du portefeuille')
    plt.xlabel('Date')
    plt.ylabel('Valeur du portefeuille')
    plt.grid(True)
    plt.show()

# Calculate and plot the portfolio value over time
portfolio_value = get_portfolio_value(start_date, end_date)
plot_portfolio_value(portfolio_value)

# Print performance metrics for the portfolio
print('Portfolio Performance Metrics:')
print(f"- Annual return: {round(float(100 * portfolio_value.pct_change().mean() * 365.25),2)}%.")
print(f"- Annual volatility: {round(float(100 * portfolio_value.pct_change().std() * 365.25 ** 0.5),2)}%.")
print(f"- Sharpe ratio: {round(float(portfolio_value.pct_change().mean() / portfolio_value.pct_change().std() * 365.25 ** 0.5),2)}.")
print(f"- Maximum Drawdown: {round(float((( portfolio_value / portfolio_value.cummax()) - 1).min())*100,2)}%.")