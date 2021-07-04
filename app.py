from flask import request
from flask import Flask
import json
import src.get as get
import os


app = Flask(__name__)


@app.route('/scrapper/data')
def get_stock_data():
    ticker = request.args.get('ticker')
    result = get.get_ticker_data(ticker)
    return result


@app.route('/scrapper/screeners')
def get_screeners():
    result = get.get_screeners()
    return json.dumps(result)


@app.route('/health')
def health():

    return {"status": "online"}


app.run()
