import collections
import csv
from typing import Collection
import math


def save_dic_csv(file,collection,add_title=False):
    
    _title_printed = False


    with open(file, 'a') as f:
       
        space = '\n'
        for item in collection:
            line = ''
            title = ''
            for key in item.keys():
                title+=key+','
                line+=str(item[key])+','
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

def calculateFairPrice(intrest,eps,PE,price):
    if intrest == '-' or eps=='-' or PE == '-' or price == '-':
        return {
            "message":'missing params',
            "status":400
        }
    min_rate_of_return = 15/100
    margin_of_safty = 50/100
    years = 9
    intrest = float(intrest.split('%')[0])
    intrest = intrest /100
    eps = float(eps)
    PE = float(PE)
    price = float(price)
    future_val = round(math.pow(1+intrest,years)*eps*PE,2)
    fair_price = round(future_val/math.pow(1+min_rate_of_return,years),2)
    buy_price = round(fair_price * margin_of_safty,2)
    price_spread = round(price-buy_price,2)
    profit_potential = round((price-fair_price)/price,2)*100
    profit_potential = str(profit_potential)+'%'

    reuslt = {
        'fair_price':fair_price,
        'buy_price':buy_price,
        'price_spread':price_spread,
        'profit_potential':profit_potential,   
        "status":200
        
    }
    return reuslt



# result = calculateFairPrice(10,0.61,141.73,86.6)
# print(result)