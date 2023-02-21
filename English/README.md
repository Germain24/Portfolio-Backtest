# Portfolio Backtest
Portfolio Backtest is a Python program designed to calculate and visualize the performance of a stock portfolio.

## Features
The program offers the following features:

- Retrieval of historical data for multiple stocks from the financialmodelingprep.com API 
- Calculation of each stock's contribution to the portfolio value using a given set of weights 
- Aggregation of contributions to obtain the total portfolio value over a given period of time 
- Plotting of the portfolio's performance over the given period of time 
- Calculation of various performance statistics, such as annual return, annual volatility, Sharpe ratio, and maximum drawdown

## How to Use
To use the program, you need to have Python 3.x installed on your system as well as the requests, pandas, numpy, and matplotlib.pyplot libraries. You can install these libraries by running the following command in your terminal:

```python
pip install requests pandas numpy matplotlib
```

Then, you can run the program by executing the portfolio_backtest.py file in your terminal with the following command:

```python
python Portoflio_Backtest.py
```

You can also customize the program by modifying the stock symbols and weights in the tickers and weights lists, as well as the start and end dates in the start_date and end_date variables.

## Author
Portfolio Backtest was created by Germain De Sousa.
