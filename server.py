from flask import request
from flask import Flask
import json
import src.get as get
import os


finviz_api = Flask(__name__)


@finviz_api.route('/scrapper/data')
def get_stock_data():
    ticker = request.args.get('ticker')
    result = get.get_ticker_data(ticker)
    return result


@finviz_api.route('/scrapper/screeners')
def get_screeners():
    result = get.get_screeners()
    return json.dumps(result)


@finviz_api.route('/health')
def health():

    return {"status": "online"}


finviz_api.run()
