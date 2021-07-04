from flask import request
from flask import Flask
import json
import src.get as get
import os


finviz = Flask(__name__)


@finviz.route('/scrapper/data')
def get_stock_data():
    ticker = request.args.get('ticker')
    result = get.get_ticker_data(ticker)
    return result


@finviz.route('/scrapper/screeners')
def get_screeners():
    result = get.get_screeners()
    return json.dumps(result)


@finviz.route('/health')
def health():
    return {"status": "online"}


if __name__ == '__main__':
    finviz.run(debug=True)
