import yfinance as yf
import datetime
from flask import Flask, redirect, url_for, render_template, request
from calculate_FOMO import calculate_FOMO

app = Flask(__name__)

@app.route('/', methods =['GET', 'POST'])
def home():
    if request.method == 'POST':
        ticker = request.form['ticker_input'].upper()
        initial_investment = int(request.form['initial_investment_input'])
        
        # remove zeros on left if included by user and split into list
        # format: MM/DD/YYYY -> [MM,DD,YYYY]
        datelst = request.form['date_input'].lstrip('0').split('/')
        date = [int(i) for i in datelst]

        month = date[0]
        day = date[1]
        year = date[2]

        formatted_future_value = calculate_FOMO(ticker, initial_investment, month, day, year)

        return render_template('FOMO.html', ticker=ticker, initial_investment=initial_investment, month=month, day=day, year=year, future_value=formatted_future_value)
    else:
        return render_template('index.html')

@app.route('/About')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=False)
