import requests
import connection as connection
from connection import headers
from data.stocks import us_stocks
from utility import save_dic_csv,load_from_ignored,load_saved_symbols,calculateFairPrice,remove_coma_end_convert_to_int,get_date,working,finished,convert_csv_to_object,get_range_of_dates
import os.path

def exception(code):
    if code == 404:
        return {"status": 404,
                "message": 'invalid/not found'}
    if code == 400:
        return {"status": 400,
                "message": 'bad request'}
    
def get_ticker_data(ticker):

    url = connection.get_url_ticker_data(ticker)
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        result = exception(res.status_code)
        return result

    encoding = 'utf-8'
    response = res.content.decode(encoding)
    result = response.split("<table")
    data = result[12].split("<tr")
    # --------------------data extraction-----------------------
    
    try:
        # -------------------------------line 1 data
        index = 1
        _data = data[index].split("<td")
        P_and_E = _data[4].split("><b>")[1].split("</b></td>")[0]
        EPS_ttm = _data[6].split("><b>")[1].split("</b></td>")[0]
        insider_Own = _data[8].split("><b>")[1].split("</b></td>")[0]
        shares_outstanding = _data[10].split("><b>")[1].split("</b></td>")[0]
        performance_week = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 2 data
        index = 2
        _data = data[index].split("<td")
        market_capitalization = _data[2].split("><b>")[1].split("</b></td>")[0]
        forward_price_to_earnings = _data[4].split("><b>")[1].split("</b></td>")[0]
        EPS_next_y = _data[6].split("><b>")[1].split("</b></td>")[0]
        insider_transactions = _data[8].split("><b>")[1].split("</b></td>")[0]
        shares_float = _data[10].split("><b>")[1].split("</b></td>")[0]
        performance_month = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 3 data
        index = 3
        _data = data[index].split("<td")
        income_ttm = _data[2].split("><b>")[1].split("</b></td>")[0]
        Price_to_Earnings_to_Growth = _data[4].split(
            "><b>")[1].split("</b></td>")[0]
        EPS_estimate_for_next_quarter = _data[6].split(
            "><b>")[1].split("</b></td>")[0]
        institutional_ownership = _data[8].split("><b>")[1].split("</b></td>")[0]
        short_interest_share = _data[10].split("><b>")[1].split("</b></td>")[0]
        performance_quarter = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 4 data
        index = 4
        _data = data[index].split("<td")
        revenue_ttm = _data[2].split("><b>")[1].split("</b></td>")[0]
        price_to_sales_ttm = _data[4].split("><b>")[1].split("</b></td>")[0]
        EPS_growth_this_year = _data[6].split("><b>")[1].split("</b></td>")[0]
        institutional_transactions_3_months = _data[8].split("><b>")[
            1].split("</b></td>")[0]
        short_interest_ratio = _data[10].split("><b>")[1].split("</b></td>")[0]
        performance_half_year = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 5 data
        index = 5
        _data = data[index].split("<td")
        book_value_per_share_mrq = _data[2].split("><b>")[1].split("</b></td>")[0]
        price_to_book_mrq = _data[4].split("><b>")[1].split("</b></td>")[0]
        EPS_growth_next_year = _data[6].split("><b>")[1].split("</b></td>")[0]
        return_on_assets_ttm = _data[8].split("><b>")[1].split("</b></td>")[0]
        target_price = _data[10].split("><b>")[1].split("</b></td>")[0]
        performance_year = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 6 data
        index = 6
        _data = data[index].split("<td")
        cash_per_share = _data[2].split("><b>")[1].split("</b></td>")[0]
        price_to_ash_per_share_mrq = _data[4].split(
            "><b>")[1].split("</b></td>")[0]
        long_term_annual_growth_estimate = _data[6].split(
            "><b>")[1].split("</b></td>")[0]
        return_on_equity_ttm = _data[8].split("><b>")[1].split("</b></td>")[0]
        _52_Week_trading_range = _data[10].split("><b>")[1].split("</b></td>")[0]
        performance_year_to_date = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 7 data
        index = 7
        _data = data[index].split("<td")
        dividend_annual = _data[2].split("><b>")[1].split("</b></td>")[0]
        price_to_free_cash_flow_ttm = _data[4].split(
            "><b>")[1].split("</b></td>")[0]
        EPS_past_5_years = _data[6].split("><b>")[1].split("</b></td>")[0]
        return_on_investment_ttm = _data[8].split("><b>")[1].split("</b></td>")[0]
        distance_from_52_week_high = _data[10].split(
            "><b>")[1].split("</b></td>")[0]
        beta = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 8 data
        index = 8
        _data = data[index].split("<td")
        dividend_yield_annual = _data[2].split("><b>")[1].split("</b></td>")[0]
        quick_ratio_mrq = _data[4].split("><b>")[1].split("</b></td>")[0]
        sales_past_5_years = _data[6].split("><b>")[1].split("</b></td>")[0]
        gross_margin_ttm = _data[8].split("><b>")[1].split("</b></td>")[0]
        distance_from_52_week_low = _data[10].split(
            "><b>")[1].split("</b></td>")[0]
        average_true_range_14 = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 9 data
        index = 9
        _data = data[index].split("<td")
        employees = _data[2].split("><b>")[1].split("</b></td>")[0]
        current_ratio_mrq = _data[4].split("><b>")[1].split("</b></td>")[0]
        quarterly_revenue_growth_yoy = _data[6].split(
            "><b>")[1].split("</b></td>")[0]
        operation_margin_ttm = _data[8].split("><b>")[1].split("</b></td>")[0]
        relative_strength_index = _data[10].split("><b>")[1].split("</b></td>")[0]
        volatility_week_month = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 10 data
        index = 10
        _data = data[index].split("<td")
        optionable = _data[2].split("><b>")[1].split("</b></td>")[0]
        total_debt_to_equity = _data[4].split("><b>")[1].split("</b></td>")[0]
        quarterly_earnings_growth_yoy = _data[6].split(
            "><b>")[1].split("</b></td>")[0]
        profit_margin = _data[8].split("><b>")[1].split("</b></td>")[0]
        relative_volume = _data[10].split("><b>")[1].split("</b></td>")[0]
        previous_close = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 11 data
        index = 11
        _data = data[index].split("<td")
        shortable = _data[2].split("><b>")[1].split("</b></td>")[0]
        long_term_debt_to_equity_mrq = _data[4].split(
            "><b>")[1].split("</b></td>")[0]
        earnings_date = _data[6].split("><b>")[1].split("</b></td>")[0]
        dividend_payout_ratio_ttm = _data[8].split("><b>")[1].split("</b></td>")[0]
        average_volume_3_months = _data[10].split("><b>")[1].split("</b></td>")[0]
        price = _data[12].split("><b>")[1].split("</b></td>")[0]
        # -------------------------------line 12 data
        index = 12
        _data = data[index].split("<td")
        analysts_mean_recommendation_1_buy_5_sell = _data[2].split("><b>")[
            1].split("</b></td>")[0]
        SMA_20 = _data[4].split("><b>")[1].split("</b></td>")[0]
        SMA50 = _data[6].split("><b>")[1].split("</b></td>")[0]
        SMA200 = _data[8].split("><b>")[1].split("</b></td>")[0]
        volume = _data[10].split("><b>")[1].split("</b></td>")[0]
        change_today = _data[12].split("><b>")[1].split("</b></td>")[0]

        if market_capitalization !='-':
            market_capitalization_type = market_capitalization[-1]
            market_capitalization_value = float(market_capitalization[:-1])
            if market_capitalization_type == 'B':
                market_capitalization = market_capitalization_value *1000000000
            if market_capitalization_type == 'M':
                market_capitalization = market_capitalization_value *1000000

        result = {
            "symbol":ticker,
            "status":'200',
            "P/E": P_and_E,
            "EPS(ttm)": EPS_ttm,
            "InsiderOwn": insider_Own,
            "SharesOutstanding": shares_outstanding,
            "Performance_Week": performance_week,
            "MarketCapitalization": str(market_capitalization),
            "Forward_P/E": forward_price_to_earnings,
            "EPS_Next_Year": EPS_next_y,
            "Insider_Transactions": insider_transactions,
            "Shares_Float": shares_float,
            "Performance_Month": performance_month,
            "Income(ttm)": income_ttm,
            "PEG": Price_to_Earnings_to_Growth,
            "EPS_Next_Quarter": EPS_estimate_for_next_quarter,
            "Institutional_Ownership": institutional_ownership,
            "Short_Float": short_interest_share,
            "Performance_Quarter": performance_quarter,
            "Sales": revenue_ttm,
            "P/S": price_to_sales_ttm,
            "EPS_This_Year": EPS_growth_this_year,
            "Inst_Trans": institutional_transactions_3_months,
            "Short_Ratio": short_interest_ratio,
            "Performance_Half_Year": performance_half_year,
            "Book/Share": book_value_per_share_mrq,
            "P/B": price_to_book_mrq,
            "EPS_Next_Year": EPS_growth_next_year,
            "Return_On_Assets_ttm": return_on_assets_ttm,
            "Target_Price": target_price,
            "Price": price,
            "Performance_Year": performance_year,
            "Cash/Share": cash_per_share,
            "P/C": price_to_ash_per_share_mrq,
            "EPS_Next_5Years": long_term_annual_growth_estimate,
            "return_on_equity_ttm": return_on_equity_ttm,
            "52W_Range": _52_Week_trading_range,
            "Performance_Year_To_Date": performance_year_to_date,
            "Dividend_Annual": dividend_annual,
            "P/FCF": price_to_free_cash_flow_ttm,
            "EPS_Past_5_Years": EPS_past_5_years,
            "ROI": return_on_investment_ttm,
            "52W_High": distance_from_52_week_high,
            "Beta": beta,
            "Dividend_Yield_Annual": dividend_yield_annual,
            "Quick_Ratio": quick_ratio_mrq,
            "Sales_Past_5_Years": sales_past_5_years,
            "Gross_Margin_ttm": gross_margin_ttm,
            "52W_Low": distance_from_52_week_low,
            "ATR": average_true_range_14,
            "Employees": employees,
            "Current_Ratio": current_ratio_mrq,
            "Sales Q/Q": quarterly_revenue_growth_yoy,
            "Operation_Margin": operation_margin_ttm,
            "RSI_14": relative_strength_index,
            "Volatility_Week/Month": volatility_week_month,
            "Optionable": optionable,
            "Total_Debt_To_Equity": total_debt_to_equity,
            "EPS Q/Q": quarterly_earnings_growth_yoy,
            "Profit_Margin": profit_margin,
            "Relative_Volume": relative_volume,
            "Previous_Close": previous_close,
            "Shortable": shortable,
            "LT_Debt/Eq": long_term_debt_to_equity_mrq,
            "Earnings_Date": earnings_date,
            "dividend_payout_ratio_ttm": dividend_payout_ratio_ttm,
            "Payout": dividend_payout_ratio_ttm,
            "Average_Volume_3_Months": average_volume_3_months,
            "Analysts mean recommendation (1=Buy 5=Sell)": analysts_mean_recommendation_1_buy_5_sell,
            "SMA_20": SMA_20,
            "SMA50": SMA50,
            "SMA200": SMA50,
            "Volume": volume,
            "Change_Today": change_today,
            'fair_price':'',
            'buy_price':'',
            'price_spread':'',
            'profit_potential':''
        }
        # -------------------remove extra html tags
        for item in result:
            if 'span' in result[item]:
                result[item] = result[item].split(">")[1].split("</span")[0]
            if "</small" in result[item]:
                result[item] = result[item].split(">")[1].split('<')[0]
            if "<small>" in result[item]:
                result[item] = result[item].replace('<small>','')
                result[item] = result[item].replace('</small>','')
        

        result['Volume'] = remove_coma_end_convert_to_int(result['Volume'],'')
        
        _price_range = result['52W_Range'].split('-')
        _low = float(_price_range[0])
        _high = float(_price_range[1])
        result['52W_Mid'] = round((_low+_high)/2,2)
        result['position_status'] = ''
        
        res = calculateFairPrice(result['EPS_Next_5Years'],result['EPS(ttm)'],result["P/E"],result['Price'])

        if res['status']==200:
            result['fair_price']=res['fair_price']
            result['buy_price']=res['buy_price']
            result['price_spread']=res['price_spread']
            result['profit_potential']=res['profit_potential']
            _buy_price = float(result['buy_price'])
            _price = float(result['Price'])
        
            if _buy_price>_price:
                result['position_status'] = 'Buy'
            else:
                result['position_status'] = 'Sell'
        return result
    except:
        print('exception')
        return exception(400)



def get_screeners():
    res = requests.get(connection.base_url, headers=headers)
    
    if res.status_code != 200:
        result = exception(res.status_code)
        return result

    encoding = 'utf-8'
    response = res.content.decode(encoding)
    data = response.split('<table')

    result = []
    for count in range(15, 17):
        _data = data[count].split('<tr')
        for index in range(2, len(_data)-2):
            name = _data[index].split("<td")[1].split(">")[
                2].replace('</b', '')
            industry = _data[index].split("<td")[1].split(
                ">")[4].split('|')[0].replace('&nbsp;', "")
            market_cap = _data[index].split("<td")[1].split(">")[4].split('|')[
                2].split(']')[0].replace(' ', '')
            ticker = _data[index].split("<td")[1].split(">")[
                6].replace('</a', "")
            last = _data[index].split("<td")[2].split('>')[
                1].replace('</td', '')
            change = _data[index].split("<td")[3].split('>')[
                2].replace('</span', '')
            volume = _data[index].split("<td")[4].split('>')[
                1].replace('</td', '')

            _temp = _data[index].split("<td")[6].split('</a>')
            _temp = _temp[len(_temp)-2].split('">')
            signal = _temp[len(_temp)-1]

            obj = {
                'ticker': ticker,
                'name': remove_coma_end_convert_to_int(name,' '),
                'industry': industry,
                'market_cap': market_cap,
                'last': last,
                'change': change,
                'volume': volume,
                'signal': signal
            }
            result.append(obj)
    return result

def scan_stocks(file_name='./data/dataset.csv'):
    save_file = file_name
    add_Title = True

    ignored_file = './data/ignored.csv'

    existing_ignored_collection = load_from_ignored(ignored_file)
    if check_file_exist(save_file)==False:
        save_dic_csv(save_file,[],False,'w')
    existing_in_dataset_collection = load_saved_symbols(save_file)

    if len(existing_in_dataset_collection)>0:
        add_Title = False

    total_count = 0
    collection=[]
    ignore_collection = []
    for s in us_stocks:
        total_count+=1
        symbol = s['symbol'].strip()
        #check if the symbol already exists or no data were found in the last check.
        if symbol in existing_ignored_collection or symbol in existing_in_dataset_collection:
            print(symbol +' - ignored')
            continue
        print('####################')
        print("symbol -- " + symbol)
        res = get_ticker_data(symbol)
        
        status = res['status']
        if status == 'NoneType':
            continue
        status = int(status)

        print('-----------------------------> '+str(status)+" status")
        print('-----------------------------> '+str(total_count)+" total")
        print('-----------------------------> '+str(len(ignore_collection))+" ignore_collection")
        print('-----------------------------> '+str(len(collection))+" collection")
        
        if len(ignore_collection)>5:
            save_dic_csv(ignored_file,ignore_collection,False)
            ignore_collection = []

        if len(collection)>5:
            save_dic_csv(save_file,collection,add_Title)
            collection = []
            add_Title = False

        if status > 200:
            ignore_collection.append({'symbol':symbol})
            continue

        if res['fair_price'] == '':
            ignore_collection.append({'symbol':symbol})
            continue
        
        #created finished recored
        _res = {
                "Symbol":res['symbol'],
                "MarketCap":res["MarketCapitalization"],
                "P/E":res['P/E'],
                "EPS(ttm)":res['EPS(ttm)'],
                "Fair_Price":res['fair_price'],
                "Buy_Price":res['buy_price'],
                "Price":res['Price'],
                "Target_Price":res['Target_Price'],
                "52W_Range":res['52W_Range'],
                "52W_High":res['52W_High'],
                '52W_Mid':res['52W_Mid'],
                "52W_Low":res['52W_Low'],
                "Volume":res['Volume'],
                "RSI_14":res['RSI_14'],
                "ATR":res['ATR'],
                "Position_Status":res['position_status']
               
        }
        collection.append(_res)        
        
def short_invest_daily():

    date = get_date()
    name = './data/short_invest-'+str(date)+'.csv'
    f = open(name, "w")
    f.close()
    collection = get_screeners()

    duplicate_pointer =[]
    result = []
    count = 0
    for rec in collection:
        
        ticker = rec['ticker']
        if ticker in duplicate_pointer:
            continue
        duplicate_pointer.append(ticker)
        data =  get_ticker_data(ticker)
        count+=1
        price = float(data['Price'])
        prev_price = float(data['Previous_Close'])
        ATR_one_day = round(price-prev_price,2)
        ATR_14 = float(data['ATR'])
        ATR_change = abs(round(ATR_one_day/ATR_14,2))
        price_delta = round((ATR_14+ATR_one_day)/2,2)
        change = float(rec['change'].split("%")[0])
        if change>0:
            price_delta = price-price_delta
        else:
            price_delta = price+price_delta
        res = {
                "Symbol":data['symbol'],
                "Status":'pending',
                "Industry":rec['industry'],
                "MarketCap":data["MarketCapitalization"],
                "P/E":data['P/E'],
                "EPS(ttm)":data['EPS(ttm)'],
                "Fair_Price":data['fair_price'],
                "Buy_Price":data['buy_price'],
                "Price":data['Price'],
                'Previous_Close':data['Previous_Close'],
                "Target_Price":data['Target_Price'],
                "52W_Range":data['52W_Range'],
                "52W_High":data['52W_High'],
                '52W_Mid':data['52W_Mid'],
                "52W_Low":data['52W_Low'],
                "Volume":data['Volume'],
                "RSI_14":data['RSI_14'],
                "ATR":data['ATR'],
                "ATR One Day":ATR_one_day,
                "ATR_change":ATR_change,
                "Position_Status":data['position_status'],
                "Ratio-Change":rec['change'],
                'Signal':rec['signal'],
                "Exit_Price":price_delta
        }
        
        count = working(count)
        result.append(res)

    save_dic_csv(name,result,True)
    finished('report - '+name.split('/')[2] +' created successfully.')    

def get_file_name(date):
    return './data/short_invest-'+date+'.csv'

def check_file_exist(file):
    result = os.path.isfile(file) 
    if result == False:
        return False
    return True

def update_price_from_file(date):
    file = get_file_name(date)

    if check_file_exist(file) == False:
        return

    collection = convert_csv_to_object(file)
    today_price_title ='price '+ str(get_date())
    count = 0
    result = []
    for item in collection:
        count +=1
        symbol = item['Symbol']
        response = get_ticker_data(symbol)
        if response['status'] == 404:
            continue
        price = response['Price']
        item[today_price_title] = price
        result.append(item)
        count = working(count)
    save_dic_csv(file,result,True,'w')
    finished('fetching current prices finshed.')

def merge_all_csv(start_date,result_file_name='./data/invest_report.csv'):
    file_name = result_file_name
    dates = get_range_of_dates(start_date,str(get_date()))
    result = []
    for date in dates:
        file  = get_file_name(date)
        if check_file_exist(file) == False:
            continue
        collection = convert_csv_to_object(file)
        for item in collection:
            result.append(item)
    save_dic_csv(file_name,result,True,'w')

def daily_automate(start_date,fetch_data=True):
    if fetch_data:
        short_invest_daily()
        dates = get_range_of_dates(start_date,str(get_date()))
        for date in dates:
            update_price_from_file(date)
    merge_all_csv(start_date)

# daily_automate('2021-07-18',True)

#scan_stocks()
# print(get_ticker_data('NUGT'))

