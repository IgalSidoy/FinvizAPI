import csv
from typing import Collection
import math
import time
from datetime import date, timedelta, datetime, timezone
import os


def convert_csv_to_object(file):

    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        result = []
        title = []
        for row in csv_reader:
            if len(title) == 0:
                title = row
                continue
            obj = {}
            for index in range(0, len(title)):
                if len(row) <= index:
                    continue
                obj[title[index]] = row[index]
            result.append(obj)
    return result


def save_dic_csv(file, collection, add_title=False, open_type='a'):

    _title_printed = False

    with open(file, open_type) as f:

        space = '\n'
        for item in collection:
            line = ''
            title = ''
            for key in item.keys():
                title += key+','
                line += str(item[key])+','
            line = line[:-1]
            title = title[:-1]
            if not _title_printed and add_title:
                _title_printed = True
                f.write(title+space)
            f.write(line+space)


def load_from_ignored(file):
    collection = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            collection.append(row.pop())
    return collection


def load_saved_symbols(file):
    collection = []
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            for col in row:
                collection.append(col)
                break
    return collection


def calculateFairPrice(intrest, eps, PE, price):
    if intrest == '-' or eps == '-' or PE == '-' or price == '-':
        return {
            "message": 'missing params',
            "status": 400
        }
    min_rate_of_return = 15/100
    margin_of_safty = 50/100
    years = 9
    intrest = float(intrest.split('%')[0])
    intrest = intrest / 100
    eps = float(eps)
    PE = float(PE)
    price = float(price)
    future_val = round(math.pow(1+intrest, years)*eps*PE, 2)
    fair_price = round(future_val/math.pow(1+min_rate_of_return, years), 2)
    buy_price = round(fair_price * margin_of_safty, 2)
    price_spread = round(price-buy_price, 2)
    profit_potential = round((price-fair_price)/price, 2)*100
    profit_potential = str(profit_potential)+'%'

    reuslt = {
        'fair_price': fair_price,
        'buy_price': buy_price,
        'price_spread': price_spread,
        'profit_potential': profit_potential,
        "status": 200

    }
    return reuslt


def remove_coma_end_convert_to_int(num, delimiter):

    if ',' in num:
        num = num.replace(',', delimiter)
        if type(num) == 'int':
            return int(num)

    return num


def get_time_range(days_back):
    today = int(time.time())
    days = days_back * 24*60*60
    result = {
        'from': today-days,
        'to': today
    }
    return result


def get_date(type='yyyy-mm-dd'):
    if type == 'yyyy-mm-dd':
        return date.today()
    if type == 'dd/mm/yyyy':
        split_date = str(date.today()).split('-')
        delimiter = '/'
        result_date = split_date[2]+delimiter + \
            split_date[1]+delimiter+split_date[0]
        return result_date


def working(count):
    clear()
    if count == 1:
        print("working\\")
        return count
    if count == 2:
        print("working|")
        return count
    if count == 3:
        print("working/")
        return count
    if count > 3:
        count = 0
        print("working-")
        return count


def finished(title):
    clear()
    if title == None:
        title = 'finished'
    print(title)


def clear():
    def clear(): return os.system('clear')
    clear()


def get_range_of_dates(from_date, to_date):
    _date = from_date.split('-')
    _from_date = date(int(_date[0]), int(_date[1]), int(_date[2]))
    _next = _from_date
    result = []
    stop = False
    while stop == False:
        if str(_next) == to_date:
            stop = True
        result.append(str(_next))
        _next = _next + timedelta(days=1)

    return result


def convert_metric_number(val):
    if val != '-':
        market_capitalization_type = val[-1]
        market_capitalization_value = float(val[:-1])
        if market_capitalization_type == 'B':
            market_capitalization = market_capitalization_value * 1000000000
        if market_capitalization_type == 'M':
            market_capitalization = market_capitalization_value * 1000000
        if market_capitalization_type == 'K':
            market_capitalization = market_capitalization_value * 1000
        return market_capitalization
    return val


def convert_percent_to_numbric(val):
    val = float(val[:-1])
    if type(val) == float:
        val = round((val/100), 4)
    return val


def get_range_date(date, days_back=14):

    date_arr = date.split('/')
    _year = int(date_arr[2])
    _month = int(date_arr[1])
    _day = int(date_arr[0])

    dt = datetime(_year, _month, _day)
    to_date = int(dt.replace(tzinfo=timezone.utc).timestamp())

    day = 60*60*24
    from_date = to_date-(day*days_back)
    to_date += day
    result = {
        'from_date': from_date,
        'to_date': to_date
    }
    return result
