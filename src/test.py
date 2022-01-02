from insights import extract_insights
from utility import load_from_ignored
from utility import convert_csv_to_object
from utility import save_dic_csv
from data.stocks import us_stocks
from pathlib import Path


def scan_stocks():
    ignored_file = './data/ignored.csv'
    result_file = './data/correlation.csv'
    period=5
    spike_triger=20
    existing_ignored_collection = load_from_ignored(ignored_file)
    my_file = Path(result_file)
    if my_file.is_file():
        dic_results = convert_csv_to_object(result_file)
    else:
        dic_results=[]

    exists = []
    for i in dic_results:
        exists.append(i['symbol'])
    total_count = 0
    
    for s in us_stocks:
        symbol = s['symbol'].strip()
        # check if the symbol already exists or no data were found in the last check.
        if symbol in existing_ignored_collection or symbol in exists:
            continue

        total_count += 1
        print('####################')
        print("symbol -- " + symbol+' '+str(total_count)+")")
        symbol_res = extract_insights(symbol,period,spike_triger)
        if symbol_res == None or symbol_res['correlation'] == 0:
            dic_results.append({
                'symbol':symbol,
                'correlation':''
                })
            continue

        dic_results.append({
            'symbol':symbol,
            'correlation':symbol_res['correlation']
        })
        print('here')
        if total_count%9 == 0 or total_count>10 :
            save_dic_csv(result_file,dic_results,True,'w')
            total_count= 0

    return dic_results


print(scan_stocks())