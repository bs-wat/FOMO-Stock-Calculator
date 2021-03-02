import yfinance as yf
import datetime

def calculate_FOMO(ticker_symbol, initial_investment, month, day, year):
    stock = yf.Ticker(ticker_symbol)
    past = datetime.date(year, month, day)

    current = datetime.date.today()

    hist = stock.history(start = past, end = current, auto_adjust = True )

    past_low = hist['Close'].values[0]

    today = stock.history(period='1d')
    current = today['Close'][0]

    shares = initial_investment / past_low

    future_investment = shares * current
    formatted_future_investment = "{:.2f}".format(future_investment)
    return formatted_future_investment